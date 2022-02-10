import typing as t

from google.protobuf.json_format import MessageToJson
import grpc

from add_things_pb2 import Data, NestedInput
from add_things_pb2_grpc import AddThingsStub

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:9126') as channel:
        stub = AddThingsStub(channel)

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
            d = Data(
                value=input_value["value"],
                label=input_value["label"],
            )
            input_data.append(d)
        input_data = NestedInput(input=input_data)
        output = stub.SumInputNested(input_data)

        print('sum result', MessageToJson(output))
