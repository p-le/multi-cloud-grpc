BASE_PATH := $(shell pwd)
GRPC_GENERATOR_IMAGE_TAG := 1.0.0

.PHONY: grpc-generate-pb2
grpc-generate-pb2:
	docker container run \
		-v $(BASE_PATH)/helloworld/protos:/protos \
		-v $(BASE_PATH)/helloworld/generated_pb2:/generated_pb2 \
		grpc-generator:$(GRPC_GENERATOR_IMAGE_TAG) helloworld.proto

.PHONY: grpc-generator-image
grpc-generator-image:
	docker image build -t grpc-generator:$(GRPC_GENERATOR_IMAGE_TAG) .
