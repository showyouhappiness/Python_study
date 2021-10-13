"""

事件锁是基于条件锁来做的，它与条件锁的区别在于一次只能放行全部，不能放行任意个数量的子线程继续运行。

我们可以将事件锁看为红绿灯，当红灯时所有子线程都暂停运行，并进入“等待”状态，当绿灯时所有子线程都恢复“运行”。

方法	                                      描述
threading.Event()	                返回一个事件锁对象
lockObject.clear()	                将事件锁设为红灯状态，即所有线程暂停运行
lockObject.is_set()	                用来判断当前事件锁状态，红灯为False，绿灯为True
lockObject.set()	                将事件锁设为绿灯状态，即所有线程恢复运行
lockObject.wait(timeout=None)	    将当前线程设置为“等待”状态，只有该线程接到“绿灯通知”或者超时时间到期之后才会继续运行，在“等待”状态下的线程将允许系统根据策略自行切换到其他线程中运行

事件锁不能利用with语句来进行使用，只能按照常规方式。
"""

# 模拟线程和红绿灯的操作，红灯停，绿灯行：
import threading

maxSubThreadNumber = 3


def task():
    thName = threading.currentThread().name
    print("start and wait run thread : %s" % thName)
    eventLock.wait()  # 暂停运行，等待绿灯
    print("green light, %s carry on run" % thName)
    print("red light, %s stop run" % thName)
    eventLock.wait()  # 暂停运行，等待绿灯
    print("green light, %s carry on run" % thName)
    print("sub thread %s run end" % thName)


if __name__ == "__main__":

    eventLock = threading.Event()

    for i in range(maxSubThreadNumber):
        subThreadIns = threading.Thread(target=task)
        subThreadIns.start()

    eventLock.set()  # 设置为绿灯
    eventLock.clear()  # 设置为红灯
    eventLock.set()  # 设置为绿灯

# with语句 模拟线程和红绿灯的操作，红灯停，绿灯行：
'''
import threading
import time

maxSubThreadNumber = 6


def task():
    thName = threading.currentThread().name
    with semaLock:
        print("run sub thread %s" % thName)
        time.sleep(3)


if __name__ == "__main__":

    semaLock = threading.Semaphore(2)

    for i in range(maxSubThreadNumber):
        subThreadIns = threading.Thread(target=task)
        subThreadIns.start()
'''

# 事件锁的应用
# 有2个任务线程来扮演李白和杜甫，如何让他们一人一句进行对答？文本如下：
import threading


def libai():
    event.wait()
    print("李白：老杜啊，不喝了我喝不下了！")
    event.set()
    event.clear()
    event.wait()
    print("李白：呼呼呼...睡着了..")


def dufu():
    print("杜甫：老李啊，来喝酒！")
    event.set()
    event.clear()
    event.wait()
    print("杜甫：老李啊，再来一壶？")
    print("杜甫：...老李？")
    event.set()


if __name__ == '__main__':
    event = threading.Event()

    t1 = threading.Thread(target=libai)
    t2 = threading.Thread(target=dufu)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
