#!/usr/bin/python  提示OS/Linux
# -*- coding: utf-8 -*-  提示使用utf-8
print('hello, world')
print('100+200=', 100 + 200)
name = 'Liyongjun'
print(name)
name = input('please enter your name:')
print('hello', name)

# 显示整数的绝对值 print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m "ok"!')
print('I\'m learning\npython')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')

print(100 + 200)
print('hello world')

import math  # 导入 math 模块

print("math.pow(100, 2) : ", math.pow(100, 2))  # 浮点数10000.0
print("math.pow(1_000_000, 2) : ", math.pow(1_000_000, 2))  # 浮点数10000.0
# 使用内置，查看输出结果区别
print("pow(100, 2) : ", pow(100, 2))  # 整数10000

print("math.pow(100, -2) : ", math.pow(100, -2))
print("math.pow(2, 4) : ", math.pow(2, 4))
print("math.pow(3, 0) : ", math.pow(3, 0))

count = 0
while (count < 9):
    print('The count is:', count)
    count += 1

print("Good bye!")
print(ord('A'), ord('中'), chr(66), chr(25991), '\u4e2d\u6587')

# print(x = b'ABC')

# str变为bytes
print('ABC'.encode('ascii'),
      '中文'.encode('utf-8'))

# bytes变为str
print(b'ABC'.decode('ascii'),
      b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# str包含多少个字符数
print(len('ABC'), len('中文'))
# str包含多少个字节数
print(len(b'ABC'), len(b'\xe4\xb8\xad\xe6\x96\x87'), len('中文'.encode('utf-8')))

# 保留两位小数
print('Age: %.2f. Gender: %s' % (25, True))

# 定义字符串变量name，输出"我的名字叫小明，请多多关照"
name = "小明"
print("我的名字叫 %s，请多多关照" % name)

# 定义整数变量student_no，输出"我的学号是 000001"
#  %o6d的意思是如果不够六位就在前面加0，如果够六位就显示全部
student_no = 1
print("我的学号是 %06d" % student_no)

# 定义小数price、weight、money
# 输出苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
# %.2f表示小数点后面取两位
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元/斤，购买了 %.2f 斤，需要支付 %.2f 元" % (price, weight, money))

# 定义一个小数scale，输出数据比例是10.00%
scale = 0.2
print("数据比例是 %.2f%%" % (scale * 100))

# 生成0-10的整数序列，计算如下：
sum = 0
list = list(range(11))
print(list)
for x in list:
    sum = sum + x
print(sum)

# 计算100以内所有奇数之和
sum = 0
n = 9
while n > 0:
    sum += n
    n -= 2
print(sum)

# 利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('Hello %s!' % a)

L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('Hello ' + a + '!')

L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('Hello', a, '!')

# 提前退出循环
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 只打印奇数，可以用continue语句跳过某些循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


# 求绝对值的my_abs函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-99))


# 只允许整数和浮点数类型的参数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
import math


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解
def quadratic(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        delta = b ** 2 - 4 * a * c
        if delta >= 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return x1, x2
        else:
            return '该方程无解'
    else:
        raise TypeError('bad operand type')


print(quadratic(1, 2, 1))


# 计算xn
def power(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        s = 1
        while y > 0:
            s *= x
            y -= 1
        return s
    else:
        raise TypeError('bad operand type')


print(power(6, 6))


# 我们写个一年级小学生注册的函数，需要传入name和gender两个参数,默认显示age和city
def enroll(name, gender, age=6, city="beijing"):
    print(name, gender, age, city)
    return name, gender, age, city


print(enroll('1', 'f', 7))


# 先定义一个函数，传入一个list，添加一个END再返回
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())


# 参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 利用可变参数，调用函数的方式可以简化成这样
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# *命名关键字参数  和 **关键字参数
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3, 4)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# 接收一个或多个数并计算乘积
def product(x, *y):
    for i in y:
        x *= i
    return x
