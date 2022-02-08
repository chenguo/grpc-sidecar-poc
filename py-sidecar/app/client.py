import grpc
import typing as t

import app_pb2
from app_pb2_grpc import PySidecarStub

def run_sum(stub: PySidecarStub, nums: t.List[int]) -> int:
    print('nums', nums)
    input_data = app_pb2.InputData(values=nums)
    output = stub.SumInput(input_data)
    return output.result


def run():
    with grpc.insecure_channel('localhost:9126') as channel:
        stub = PySidecarStub(channel)

        sum_result = run_sum(stub, [5, 60, 100])
        print('sum result', sum_result)

if __name__ == '__main__':
    run()
