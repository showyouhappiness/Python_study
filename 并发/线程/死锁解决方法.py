# https://blog.csdn.net/u013210620/article/details/78723704
from threading import Thread, RLock
import time

mutexA = mutexB = RLock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到A锁' % self.name)

        mutexB.acquire()
        print('%s 拿到B锁' % self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到B锁' % self.name)
        time.sleep(0.1)
        mutexA.acquire()
        print('%s 拿到A锁' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
