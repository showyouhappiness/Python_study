"""
递归锁是同步锁的一个升级版本，在同步锁的基础上可以做到连续重复使用多次acquire()后再重复使用多次release()的操作，但是一定要注意加锁次数和解锁次数必须一致，否则也将引发死锁现象。
方法	                                                                        描述
threading.RLock()	                                                    返回一个递归锁对象
lockObject.acquire(blocking=True, timeout=1)	上锁，当一个线程在执行被上锁代码块时，将不允许切换到其他线程运行，默认锁失效时间为1秒
lockObject.release()	                        解锁，当一个线程在执行未被上锁代码块时，将允许系统根据策略自行切换到其他线程中运行
lockObject.locaked()	                                        判断该锁对象是否处于上锁状态，返回一个布尔值

"""
import threading

num = 0


def add():
    lock.acquire()
    lock.acquire()
    global num
    for i in range(10_000_000):
        num += 1
    lock.release()
    lock.release()


def sub():
    lock.acquire()
    lock.acquire()
    global num
    for i in range(10_000_000):
        num -= 1
    lock.release()
    lock.release()


if __name__ == "__main__":
    lock = threading.RLock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)


'''
with语句

由于threading.RLock()对象中实现了__enter__()与__exit__()方法，故我们可以使用with语句进行上下文管理形式的加锁解锁操作：

import threading

num = 0


def add():
    with lock:
        # 自动加锁
        global num
        for i in range(10_000_000):
            num += 1
        # 自动解锁


def sub():
    with lock:
        # 自动加锁
        global num
        for i in range(10_000_000):
            num -= 1
        # 自动解锁


if __name__ == "__main__":
    lock = threading.RLock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)
'''