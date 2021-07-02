import os
import time
from multiprocessing import Process, pool
from random import random


def task(task_name):
    print('开始任务：{}'.format(task_name))
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    n = '完成任务：{}！用时：{}，进程id：{}'.format(task_name, (end - start), os.getpid())
    return n


def callback_func(n):
    container.append(n)


container = []
if __name__ == '__main__':
    pool = pool.Pool(5)

    tasks = ['起床', '洗脸', '洗头', '刷牙', '休整', '穿鞋', '出发']
    for task_detail in tasks:
        pool.apply_async(task, args=(task_detail,), callback=callback_func)
    pool.close()  # 添加任务结束,不能再添加任务了
    pool.join()  # 让主进程等待所有子进程执行完毕（让主进程让步）
    for c in container:
        print(c)
    print('开始新一天搬砖')
