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
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))

        # 服务器(流)
        # response = client.TestClientRecvStream(helloworld_pb2.TestClientRecvStreamRequest(
        #     data='liyongjun'
        # ))
        # for item in response:
        #     print(item.result)
        #     print("Greeter client received: " + response.message)

        # 客户端(流)
        # response = client.TestClientSendStream(test())
        # print(response.result)

        # 双向流
        response = client.TestTwoWayStream(test(), timeout=10)
        for res in response:
            print(res.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()
