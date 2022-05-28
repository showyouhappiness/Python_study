import threading
import time


def test(p):
    time.sleep(0.001)
    print(p)


ts = []

for i in range(150):
    # target指定线程要执行的代码，args指定该代码的参数
    th = threading.Thread(target=test, args=[i])
    ts.append(th)

for i in ts:
    i.start()

# 此处的join函数使子线程全部跑完再继续往下跑子线程
for i in ts:
    i.join()

print("it is end !")
