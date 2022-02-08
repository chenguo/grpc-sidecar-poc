# example derived from https://github.com/grpc/grpc/tree/v1.43.0/examples/python/route_guide
import asyncio
import grpc
import os

import app_pb2
import app_pb2_grpc
import py_package

default_port = 9126

def get_port() -> int:
    try:
        port = int(os.getenv('PORT'))
        return port
    except:
        return default_port

class AppServicer(app_pb2_grpc.PySidecarServicer):

    def SumInput(
            self,
            input_data: app_pb2.InputData,
            unused_context) -> app_pb2.OutputData:

        print('sum input request', input_data.values)
        result = py_package.sum_inputs(input_data.values)
        output_data = app_pb2.OutputData(result=result)
        return output_data


async def serve() -> None:
    server = grpc.aio.server()
    app_pb2_grpc.add_PySidecarServicer_to_server(
        AppServicer(),
        server)

    port = get_port()
    server.add_insecure_port(f'[::]:{str(port)}')
    await server.start()

    print('GRPC listening on port', port)

    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(serve())
