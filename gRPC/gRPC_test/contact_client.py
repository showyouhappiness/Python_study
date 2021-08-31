import logging
import random
import threading
import time

import grpc
import contact_pb2
import contact_pb2_grpc


# 接收服务端发送过来的任务
def get_task(stub):
    try:
        for task in stub.getTask(contact_pb2.Empty()):
            print(f"客户端已接收到服务端任务：{task.task}\n")
            # 顺便再告诉服务端我已经接收到你发的任务，你不用担心我没接收到它
            yield contact_pb2.Result(
                ret=f"客户端接收到任务:{task.task}"
            )
    except Exception as e:
        print(f'err:{e}')
        return


# 先制造一些客户端能发送的数据
def make_some_data():
    for i in range(15):
        num = random.randint(1, 20)
        yield contact_pb2.ClientMsg(msg=f"数据:{num}")


def send_status(stub):
    try:
        while True:
            status_response = stub.sendStatus(make_some_data())
            for ret in status_response:
                print(ret.result)
            time.sleep(60)
    except Exception as e:
        print(f'err in send_status:{e}')
        return


# 客户端再通知服务端我接收到你的消息了
def tell_result(stub):
    result = get_task(stub)
    stub.tellResult(result)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = contact_pb2_grpc.ContactStub(channel)
        while True:
            try:
                threading.Thread(target=send_status, args=(stub,), daemon=True).start()
                tell_result(stub)
            except grpc.RpcError as e:
                print(f"server connected out, please retry:{e.code()},{e.details()}")
            except Exception as e:
                print(f'unknown err:{e}')
            finally:
                time.sleep(2)


if __name__ == '__main__':
    run()
