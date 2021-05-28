BASE_PATH := $(shell pwd)
GRPC_GENERATOR_IMAGE_TAG := 1.0.0

.PHONY: grpc-generate-pb2-helloworld
grpc-generate-pb2-helloworld:
	docker container run \
		--rm -it \
		-v $(BASE_PATH)/helloworld/protos/helloworld.proto:/protos/helloworld.proto \
		-v $(BASE_PATH)/helloworld/generated_pb2:/generated_pb2 \
		grpc-generator:$(GRPC_GENERATOR_IMAGE_TAG) helloworld.proto

.PHONY: grpc-generate-pb2-bookstore
grpc-generate-pb2-bookstore:
	docker container run \
		--rm -it \
		-v $(BASE_PATH)/bookstore/protos/bookstore.proto:/protos/bookstore.proto \
		-v $(BASE_PATH)/bookstore/generated_pb2:/generated_pb2 \
		grpc-generator:$(GRPC_GENERATOR_IMAGE_TAG) bookstore.proto

.PHONY: grpc-generate-pb2-viet-soccer
grpc-generate-pb2-viet-soccer:
	docker container run \
		--rm -it \
		-v $(BASE_PATH)/viet-soccer/protos/credential.proto:/protos/credential.proto \
		-v $(BASE_PATH)/viet-soccer/generated_pb2:/generated_pb2 \
		grpc-generator:$(GRPC_GENERATOR_IMAGE_TAG) credential.proto

.PHONY: grpc-generator-image
grpc-generator-image:
	docker image build -t grpc-generator:$(GRPC_GENERATOR_IMAGE_TAG) .
