# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\x04test\"*\n\rHelloWorldReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"!\n\x0fHelloWorldReply\x12\x0e\n\x06result\x18\x01 \x01(\t\"\x9f\x02\n\x10helloTestRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\t\x12\x32\n\x06number\x18\x04 \x03(\x0b\x32\".test.helloTestRequest.NumberEntry\x1aK\n\x1bhelloTestRequestNumberValue\x12\x0c\n\x04name\x18\x0b \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x11\n\tis_active\x18\x03 \x01(\x08\x1a\x61\n\x0bNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.test.helloTestRequest.helloTestRequestNumberValue:\x02\x38\x01\"\x10\n\x0ehelloTestReply\"+\n\x1bTestClientRecvStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientRecvStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"+\n\x1bTestClientSendStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientSendStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"\'\n\x17TestTwoWayStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"*\n\x18TestTwoWayStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\xa3\x03\n\x05hello\x12:\n\nHelloWorld\x12\x13.test.HelloWorldReq\x1a\x15.test.HelloWorldReply\"\x00\x12?\n\thelloTest\x12\x16.test.helloTestRequest\x1a\x14.test.helloTestReply\"\x00(\x01\x30\x01\x12\x61\n\x14TestClientRecvStream\x12!.test.TestClientRecvStreamRequest\x1a\".test.TestClientRecvStreamResponse\"\x00\x30\x01\x12\x61\n\x14TestClientSendStream\x12!.test.TestClientSendStreamRequest\x1a\".test.TestClientSendStreamResponse\"\x00(\x01\x12W\n\x10TestTwoWayStream\x12\x1d.test.TestTwoWayStreamRequest\x1a\x1e.test.TestTwoWayStreamResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_HELLOWORLDREQ = _descriptor.Descriptor(
  name='HelloWorldReq',
  full_name='test.HelloWorldReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloWorldReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloWorldReq.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=68,
)


_HELLOWORLDREPLY = _descriptor.Descriptor(
  name='HelloWorldReply',
  full_name='test.HelloWorldReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.HelloWorldReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=103,
)


_HELLOTESTREQUEST_HELLOTESTREQUESTNUMBERVALUE = _descriptor.Descriptor(
  name='helloTestRequestNumberValue',
  full_name='test.helloTestRequest.helloTestRequestNumberValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.helloTestRequest.helloTestRequestNumberValue.name', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.helloTestRequest.helloTestRequestNumberValue.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='test.helloTestRequest.helloTestRequestNumberValue.is_active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=294,
)

_HELLOTESTREQUEST_NUMBERENTRY = _descriptor.Descriptor(
  name='NumberEntry',
  full_name='test.helloTestRequest.NumberEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test.helloTestRequest.NumberEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='test.helloTestRequest.NumberEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=393,
)

_HELLOTESTREQUEST = _descriptor.Descriptor(
  name='helloTestRequest',
  full_name='test.helloTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.helloTestRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.helloTestRequest.age', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='test.helloTestRequest.data', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='test.helloTestRequest.number', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HELLOTESTREQUEST_HELLOTESTREQUESTNUMBERVALUE, _HELLOTESTREQUEST_NUMBERENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=393,
)


_HELLOTESTREPLY = _descriptor.Descriptor(
  name='helloTestReply',
  full_name='test.helloTestReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=395,
  serialized_end=411,
)


_TESTCLIENTRECVSTREAMREQUEST = _descriptor.Descriptor(
  name='TestClientRecvStreamRequest',
  full_name='test.TestClientRecvStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestClientRecvStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=456,
)


_TESTCLIENTRECVSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestClientRecvStreamResponse',
  full_name='test.TestClientRecvStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestClientRecvStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=504,
)


_TESTCLIENTSENDSTREAMREQUEST = _descriptor.Descriptor(
  name='TestClientSendStreamRequest',
  full_name='test.TestClientSendStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestClientSendStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=549,
)


_TESTCLIENTSENDSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestClientSendStreamResponse',
  full_name='test.TestClientSendStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestClientSendStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=597,
)


_TESTTWOWAYSTREAMREQUEST = _descriptor.Descriptor(
  name='TestTwoWayStreamRequest',
  full_name='test.TestTwoWayStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestTwoWayStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=638,
)


_TESTTWOWAYSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestTwoWayStreamResponse',
  full_name='test.TestTwoWayStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestTwoWayStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=682,
)

_HELLOTESTREQUEST_HELLOTESTREQUESTNUMBERVALUE.containing_type = _HELLOTESTREQUEST
_HELLOTESTREQUEST_NUMBERENTRY.fields_by_name['value'].message_type = _HELLOTESTREQUEST_HELLOTESTREQUESTNUMBERVALUE
_HELLOTESTREQUEST_NUMBERENTRY.containing_type = _HELLOTESTREQUEST
_HELLOTESTREQUEST.fields_by_name['number'].message_type = _HELLOTESTREQUEST_NUMBERENTRY
DESCRIPTOR.message_types_by_name['HelloWorldReq'] = _HELLOWORLDREQ
DESCRIPTOR.message_types_by_name['HelloWorldReply'] = _HELLOWORLDREPLY
DESCRIPTOR.message_types_by_name['helloTestRequest'] = _HELLOTESTREQUEST
DESCRIPTOR.message_types_by_name['helloTestReply'] = _HELLOTESTREPLY
DESCRIPTOR.message_types_by_name['TestClientRecvStreamRequest'] = _TESTCLIENTRECVSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestClientRecvStreamResponse'] = _TESTCLIENTRECVSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['TestClientSendStreamRequest'] = _TESTCLIENTSENDSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestClientSendStreamResponse'] = _TESTCLIENTSENDSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['TestTwoWayStreamRequest'] = _TESTTWOWAYSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestTwoWayStreamResponse'] = _TESTTWOWAYSTREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloWorldReq = _reflection.GeneratedProtocolMessageType('HelloWorldReq', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDREQ,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloWorldReq)
  })
