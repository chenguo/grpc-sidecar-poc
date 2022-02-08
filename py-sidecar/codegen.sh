#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

(
    cd $DIR
    # rm -rf app/proto
    # mkdir -p app/proto
    # touch app/proto/__init__.py
    python -m grpc_tools.protoc \
           -I../proto \
           --python_out=./app \
           --grpc_python_out=./app \
           ../proto/app.proto
)
