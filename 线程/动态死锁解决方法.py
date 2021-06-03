import threading
import hashlib


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
    hasha, hashb = hashlock(_from, to)
    print(hasha, hashb)
    if hasha > hashb:
        _from.lock.acquire()  # 锁住自己的账户
        to.lock.acquire()  # 锁住对方的账户
        # 交易#################
        _from.withdraw(amount)
        to.deposit(amount)
        #################
        to.lock.release()
        _from.lock.release()
    elif hasha < hashb:
        to.lock.acquire()  # 锁住自己的账户
        _from.lock.acquire()  # 锁住对方的账户
        # 交易#################
        _from.withdraw(amount)
        to.deposit(amount)
        #################
        _from.lock.release()
        to.lock.release()
    else:  ##hash值相等，最上层使用mylock锁，你可以把transfer做成一个类，此类中实例一个mylock。
        mylock.acquire()
        _from.lock.acquire()  # 锁住自己的账户
        to.lock.acquire()  # 锁住对方的账户
        # 交易#################
        _from.withdraw(amount)
        to.deposit(amount)
        #################
        to.lock.release()
        _from.lock.release()
        mylock.release()


def hashlock(_from, to):
    hash1 = hashlib.md5()
    hash1.update(bytes(_from.id, encoding='utf-8'))
    hasha = hash1.hexdigest()
    hash = hashlib.md5()
    hash.update(bytes(to.id, encoding='utf-8'))
    hashb = hash.hexdigest()
    return hasha, hashb


a = Account('a', 1000)
b = Account('b', 1000)
mylock = threading.Lock()
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
