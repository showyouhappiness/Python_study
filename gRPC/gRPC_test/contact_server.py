import logging
import random
import time
from concurrent import futures

import grpc
import contact_pb2_grpc
import contact_pb2


# 在类初试化的时候定义了一个列表self.tasks来充当任务队列
def getTask(self, request_iterator, context):
    print("服务端已接收到客户端上线通知，开始发送任务给客户端\n")
    last_index = 0
    while True:
        print("服务端开始发送任务给客户端了。。。。。。\n")
        while len(self.tasks) > last_index:
            n = self.tasks[last_index]
            last_index += 1
            yield n
            print(f'服务端发送给了客户端任务：{n.task}##########\n')

        # 顺便制造些服务端的任务数据用来填充到任务队列里面
        for i in range(10):
            num = random.randint(100, 200)
            self.tasks.append(contact_pb2.ServerMsg(
                task=f"任务:{num}"
            ))
        time.sleep(40)

        # 注意服务端的具体实现函数是在类里面
        def sendStatus(self, request_iterator, context):
            for note in request_iterator:
                yield contact_pb2.Result(
                    result=f"服务端接收到消息:{note.msg}"
                )


def tellResult(self, request_iterator, context):
    for response in request_iterator:
        print(f"我已经知道客户端接收到我发过去的任务:{response.ret}")

    return contact_pb2.Empty()


if __name__ == '__main__':
    logging.basicConfig()
    tellResult()