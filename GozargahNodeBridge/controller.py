import ssl
import asyncio
from enum import IntEnum
from pathlib import Path
from typing import Optional, List

from aiorwlock import RWLock

from GozargahNodeBridge.common.service_pb2 import User
from GozargahNodeBridge.utils import string_to_temp_file


class RollingQueue(asyncio.Queue):
    async def put(self, item):
        while self.maxsize > 0 and self.full():
            await self.get()
        await super().put(item)


class NodeAPIError(Exception):
    def __init__(self, code, detail):
        self.code = code
        self.detail = detail

    def __str__(self):
        return f"NodeAPIError(code={self.code}, detail={self.detail})"


class Health(IntEnum):
    NOT_CONNECTED = 0
    BROKEN = 1
    HEALTHY = 2


class Controller:
    def __init__(
        self, client_cert: str, client_key: str, server_ca: str, extra: dict | None = None, max_logs: int = 1000
    ):
        self.max_logs = max_logs
        self._temp_files = []
        if extra is None:
            extra = {}
        try:
            ca_path = string_to_temp_file(server_ca)
            cert_path = string_to_temp_file(client_cert)
            key_path = string_to_temp_file(client_key)
            self._temp_files.extend([Path(ca_path), Path(cert_path), Path(key_path)])

            self.ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            self.ctx.set_alpn_protocols(["h2"])
            self.ctx.load_verify_locations(cafile=ca_path)
            self.ctx.load_cert_chain(certfile=cert_path, keyfile=key_path)
            self.ctx.check_hostname = False
            self.ctx.verify_mode = ssl.CERT_REQUIRED

        except (ssl.SSLError, IOError) as e:
            self._cleanup_temp_files()
            raise NodeAPIError(-1, f"SSL initialization failed: {str(e)}")

        self._health = Health.NOT_CONNECTED
        self._user_queue: asyncio.Queue[User] | None = None
        self._logs_queue: RollingQueue[str] | None = None
        self._notify_queue: asyncio.Queue | None = None
        self._tasks: List[asyncio.Task] = []
        self._node_version = ""
        self._core_version = ""
        self._extra = extra
        self._lock = RWLock()

    def _cleanup_temp_files(self):
        """Clean up temporary certificate files"""
        for path in self._temp_files:
            try:
                path.unlink(missing_ok=True)
            except Exception:
                pass

    def __del__(self):
        self._cleanup_temp_files()

    async def set_health(self, health: Health):
        async with self._lock.writer_lock:
            if health == Health.BROKEN and self._health != Health.BROKEN:
                if self._notify_queue:
                    await self._notify_queue.put(None)
            self._health = health

    async def get_health(self) -> Health:
        async with self._lock.reader_lock:
            return self._health

    async def connected(self) -> bool:
        if await self.get_health() == Health.NOT_CONNECTED:
            raise NodeAPIError(code=0, detail="Node is not connected")
        return True

    async def update_user(self, user: User):
        await self.connected()
        async with self._lock.writer_lock:
            if self._user_queue:
                await self._user_queue.put(user)

    async def remove_user(self, user: User):
        await self.connected()
        async with self._lock.writer_lock:
            if self._user_queue:
                user.inbounds.clear()
                await self._user_queue.put(user)

    async def get_logs(self) -> Optional[asyncio.Queue]:
        await self.connected()
        async with self._lock.reader_lock:
            return self._logs_queue

    @property
    async def node_version(self) -> str:
        async with self._lock.reader_lock:
            return self._node_version

    @property
    async def core_version(self) -> str:
        async with self._lock.reader_lock:
            return self._core_version

    async def get_extra(self) -> dict:
        async with self._lock.reader_lock:
            return self._extra

    async def connect(self, node_version: str, core_version: str, tasks: List[asyncio.Task] | None = None):
        if tasks is None:
            tasks = []
        async with self._lock.writer_lock:
            self._user_queue = asyncio.Queue()
            self._notify_queue = asyncio.Queue()
            self._logs_queue = RollingQueue(self.max_logs)
            self._tasks = tasks
            self._node_version = node_version
            self._core_version = core_version
            self._health = Health.HEALTHY

    async def disconnect(self):
        async with self._lock.writer_lock:
            for task in self._tasks:
                task.cancel()

            await asyncio.gather(*self._tasks, return_exceptions=True)
            self._tasks.clear()

            if self._user_queue:
                await self._user_queue.put(None)
                self._user_queue = None

            if self._notify_queue:
                await self._notify_queue.put(None)
                self._notify_queue = None

            if self._logs_queue:
                await self._logs_queue.put(None)
                self._logs_queue = None

            self._node_version = ""
            self._core_version = ""
            self._health = Health.NOT_CONNECTED
