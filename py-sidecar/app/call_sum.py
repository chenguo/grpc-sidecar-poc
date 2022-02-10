import typing as t

from google.protobuf.json_format import MessageToJson
import grpc

from add_things_pb2 import InputData
from add_things_pb2_grpc import AddThingsStub

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:9126") as channel:
        stub = AddThingsStub(channel)

        input_nums = [5, 60, 100]
        print("sum input", input_nums)
        input_data = InputData(values=input_nums)
        output = stub.SumInput(input_data)

        print("sum result", MessageToJson(output))
