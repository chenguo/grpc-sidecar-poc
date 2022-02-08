import grpc
import typing as t

import app_pb2
from app_pb2_grpc import PySidecarStub

def run_sum(stub: PySidecarStub, nums: t.List[int]) -> int:
    print('sum input', nums)
    input_data = app_pb2.InputData(values=nums)
    output = stub.SumInput(input_data)
    return output.result

def run_nested_sum(stub: PySidecarStub, nested_input: t.List[t.Dict]) -> int:
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
    return output.output.value


def run():
    with grpc.insecure_channel('localhost:9126') as channel:
        stub = PySidecarStub(channel)

        sum_result = run_sum(stub, [5, 60, 100])
        print('sum result', sum_result)

        nested_sum_result = run_nested_sum(stub, [
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
        ])

        print('nested sum result', nested_sum_result)

if __name__ == '__main__':
    run()
