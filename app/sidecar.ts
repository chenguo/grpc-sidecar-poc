// import { client } from './proto-shim';

import * as grpc from "@grpc/grpc-js";
import {
  Data,
  InputData,
  OutputData,
  NestedInput,
  NestedOutput,
  AddThingsClient,
} from "./gen/add-things";

const sidecarRoute = process.env.SIDECAR || "localhost:9126";
console.log("Connecting to GRPC sidecar at ", sidecarRoute);
const client = new AddThingsClient(
  sidecarRoute,
  grpc.credentials.createInsecure()
);

export async function sidecarSum(x: number, y: number): Promise<OutputData> {
  const input = new InputData({ values: [x, y] });
  return await client.SumInput(input);
}

export async function sidecarSumNested(
  x: number,
  y: number
): Promise<NestedOutput> {
  const input = new NestedInput({
    input: [
      new Data({
        value: x,
        label: "x",
      }),
      new Data({
        value: y,
        label: "y",
      }),
    ],
  });

  return client.SumInputNested(input);
}
