import os
from multiprocessing import Process
from time import sleep


def task():
    while True:
        sleep(1)
        print('获取task的pid——>{}'.format(os.getpid()))


def task2():
    while True:
        sleep(2)
        print('获取task2的pid——>{}'.format(os.getpid()))


if __name__ == '__main__':
    print('这是主进程的开始')
    p = Process(target=task, name='task')
    p.start()
    print(p.name)
    p2 = Process(target=task2, name='task2')
    p2.start()
    print(p2.name)
    print('这是主进程的结尾')
