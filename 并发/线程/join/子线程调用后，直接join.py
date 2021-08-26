import threading
import time


def test(p):
    time.sleep(0.001)
    print(p)


ts = []

for i in [1, 2, 3, 4, 5, 6]:
    # target指定线程要执行的代码，args指定该代码的参数
    th = threading.Thread(target=test, args=[i])
    ts.append(th)

for i in ts:
    i.start()
    # 此处的join函数子线程按顺序执行，即i线程跑完后才能继续跑下一个线程
    i.join()

print("it is end !")
