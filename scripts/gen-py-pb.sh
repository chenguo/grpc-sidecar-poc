#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROTO_DIR=$1

if [ -z "$PROTO_DIR" ]; then
    PROTO_DIR=$DIR/../proto
fi

cd $DIR
python -m grpc_tools.protoc \
       -I$PROTO_DIR \
       --python_out=$DIR/../py-sidecar/app \
       --grpc_python_out=$DIR/../py-sidecar/app \
       $PROTO_DIR/add-things.proto

