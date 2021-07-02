# coding=utf-8
import time
import threading


class Account:
    def __init__(self, _id, balance):
        self.id = _id
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def transfer(_from, to, amount):
    _from.lock.acquire()  # 锁住自己的账户
    time.sleep(1)  # 让交易时间变长，2个交易线程时间上重叠，有足够时间来产生死锁
    _from.withdraw(amount)
    print('wait for lock')
    to.lock.acquire()  # 锁住对方的账户
    to.deposit(amount)
    to.lock.release()
    _from.lock.release()


a = Account('a', 1000)
b = Account('b', 1000)
# a往b转账100
t1 = threading.Thread(target=transfer, args=(a, b, 100))
t1.start()
# b往a转账200
t2 = threading.Thread(target=transfer, args=(b, a, 200))
t2.start()
t1.join()
t2.join()
print("a的账户余额：", a.balance)
print("b的账户余额：", b.balance)