_sym_db.RegisterMessage(HelloWorldReq)

HelloWorldReply = _reflection.GeneratedProtocolMessageType('HelloWorldReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloWorldReply)
  })
_sym_db.RegisterMessage(HelloWorldReply)

helloTestRequest = _reflection.GeneratedProtocolMessageType('helloTestRequest', (_message.Message,), {

  'helloTestRequestNumberValue' : _reflection.GeneratedProtocolMessageType('helloTestRequestNumberValue', (_message.Message,), {
    'DESCRIPTOR' : _HELLOTESTREQUEST_HELLOTESTREQUESTNUMBERVALUE,
    '__module__' : 'helloworld_pb2'
    # @@protoc_insertion_point(class_scope:test.helloTestRequest.helloTestRequestNumberValue)
    })
  ,

  'NumberEntry' : _reflection.GeneratedProtocolMessageType('NumberEntry', (_message.Message,), {
    'DESCRIPTOR' : _HELLOTESTREQUEST_NUMBERENTRY,
    '__module__' : 'helloworld_pb2'
    # @@protoc_insertion_point(class_scope:test.helloTestRequest.NumberEntry)
    })
  ,
  'DESCRIPTOR' : _HELLOTESTREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.helloTestRequest)
  })
_sym_db.RegisterMessage(helloTestRequest)
_sym_db.RegisterMessage(helloTestRequest.helloTestRequestNumberValue)
_sym_db.RegisterMessage(helloTestRequest.NumberEntry)

helloTestReply = _reflection.GeneratedProtocolMessageType('helloTestReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOTESTREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.helloTestReply)
  })
_sym_db.RegisterMessage(helloTestReply)

TestClientRecvStreamRequest = _reflection.GeneratedProtocolMessageType('TestClientRecvStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTRECVSTREAMREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientRecvStreamRequest)
  })
_sym_db.RegisterMessage(TestClientRecvStreamRequest)

TestClientRecvStreamResponse = _reflection.GeneratedProtocolMessageType('TestClientRecvStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTRECVSTREAMRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientRecvStreamResponse)
  })
_sym_db.RegisterMessage(TestClientRecvStreamResponse)

TestClientSendStreamRequest = _reflection.GeneratedProtocolMessageType('TestClientSendStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTSENDSTREAMREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientSendStreamRequest)
  })
_sym_db.RegisterMessage(TestClientSendStreamRequest)

TestClientSendStreamResponse = _reflection.GeneratedProtocolMessageType('TestClientSendStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTSENDSTREAMRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientSendStreamResponse)
  })
_sym_db.RegisterMessage(TestClientSendStreamResponse)

TestTwoWayStreamRequest = _reflection.GeneratedProtocolMessageType('TestTwoWayStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTTWOWAYSTREAMREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.TestTwoWayStreamRequest)
  })
_sym_db.RegisterMessage(TestTwoWayStreamRequest)

TestTwoWayStreamResponse = _reflection.GeneratedProtocolMessageType('TestTwoWayStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTTWOWAYSTREAMRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:test.TestTwoWayStreamResponse)
  })
_sym_db.RegisterMessage(TestTwoWayStreamResponse)


_HELLOTESTREQUEST_NUMBERENTRY._options = None

_HELLO = _descriptor.ServiceDescriptor(
  name='hello',
  full_name='test.hello',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=685,
  serialized_end=1104,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloWorld',
    full_name='test.hello.HelloWorld',
    index=0,
    containing_service=None,
    input_type=_HELLOWORLDREQ,
    output_type=_HELLOWORLDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='helloTest',
    full_name='test.hello.helloTest',
    index=1,
    containing_service=None,
    input_type=_HELLOTESTREQUEST,
    output_type=_HELLOTESTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestClientRecvStream',
    full_name='test.hello.TestClientRecvStream',
    index=2,
    containing_service=None,
    input_type=_TESTCLIENTRECVSTREAMREQUEST,
    output_type=_TESTCLIENTRECVSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestClientSendStream',
    full_name='test.hello.TestClientSendStream',
    index=3,
    containing_service=None,
    input_type=_TESTCLIENTSENDSTREAMREQUEST,
    output_type=_TESTCLIENTSENDSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestTwoWayStream',
    full_name='test.hello.TestTwoWayStream',
    index=4,
    containing_service=None,
    input_type=_TESTTWOWAYSTREAMREQUEST,
    output_type=_TESTTWOWAYSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLO)

DESCRIPTOR.services_by_name['hello'] = _HELLO

# @@protoc_insertion_point(module_scope)
