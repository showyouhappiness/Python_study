"""
https://github.com/grpc/grpc/tree/master/examples/python/helloworld
The Python implementation of the GRPC helloworld.Greeter server.
"""
import time
from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)

    # 服务器(流)一直给客户端返回信息
    def TestClientRecvStream(self, request, context):
        index = 0
        while context.is_active():
            data = request.data
            if data == 'close':
                print('data is close, request will cancel')
                context.cancel()
            time.sleep(1)
            index += 1
            result = 'send %d %s' % (index, data)
            print(result)
            yield helloworld_pb2.TestClientRecvStreamResponse(
                result=result
            )

    # 客户端(流)一直给服务器发送信息
    def TestClientSendStream(self, request_iterator, context):
        index = 0
        for request in request_iterator:
            print(request.data, ':', index)
            if index == 10:
                break
            index += 1
        return helloworld_pb2.TestClientSendStreamResponse(
            result='ok'
        )

    # 双向流
    def TestTwoWayStream(self, request_iterator, context):
        index = 0
        for request in request_iterator:
            data = request.data
            if index == 3:
                context.cancel()
            index += 1
            yield helloworld_pb2.TestTwoWayStreamResponse(
                result='service send client %s' % data
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
