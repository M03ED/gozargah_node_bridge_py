# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: GozargahNodeBridge/common/service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'GozargahNodeBridge/common/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'GozargahNodeBridge/common/service.proto\x12\x07service\"\x07\n\x05\x45mpty\"r\n\x10\x42\x61seInfoResponse\x12\x0f\n\x07started\x18\x01 \x01(\x08\x12\x14\n\x0c\x63ore_version\x18\x02 \x01(\t\x12\x14\n\x0cnode_version\x18\x03 \x01(\t\x12\x12\n\nsession_id\x18\x04 \x01(\t\x12\r\n\x05\x65xtra\x18\x05 \x01(\t\"o\n\x07\x42\x61\x63kend\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.service.BackendType\x12\x0e\n\x06\x63onfig\x18\x02 \x01(\t\x12\x1c\n\x05users\x18\x03 \x03(\x0b\x32\r.service.User\x12\x12\n\nkeep_alive\x18\x04 \x01(\x04\"\x15\n\x03Log\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t\"?\n\x04Stat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x03\",\n\x0cStatResponse\x12\x1c\n\x05stats\x18\x01 \x03(\x0b\x32\r.service.Stat\"*\n\x0bStatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05reset\x18\x02 \x01(\x08\"\x81\x01\n\x12OnlineStatResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x03ips\x18\x02 \x03(\x0b\x32$.service.OnlineStatResponse.IpsEntry\x1a*\n\x08IpsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xcc\x01\n\x14\x42\x61\x63kendStatsResponse\x12\x15\n\rnum_goroutine\x18\x01 \x01(\r\x12\x0e\n\x06num_gc\x18\x02 \x01(\r\x12\r\n\x05\x61lloc\x18\x03 \x01(\x04\x12\x13\n\x0btotal_alloc\x18\x04 \x01(\x04\x12\x0b\n\x03sys\x18\x05 \x01(\x04\x12\x0f\n\x07mallocs\x18\x06 \x01(\x04\x12\r\n\x05\x66rees\x18\x07 \x01(\x04\x12\x14\n\x0clive_objects\x18\x08 \x01(\x04\x12\x16\n\x0epause_total_ns\x18\t \x01(\x04\x12\x0e\n\x06uptime\x18\n \x01(\r\"\xa4\x01\n\x13SystemStatsResponse\x12\x11\n\tmem_total\x18\x01 \x01(\x04\x12\x10\n\x08mem_used\x18\x02 \x01(\x04\x12\x11\n\tcpu_cores\x18\x03 \x01(\x04\x12\x11\n\tcpu_usage\x18\x04 \x01(\x01\x12 \n\x18incoming_bandwidth_speed\x18\x05 \x01(\x04\x12 \n\x18outgoing_bandwidth_speed\x18\x06 \x01(\x04\"\x13\n\x05Vmess\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x05Vless\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x66low\x18\x02 \x01(\t\"\x1a\n\x06Trojan\x12\x10\n\x08password\x18\x01 \x01(\t\"/\n\x0bShadowsocks\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\"\x91\x01\n\x05Proxy\x12\x1d\n\x05vmess\x18\x01 \x01(\x0b\x32\x0e.service.Vmess\x12\x1d\n\x05vless\x18\x02 \x01(\x0b\x32\x0e.service.Vless\x12\x1f\n\x06trojan\x18\x03 \x01(\x0b\x32\x0f.service.Trojan\x12)\n\x0bshadowsocks\x18\x04 \x01(\x0b\x32\x14.service.Shadowsocks\"H\n\x04User\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x1f\n\x07proxies\x18\x02 \x01(\x0b\x32\x0e.service.Proxy\x12\x10\n\x08inbounds\x18\x03 \x03(\t\"%\n\x05Users\x12\x1c\n\x05users\x18\x01 \x03(\x0b\x32\r.service.User*\x17\n\x0b\x42\x61\x63kendType\x12\x08\n\x04XRAY\x10\x00\x32\x92\x07\n\x0bNodeService\x12\x36\n\x05Start\x12\x10.service.Backend\x1a\x19.service.BaseInfoResponse\"\x00\x12(\n\x04Stop\x12\x0e.service.Empty\x1a\x0e.service.Empty\"\x00\x12:\n\x0bGetBaseInfo\x12\x0e.service.Empty\x1a\x19.service.BaseInfoResponse\"\x00\x12+\n\x07GetLogs\x12\x0e.service.Empty\x1a\x0c.service.Log\"\x00\x30\x01\x12@\n\x0eGetSystemStats\x12\x0e.service.Empty\x1a\x1c.service.SystemStatsResponse\"\x00\x12\x42\n\x0fGetBackendStats\x12\x0e.service.Empty\x1a\x1d.service.BackendStatsResponse\"\x00\x12\x42\n\x11GetOutboundsStats\x12\x14.service.StatRequest\x1a\x15.service.StatResponse\"\x00\x12\x41\n\x10GetOutboundStats\x12\x14.service.StatRequest\x1a\x15.service.StatResponse\"\x00\x12\x41\n\x10GetInboundsStats\x12\x14.service.StatRequest\x1a\x15.service.StatResponse\"\x00\x12@\n\x0fGetInboundStats\x12\x14.service.StatRequest\x1a\x15.service.StatResponse\"\x00\x12>\n\rGetUsersStats\x12\x14.service.StatRequest\x1a\x15.service.StatResponse\"\x00\x12=\n\x0cGetUserStats\x12\x14.service.StatRequest\x1a\x15.service.StatResponse\"\x00\x12I\n\x12GetUserOnlineStats\x12\x14.service.StatRequest\x1a\x1b.service.OnlineStatResponse\"\x00\x12-\n\x08SyncUser\x12\r.service.User\x1a\x0e.service.Empty\"\x00(\x01\x12-\n\tSyncUsers\x12\x0e.service.Users\x1a\x0e.service.Empty\"\x00\x42\x18Z\x16marzban_node_go/commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GozargahNodeBridge.common.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\026marzban_node_go/common'
  _globals['_ONLINESTATRESPONSE_IPSENTRY']._loaded_options = None
  _globals['_ONLINESTATRESPONSE_IPSENTRY']._serialized_options = b'8\001'
  _globals['_BACKENDTYPE']._serialized_start=1368
  _globals['_BACKENDTYPE']._serialized_end=1391
  _globals['_EMPTY']._serialized_start=52
  _globals['_EMPTY']._serialized_end=59
  _globals['_BASEINFORESPONSE']._serialized_start=61
  _globals['_BASEINFORESPONSE']._serialized_end=175
  _globals['_BACKEND']._serialized_start=177
  _globals['_BACKEND']._serialized_end=288
  _globals['_LOG']._serialized_start=290
  _globals['_LOG']._serialized_end=311
  _globals['_STAT']._serialized_start=313
  _globals['_STAT']._serialized_end=376
  _globals['_STATRESPONSE']._serialized_start=378
  _globals['_STATRESPONSE']._serialized_end=422
  _globals['_STATREQUEST']._serialized_start=424
  _globals['_STATREQUEST']._serialized_end=466
  _globals['_ONLINESTATRESPONSE']._serialized_start=469
  _globals['_ONLINESTATRESPONSE']._serialized_end=598
  _globals['_ONLINESTATRESPONSE_IPSENTRY']._serialized_start=556
  _globals['_ONLINESTATRESPONSE_IPSENTRY']._serialized_end=598
  _globals['_BACKENDSTATSRESPONSE']._serialized_start=601
  _globals['_BACKENDSTATSRESPONSE']._serialized_end=805
  _globals['_SYSTEMSTATSRESPONSE']._serialized_start=808
  _globals['_SYSTEMSTATSRESPONSE']._serialized_end=972
  _globals['_VMESS']._serialized_start=974
  _globals['_VMESS']._serialized_end=993
  _globals['_VLESS']._serialized_start=995
  _globals['_VLESS']._serialized_end=1028
  _globals['_TROJAN']._serialized_start=1030
  _globals['_TROJAN']._serialized_end=1056
  _globals['_SHADOWSOCKS']._serialized_start=1058
  _globals['_SHADOWSOCKS']._serialized_end=1105
  _globals['_PROXY']._serialized_start=1108
  _globals['_PROXY']._serialized_end=1253
  _globals['_USER']._serialized_start=1255
  _globals['_USER']._serialized_end=1327
  _globals['_USERS']._serialized_start=1329
  _globals['_USERS']._serialized_end=1366
  _globals['_NODESERVICE']._serialized_start=1394
  _globals['_NODESERVICE']._serialized_end=2308
# @@protoc_insertion_point(module_scope)
