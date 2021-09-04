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

'''
书写一个拦截器的类
init code detail
grpc_code 错误函数 abort
intercept_service(self,continuation,handler_call_details)
'''


def _abort(code, details):  # unary,stream
    def terminate(ignored_request, context):
        context.abort(code, details)

    return grpc.unary_unary_rpc_method_handler(terminate())


class TestInterceptor(grpc.ServerInterceptor):
    def __init__(self, key, value, code, detail):
        self.key = key
        self.value = value
        self._abort = _abort(code, detail)

    def intercept_service(self, continuation, handler_call_details):
        # continuation 函数执行器
        # handler_call_details  header原数据
        headers = dict(handler_call_details.invocation_metadata)
        print(handler_call_details.invocation_metadata)
        print(headers)
        # if (self.key, self.value) not in handler_call_details.invocation_metadata:
        #     return self._abort
        if headers.get(self.key, '') != self.value:
            return self._abort
        return continuation(handler_call_details)


class Greeter(helloworld_pb2_grpc.helloServicer):

    def SayHello(self, request, context):
        name = request.name
        age = request.age
        # 下面三行是自定义报错
        # context.set_details('haha bug')
        # context.set_code(grpc.StatusCode.DATA_LOSS)
        # raise context

        # 添加headers
        context.set_trailing_metadata(('key', 'value'), ('name', 'liyongjun'))
        headers = context.invocation_metadata()
        print(headers)
        print(headers[0].key, headers[0].value)

        # 压缩
        context.set_compression(grpc.Compression.Gzip)  # dir(grpc.Compression)查看都有哪些压缩方式

        result = f'my name is {name},i am{age} years old'
        return helloworld_pb2.HelloWorldReply(result=result)
        # return helloworld_pb2.HelloWorldReply(message='Hello, %s!' % request.name)

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
    validator = TestInterceptor('name', 'liyongjun', grpc.StatusCode.UNAUTHENTICATED, 'AccessDenied')
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        # 整体（所有方法）添加压缩
        compression=grpc.Compression.Gzip,
        options=[
            ('grpc.max_send_message_length', 50 * 1024 * 1024),
            ('grpc.max_receive_message_length', 50 * 1024 * 1024)
        ],
        interceptors=(validator,)
    )
    helloworld_pb2_grpc.add_helloServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
