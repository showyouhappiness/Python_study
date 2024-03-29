# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class helloStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloWorld = channel.unary_unary(
                '/test.hello/HelloWorld',
                request_serializer=helloworld__pb2.HelloWorldReq.SerializeToString,
                response_deserializer=helloworld__pb2.HelloWorldReply.FromString,
                )
        self.helloTest = channel.stream_stream(
                '/test.hello/helloTest',
                request_serializer=helloworld__pb2.helloTestRequest.SerializeToString,
                response_deserializer=helloworld__pb2.helloTestReply.FromString,
                )
        self.TestClientRecvStream = channel.unary_stream(
                '/test.hello/TestClientRecvStream',
                request_serializer=helloworld__pb2.TestClientRecvStreamRequest.SerializeToString,
                response_deserializer=helloworld__pb2.TestClientRecvStreamResponse.FromString,
                )
        self.TestClientSendStream = channel.stream_unary(
                '/test.hello/TestClientSendStream',
                request_serializer=helloworld__pb2.TestClientSendStreamRequest.SerializeToString,
                response_deserializer=helloworld__pb2.TestClientSendStreamResponse.FromString,
                )
        self.TestTwoWayStream = channel.stream_stream(
                '/test.hello/TestTwoWayStream',
                request_serializer=helloworld__pb2.TestTwoWayStreamRequest.SerializeToString,
                response_deserializer=helloworld__pb2.TestTwoWayStreamResponse.FromString,
                )


class helloServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloWorld(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def helloTest(self, request_iterator, context):
        """可以将传入和传出的写成流的形式
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestClientRecvStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestClientSendStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestTwoWayStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_helloServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloWorld': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloWorld,
                    request_deserializer=helloworld__pb2.HelloWorldReq.FromString,
                    response_serializer=helloworld__pb2.HelloWorldReply.SerializeToString,
            ),
            'helloTest': grpc.stream_stream_rpc_method_handler(
                    servicer.helloTest,
                    request_deserializer=helloworld__pb2.helloTestRequest.FromString,
                    response_serializer=helloworld__pb2.helloTestReply.SerializeToString,
            ),
            'TestClientRecvStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TestClientRecvStream,
                    request_deserializer=helloworld__pb2.TestClientRecvStreamRequest.FromString,
                    response_serializer=helloworld__pb2.TestClientRecvStreamResponse.SerializeToString,
            ),
            'TestClientSendStream': grpc.stream_unary_rpc_method_handler(
                    servicer.TestClientSendStream,
                    request_deserializer=helloworld__pb2.TestClientSendStreamRequest.FromString,
                    response_serializer=helloworld__pb2.TestClientSendStreamResponse.SerializeToString,
            ),
            'TestTwoWayStream': grpc.stream_stream_rpc_method_handler(
                    servicer.TestTwoWayStream,
                    request_deserializer=helloworld__pb2.TestTwoWayStreamRequest.FromString,
                    response_serializer=helloworld__pb2.TestTwoWayStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.hello', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class hello(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloWorld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.hello/HelloWorld',
            helloworld__pb2.HelloWorldReq.SerializeToString,
            helloworld__pb2.HelloWorldReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def helloTest(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/test.hello/helloTest',
            helloworld__pb2.helloTestRequest.SerializeToString,
            helloworld__pb2.helloTestReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestClientRecvStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/test.hello/TestClientRecvStream',
            helloworld__pb2.TestClientRecvStreamRequest.SerializeToString,
            helloworld__pb2.TestClientRecvStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestClientSendStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/test.hello/TestClientSendStream',
            helloworld__pb2.TestClientSendStreamRequest.SerializeToString,
            helloworld__pb2.TestClientSendStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestTwoWayStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/test.hello/TestTwoWayStream',
            helloworld__pb2.TestTwoWayStreamRequest.SerializeToString,
            helloworld__pb2.TestTwoWayStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
