#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from concurrent import futures

import grpc
import Go_Python_gRPC_pb2_grpc
import Go_Python_gRPC_pb2
from Go_Python_gRPC_pb2_grpc import MyServiceServicer
from service import get_users


class Service(MyServiceServicer):
    def Health(self, request, context):
        return

    def User(self, request, context):
        print('start to process request...')
        res = get_users(request.userIDs)
        users = []
        for u in res:
            users.append(Go_Python_gRPC_pb2.User(name=u['name'], age=u['age'], email=u['email']))
        return Go_Python_gRPC_pb2.UserReply(message='success', data=users)


def serve():
    print('start grpc server====>')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Go_Python_gRPC_pb2_grpc.add_MyServiceServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
