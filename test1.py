# # import json
# #
# # list1 = [[1, 2, 3, 4], [2, 3, 4, 5]]
# # str1 = json.dumps(list1)
# # print(str1)
# # list2 = json.loads(str1)
# # print(list2)
import time

#
# # coding:utf-8
# import time
# import redis
#
# number_list = ['300033', '300032', '300031', '300030']
# signal = ['1', '-1', '1', '-1']
#
# rc = redis.StrictRedis(host='localhost', port='6379', db=3, password='1q2w3e4r5t')
# for i in range(len(number_list)):
#     value_new = str(number_list[i]) + ' ' + str(signal[i])
#     rc.publish("liao", value_new)  # 发布消息到
#
# s = 'U:test/11231321.1.2.3.4.jpg'
# print(".".join(s.split('.')[:-1]))


# list1 = ['set signal_id: 4', 'RETURNING casting_id:', 'set signal_id: 5', 'reset signal_id 4', 'reset signal_id 5']
# list2 = ['set signal_id: 5', 'RETURNING casting_id:', 'set signal_id: 4', 'reset signal_id 4', 'reset signal_id 5']
#
# # 判定两个列表是否相等
# if list1 == list2:
#     print('相等')
# else:
#     print('不相等')
# tital = 100
# for i in range(2):
#     tital = tital - 10
#     print(tital)

import commu
import ctypes

# ptr = ctypes.c_void_p(id('hello world'))
# print(ptr)
# print(commu.ReadRecognizeInfo(ptr))

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
