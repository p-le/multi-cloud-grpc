FROM python:3.8-slim

WORKDIR /protos

COPY google ./google

RUN pip install --no-cache-dir grpcio-tools==1.37.1

ENTRYPOINT [ \
    "python", \
    "-m", \
    "grpc_tools.protoc", \
    "--include_imports", \
    "--include_source_info", \
    "--proto_path=.", \
    "--descriptor_set_out=/generated_pb2/api_descriptor.pb", \
    "--python_out=/generated_pb2", \
    "--grpc_python_out=/generated_pb2" \
]
