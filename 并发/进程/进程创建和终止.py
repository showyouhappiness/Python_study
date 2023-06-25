import os
from multiprocessing import Process
from time import sleep


def task(s, name):
    while True:
        sleep(s)
        print('获取{}的pid——>{},主线程的pid——>{}'.format(name, os.getpid(), os.getppid()))


def task2(s, name):
    while True:
        sleep(s)
        print('获取{}的pid——>{},主线程的pid——>{}'.format(name, os.getpid(), os.getppid()))


number = 0
if __name__ == '__main__':
    print('这是主线程的开始')
    p = Process(target=task, name='task', args=(1, 'task'))
    p.start()
    print(p.name)
    p2 = Process(target=task, name='task2', args=(2, 'task2'))
    p2.start()
    print(p2.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p.terminate()  # 终止进程
            p2.terminate()  # 终止进程
            break
        else:
            print('number——>{}'.format(number))
    print('这是主线程的结尾')
