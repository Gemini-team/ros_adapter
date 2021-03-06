# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: navigation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='navigation.proto',
  package='navigation',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.navigationB\nNavigationP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10navigation.proto\x12\nnavigation\"\'\n\x04Vec3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"\xcc\x01\n\x11NavigationRequest\x12\x11\n\ttimeStamp\x18\x01 \x01(\x01\x12\"\n\x08position\x18\x02 \x01(\x0b\x32\x10.navigation.Vec3\x12+\n\x0borientation\x18\x03 \x01(\x0b\x32\x16.navigation.Quaternion\x12(\n\x0elinearVelocity\x18\x04 \x01(\x0b\x32\x10.navigation.Vec3\x12)\n\x0f\x61ngularVelocity\x18\x05 \x01(\x0b\x32\x10.navigation.Vec3\"%\n\x12NavigationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x66\n\nNavigation\x12X\n\x15SendNavigationMessage\x12\x1d.navigation.NavigationRequest\x1a\x1e.navigation.NavigationResponse\"\x00\x42\x31\n\x1bio.grpc.examples.navigationB\nNavigationP\x01\xa2\x02\x03HLWb\x06proto3'
)




_VEC3 = _descriptor.Descriptor(
  name='Vec3',
  full_name='navigation.Vec3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='navigation.Vec3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='navigation.Vec3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='navigation.Vec3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=32,
  serialized_end=71,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='navigation.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='navigation.Quaternion.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='navigation.Quaternion.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='navigation.Quaternion.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='navigation.Quaternion.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=73,
  serialized_end=129,
)


_NAVIGATIONREQUEST = _descriptor.Descriptor(
  name='NavigationRequest',
  full_name='navigation.NavigationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='navigation.NavigationRequest.timeStamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='navigation.NavigationRequest.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='navigation.NavigationRequest.orientation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='linearVelocity', full_name='navigation.NavigationRequest.linearVelocity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angularVelocity', full_name='navigation.NavigationRequest.angularVelocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=336,
)


_NAVIGATIONRESPONSE = _descriptor.Descriptor(
  name='NavigationResponse',
  full_name='navigation.NavigationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='navigation.NavigationResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=338,
  serialized_end=375,
)

_NAVIGATIONREQUEST.fields_by_name['position'].message_type = _VEC3
_NAVIGATIONREQUEST.fields_by_name['orientation'].message_type = _QUATERNION
_NAVIGATIONREQUEST.fields_by_name['linearVelocity'].message_type = _VEC3
_NAVIGATIONREQUEST.fields_by_name['angularVelocity'].message_type = _VEC3
DESCRIPTOR.message_types_by_name['Vec3'] = _VEC3
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['NavigationRequest'] = _NAVIGATIONREQUEST
DESCRIPTOR.message_types_by_name['NavigationResponse'] = _NAVIGATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vec3 = _reflection.GeneratedProtocolMessageType('Vec3', (_message.Message,), {
  'DESCRIPTOR' : _VEC3,
  '__module__' : 'navigation_pb2'
  # @@protoc_insertion_point(class_scope:navigation.Vec3)
  })
_sym_db.RegisterMessage(Vec3)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {
  'DESCRIPTOR' : _QUATERNION,
  '__module__' : 'navigation_pb2'
  # @@protoc_insertion_point(class_scope:navigation.Quaternion)
  })
_sym_db.RegisterMessage(Quaternion)

NavigationRequest = _reflection.GeneratedProtocolMessageType('NavigationRequest', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONREQUEST,
  '__module__' : 'navigation_pb2'
  # @@protoc_insertion_point(class_scope:navigation.NavigationRequest)
  })
_sym_db.RegisterMessage(NavigationRequest)

NavigationResponse = _reflection.GeneratedProtocolMessageType('NavigationResponse', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATIONRESPONSE,
  '__module__' : 'navigation_pb2'
  # @@protoc_insertion_point(class_scope:navigation.NavigationResponse)
  })
_sym_db.RegisterMessage(NavigationResponse)


DESCRIPTOR._options = None

_NAVIGATION = _descriptor.ServiceDescriptor(
  name='Navigation',
  full_name='navigation.Navigation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=377,
  serialized_end=479,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendNavigationMessage',
    full_name='navigation.Navigation.SendNavigationMessage',
    index=0,
    containing_service=None,
    input_type=_NAVIGATIONREQUEST,
    output_type=_NAVIGATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NAVIGATION)

DESCRIPTOR.services_by_name['Navigation'] = _NAVIGATION

# @@protoc_insertion_point(module_scope)
