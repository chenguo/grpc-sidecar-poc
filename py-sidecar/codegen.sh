#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

(
    cd $DIR
    mkdir -p app/proto
    python -m grpc_tools.protoc \
           -I../proto \
           --python_out=./app/proto \
           --grpc_python_out=./app/proto \
           ../proto/app.proto
)
