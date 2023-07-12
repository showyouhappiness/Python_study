import json

list1 = [[1, 2, 3, 4], [2, 3, 4, 5]]
str1 = json.dumps(list1)
print(str1)
list2 = json.loads(str1)
print(list2)

# coding:utf-8
import time
import redis

number_list = ['300033', '300032', '300031', '300030']
signal = ['1', '-1', '1', '-1']

rc = redis.StrictRedis(host='localhost', port='6379', db=3, password='1q2w3e4r5t')
for i in range(len(number_list)):
    value_new = str(number_list[i]) + ' ' + str(signal[i])
    rc.publish("liao", value_new)  # 发布消息到

s = 'U:test/11231321.1.2.3.4.jpg'
print(".".join(s.split('.')[:-1]))

import commu
import ctypes

ptr = ctypes.c_void_p(id('hello world'))
print(ptr)
print(commu.ReadRecognizeInfo(ptr))

data = (ctypes.c_int * 5)()
json_string = 'hello world'
print(type(-1))
commu.ShareMemoryInit()
while True:
    result = commu.WriteRecognizeInfo(data, json_string)
    if result == int(-1):
        continue
    else:
        print(result)
        time.sleep(5)
    time.sleep(0.1)


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为零")
        return None
    else:
        return result
    finally:
        print("执行 finally 块")


# 调用函数
print(divide(10, 2))
print('-----------------------------------------------')
print(divide(10, 0))
