import typing as t

from google.protobuf.json_format import MessageToJson
import grpc

import app_pb2
from app_pb2_grpc import PySidecarStub

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:9126') as channel:
        stub = PySidecarStub(channel)

        nested_input = [
            {
                "value": 100,
                "label": "foo",
            },
            {
                "value": 101,
                "label": "bar",

            },
            {
                "value": 102,
                "label": "baz",
            },
        ]

        print('nested sum input', nested_input)

        input_data = []
        for input_value in nested_input:
            d = app_pb2.Data(
                value=input_value["value"],
                label=input_value["label"],
            )
            input_data.append(d)
        input_data = app_pb2.NestedInput(input=input_data)
        output = stub.SumInputNested(input_data)

        print('sum result', MessageToJson(output))
