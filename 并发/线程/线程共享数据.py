import threading

money = 1000


def run1():
    global money
    for i in range(400):
        money -= 1


def run2():
    global money
    for i in range(400):
        money -= 1


if __name__ == '__main__':
    th1 = threading.Thread(target=run1)  # 方法的功能一样的话，可以使用同一个方法
    th1.start()
    th2 = threading.Thread(target=run2)
    th2.start()
    th1.join()
    th2.join()
    print(money)
