import typing as t

from google.protobuf.json_format import MessageToJson
import grpc

import app_pb2
from app_pb2_grpc import PySidecarStub

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:9126') as channel:
        stub = PySidecarStub(channel)

        input_nums = [5, 60, 100]
        print('sum input', input_nums)
        input_data = app_pb2.InputData(values=input_nums)
        output = stub.SumInput(input_data)

        print('sum result', MessageToJson(output))
