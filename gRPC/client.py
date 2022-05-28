"""
https://github.com/grpc/grpc/tree/master/examples/python/helloworld
The Python implementation of the GRPC helloworld.Greeter client.
"""

from __future__ import print_function

import logging
import random
import time

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


# 客户端（流）
def test():
    index = 0
    while True:
        time.sleep(1)
        data = str(random.Random())
        if index == 5:
            break
        print(index)
        index += 1
        yield helloworld_pb2.TestClientSendStreamRequest(data=data)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.helloStub(channel)
        # # response = stub.HelloWorld(helloworld_pb2.HelloWorldReq(name='you'))
        # # print("Greeter client received: " + response)
        # try:
        #     response, call = stub.HelloWorld.with_call(helloworld_pb2.HelloWorldReq(
        #         name='you'
        #     ),
        #         # 客户端压缩
        #         compression=grpc.Compression.Gzip,
        #         metadata=(('client_key', 'client_value'),),
        #         wait_for_ready=True
        #     )
        #     print("client received: " + response.result)
        #     header = call.trailing_metadata
        #     print(header)
        #     print(header[0].key, header[0].value)
        # except Exception as e:
        #     # print(e.code())
        #     print(e.code().name, e.code().value)
        #     print(e.details())
        #     # print(e)

        # 服务器(流)
        # response = stub.TestClientRecvStream(helloworld_pb2.TestClientRecvStreamRequest(
        #     data='liyongjun'
        # ))
        # for item in response:
        #     print(item.result)

        # 客户端(流)
        # response = stub.TestClientSendStream(test())
        # print(response.result)

        # 双向流
        response = stub.TestTwoWayStream(test(), timeout=10)
        for res in response:
            print(res.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()
