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

# 计算10以内所有奇数之和
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
