# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: credential.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='credential.proto',
  package='vietsoccer.firestore.api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63redential.proto\x12\x18vietsoccer.firestore.api\x1a\x1cgoogle/api/annotations.proto\"\x80\x01\n\x0b\x43redentials\x12\r\n\x05token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x11\n\ttoken_uri\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\x15\n\rclient_secret\x18\x05 \x01(\t\x12\x0e\n\x06scopes\x18\x06 \x03(\t\"\x15\n\x06\x44omain\x12\x0b\n\x03uri\x18\x01 \x01(\t\"*\n\x17SaveCredentialsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x93\x02\n\x10OauthCredentials\x12r\n\x0eGetCredentials\x12 .vietsoccer.firestore.api.Domain\x1a%.vietsoccer.firestore.api.Credentials\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/credentials\x12\x8a\x01\n\x0fSaveCredentials\x12%.vietsoccer.firestore.api.Credentials\x1a\x31.vietsoccer.firestore.api.SaveCredentialsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x0f/v1/credentials:\x04\x64\x61tab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CREDENTIALS = _descriptor.Descriptor(
  name='Credentials',
  full_name='vietsoccer.firestore.api.Credentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='vietsoccer.firestore.api.Credentials.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='refresh_token', full_name='vietsoccer.firestore.api.Credentials.refresh_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_uri', full_name='vietsoccer.firestore.api.Credentials.token_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='vietsoccer.firestore.api.Credentials.client_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_secret', full_name='vietsoccer.firestore.api.Credentials.client_secret', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='vietsoccer.firestore.api.Credentials.scopes', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=77,
  serialized_end=205,
)


_DOMAIN = _descriptor.Descriptor(
  name='Domain',
  full_name='vietsoccer.firestore.api.Domain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='vietsoccer.firestore.api.Domain.uri', index=0,
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
  serialized_start=207,
  serialized_end=228,
)


_SAVECREDENTIALSRESPONSE = _descriptor.Descriptor(
  name='SaveCredentialsResponse',
  full_name='vietsoccer.firestore.api.SaveCredentialsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='vietsoccer.firestore.api.SaveCredentialsResponse.success', index=0,
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
  serialized_start=230,
  serialized_end=272,
)

DESCRIPTOR.message_types_by_name['Credentials'] = _CREDENTIALS
DESCRIPTOR.message_types_by_name['Domain'] = _DOMAIN
DESCRIPTOR.message_types_by_name['SaveCredentialsResponse'] = _SAVECREDENTIALSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'credential_pb2'
  # @@protoc_insertion_point(class_scope:vietsoccer.firestore.api.Credentials)
  })
_sym_db.RegisterMessage(Credentials)

Domain = _reflection.GeneratedProtocolMessageType('Domain', (_message.Message,), {
  'DESCRIPTOR' : _DOMAIN,
  '__module__' : 'credential_pb2'
  # @@protoc_insertion_point(class_scope:vietsoccer.firestore.api.Domain)
  })
_sym_db.RegisterMessage(Domain)

SaveCredentialsResponse = _reflection.GeneratedProtocolMessageType('SaveCredentialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVECREDENTIALSRESPONSE,
  '__module__' : 'credential_pb2'
  # @@protoc_insertion_point(class_scope:vietsoccer.firestore.api.SaveCredentialsResponse)
  })
_sym_db.RegisterMessage(SaveCredentialsResponse)



_OAUTHCREDENTIALS = _descriptor.ServiceDescriptor(
  name='OauthCredentials',
  full_name='vietsoccer.firestore.api.OauthCredentials',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=275,
  serialized_end=550,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCredentials',
    full_name='vietsoccer.firestore.api.OauthCredentials.GetCredentials',
    index=0,
    containing_service=None,
    input_type=_DOMAIN,
    output_type=_CREDENTIALS,
    serialized_options=b'\202\323\344\223\002\021\022\017/v1/credentials',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SaveCredentials',
    full_name='vietsoccer.firestore.api.OauthCredentials.SaveCredentials',
    index=1,
    containing_service=None,
    input_type=_CREDENTIALS,
    output_type=_SAVECREDENTIALSRESPONSE,
    serialized_options=b'\202\323\344\223\002\027\"\017/v1/credentials:\004data',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OAUTHCREDENTIALS)

DESCRIPTOR.services_by_name['OauthCredentials'] = _OAUTHCREDENTIALS

# @@protoc_insertion_point(module_scope)
