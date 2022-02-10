#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
APP_DIR=$DIR/../py-sidecar

cd $DIR
python -m grpc_tools.protoc \
       -I$APP_DIR/proto \
       --python_out=$APP_DIR/app \
       --grpc_python_out=$APP_DIR/app \
       $APP_DIR/proto/add-things.proto
