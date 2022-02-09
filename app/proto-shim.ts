// adapted from https://github.com/grpc/grpc/blob/v1.43.0/examples/node/dynamic_codegen/route_guide/route_guide_client.js

import { get } from 'lodash';
import * as grpc from '@grpc/grpc-js';
import * as  protoLoader from '@grpc/proto-loader';

// Suggested options for similarity to existing grpc.load behavior
const PROTO_PATH = __dirname + '/../proto/app.proto';
const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

// The protoDescriptor object has the full package hierarchy
const defs = grpc.loadPackageDefinition(packageDefinition);
const PySidecar = get(defs, 'PySidecar') as grpc.ServiceClientConstructor;

const sidecarRoute = process.env.SIDECAR || 'localhost:9126';
console.log('Connecting to GRPC sidecar at ', sidecarRoute);

export const client = new PySidecar(
  sidecarRoute,
  grpc.credentials.createInsecure()
);
