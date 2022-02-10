// import { client } from './proto-shim';

import * as grpc from '@grpc/grpc-js';
import { InputData, OutputData, NestedInput, NestedOutput, PySidecarClient } from './gen/app';

const sidecarRoute = process.env.SIDECAR || 'localhost:9126';
console.log('Connecting to GRPC sidecar at ', sidecarRoute);
const client = new PySidecarClient(
  sidecarRoute,
  grpc.credentials.createInsecure()
);

export async function sidecarSum(x: number, y: number): Promise<OutputData> {
  const input = new InputData({ values: [x, y] });
  return await client.SumInput(input);
}

export async function sidecarSumNested(x: number, y: number): Promise<NestedOutput> {
  const input = new NestedInput({
    input: [{
      value: x,
      label: 'x',
    }, {
      value: y,
      label: 'y',
    }]
  });

  return client.SumInputNested(input);
}
