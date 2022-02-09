#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

(
    cd $DIR
    python -m grpc_tools.protoc \
           -I./proto \
           --python_out=./app \
           --grpc_python_out=./app \
           ./proto/app.proto
)
