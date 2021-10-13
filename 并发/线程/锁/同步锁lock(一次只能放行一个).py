"""
互斥指的是某一资源同一时刻仅能有一个访问者对其进行访问，具有唯一性和排他性，但是互斥无法限制访问者对资源的访问顺序，即访问是无序的
同步是指在互斥的基础上（大多数情况），通过其他机制实现访问者对资源的有序访问
同步其实已经实现了互斥，是互斥的一种更为复杂的实现，因为它在互斥的基础上实现了有序访问的特点


方法                                                                      	描述
threading.Lock()	                                                    返回一个同步锁对象
lockObject.acquire(blocking=True, timeout=1)	    上锁，当一个线程在执行被上锁代码块时，将不允许切换到其他线程运行，默认锁失效时间为1秒
lockObject.release()	                            解锁，当一个线程在执行未被上锁代码块时，将允许系统根据策略自行切换到其他线程中运行
lockObject.locaked()	                                    判断该锁对象是否处于上锁状态，返回一个布尔值

"""
import threading

num = 0


def add():
    lock.acquire()
    global num
    for i in range(10_000_000):
        num += 1
    lock.release()


def sub():
    lock.acquire()
    global num
    for i in range(10_000_000):
        num -= 1
    lock.release()


if __name__ == "__main__":
    lock = threading.Lock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)

'''
死锁现象

对于同步锁来说，一次acquire()必须对应一次release()，不能出现连续重复使用多次acquire()后再重复使用多次release()的操作，这样会引起死锁造成程序的阻塞，完全不动了，如下所示：

import threading

num = 0


def add():
    lock.acquire()  # 上锁
    lock.acquire()  # 死锁
    # 不执行
    global num
    for i in range(10_000_000):
        num += 1
    lock.release()
    lock.release()


def sub():
    lock.acquire()  # 上锁
    lock.acquire()  # 死锁
    # 不执行
    global num
    for i in range(10_000_000):
        num -= 1
    lock.release()
    lock.release()


if __name__ == "__main__":
    lock = threading.Lock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)
'''

'''
with语句

由于threading.Lock()对象中实现了__enter__()与__exit__()方法，故我们可以使用with语句进行上下文管理形式的加锁解锁操作：
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
    lock = threading.Lock()

    subThread01 = threading.Thread(target=add)
    subThread02 = threading.Thread(target=sub)

    subThread01.start()
    subThread02.start()

    subThread01.join()
    subThread02.join()

    print("num result : %s" % num)

'''
