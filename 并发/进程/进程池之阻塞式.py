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
    print(n)


if __name__ == '__main__':
    pool = pool.Pool(5)

    tasks = ['起床', '洗脸', '洗头', '刷牙', '休整', '穿鞋', '出发']
    for task_detail in tasks:
        pool.apply(task, args=(task_detail,))  # apply()方法用来向进程池提交需要执行的函数和参数，它会阻塞等待子进程的执行结果
    pool.close()  # 添加任务结束,不能再添加任务了
    pool.join()  # 会等待所有子进程执行完毕
    print('开始新一天搬砖')
