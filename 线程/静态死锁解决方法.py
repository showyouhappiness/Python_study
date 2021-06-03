# coding=utf-8
# https://www.cnblogs.com/-wenli/p/12983835.html
import time
import threading


class Account:
    def __init__(self, _id, balance):
        self.id = _id
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def transfera_b(_from, to, amount):
    lock_a.acquire()  # 锁住自己的账户
    time.sleep(1)  # 让交易时间变长，2个交易线程时间上重叠，有足够时间来产生死锁
    _from.withdraw(amount)
    lock_b.acquire()  # 锁住对方的账户
    to.deposit(amount)
    lock_b.release()
    lock_a.release()


def transferb_a(_from, to, amount):
    lock_a.acquire()  # 锁住自己的账户
    time.sleep(1)  # 让交易时间变长，2个交易线程时间上重叠，有足够时间来产生死锁
    _from.withdraw(amount)
    lock_b.acquire()  # 锁住对方的账户
    to.deposit(amount)
    lock_b.release()
    lock_a.release()


lock_a = threading.Lock()
lock_b = threading.Lock()
a = Account('a', 1000)
b = Account('b', 1000)
# a往b转账100
t1 = threading.Thread(target=transfera_b, args=(a, b, 100))
t1.start()
# b往a转账200
t2 = threading.Thread(target=transferb_a, args=(b, a, 200))
t2.start()
t1.join()
t2.join()
print("a的账户余额：", a.balance)
print("b的账户余额：", b.balance)
