#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROTO_DIR=$DIR/../proto

rm -rf $DIR/../app/gen
mkdir -p $DIR/../app/gen

export PATH=$PATH:$DIR/../node_modules/.bin
protoc \
    --ts_out $DIR/../app/gen \
    --ts_opt generate_dependencies,server_none \
    --ts_opt unary_rpc_promise=true \
    --proto_path $PROTO_DIR \
    $PROTO_DIR/add-things.proto
