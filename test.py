"""
将文件从一台服务器上拷贝到另外一台服务器上
scp 需要拷贝的文件路径 用户名(一般是root用户分配的用户)@另一台服务器的地址:存放的具体地址

将一个文件夹从一台服务器上拷贝到另外一台服务器上
scp -r 需要拷贝的文件夹路径 用户名(一般是root用户分配的用户)@另一台服务器的地址:存放的具体地址


使用sftp连接另外一台服务器
sftp root@另一台服务器的地址

上传可以使用：
put 上传的文件
put -r 上传的文件夹
下载可以使用：
get 下载的文件
get -r 下载的文件夹

查看远端的路径：
使用 pwd
# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)


import uuid

print(uuid.uuid4())


# import time
# import datetime
#
# now = time.time()
# print(now)
#
# now1 = datetime.datetime.now()
#
# print(now1)
# print(now1.second)
# print(now1.microsecond)

# import datetime
# import os
#
# now_time = datetime.datetime.now()
# yes_time = now_time + datetime.timedelta(days=-1)
# yes_time_nyr = yes_time.strftime('%Y-%m-%d')
#
# src_path = r'E:\work\ai_server\log\log_file'
# target_path = r'E:\log'
#
#
# def copy(src, target, time):
#     if os.path.isdir(src) and os.path.isdir(target):
#         fileList = os.listdir(src)
#         for file in fileList:
#             if time in file:
#                 path = os.path.join(src, file)
#                 with open(path, 'rb') as readStream:
#                     container = readStream.read()
#                     path1 = os.path.join(target, file)
#                     with open(path1, 'wb') as writeStream:
#                         writeStream.write(container)
#
#
# copy(src_path, target_path, yes_time_nyr)


# str1 = str(msg.payload, encoding="utf-8")
# data = eval(str1)
# print(data['name'])






#
# list1 = [('000007',), ('000008',), ('000030',), ('006799',), ('006800',), ('006801',), ('006802',), ('006803',),
#          ('006804',), ('006805',), ('006806',), ('006807',), ('006808',), ('006809',), ('006810',), ('006811',),
#          ('006812',), ('006813',), ('006814',), ('006815',), ('006816',), ('006817',), ('006818',), ('006819',),
#          ('006820',), ('006821',), ('006822',), ('006823',), ('006824',), ('006825',)]
#
# for i, view_detail in enumerate(list1):
#     print(i, view_detail[0].strip())
# import datetime
#
# nowTime = datetime.datetime.now().timetuple()
# VersionInfo = str(nowTime.tm_year) + "-" + str(nowTime.tm_mon) + "-" + str(nowTime.tm_mday)
# print(VersionInfo)
# print(399 % 400 == 399)
# 导入线程模块
import threading


def thread_Timer():
    print("该起床啦...5秒之后再次呼叫你起床...")

    # # 声明全局变量
    # global t1
    # # 创建并初始化线程
    # t1 = threading.Timer(1, thread_Timer)
    # # 启动线程
    # t1.start()


if __name__ == "__main__":
    # 创建并初始化线程
    t1 = threading.Timer(5, thread_Timer)
    # 启动线程
    t1.start()


def add(numbers, initial=0):
    for i in numbers.split(','):
        initial += int(i)
    return initial


result = add(input())
print(result)





# import json
#
# key_list = []
#
#
# def generate_file():
#     with open('C:\\Users\\Administrator\\.crf-config.json', 'r') as f:
#         read_result = json.loads(f.read())
#         return read_result
#
#
# def get_dict_allkeys(dict_a):
#     '''
#     多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
#     :param dict_a:
#     :return: key_list
#     '''
#     if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
#         for x in range(len(dict_a)):
#             temp_key = list(dict_a.keys())[x]
#             temp_value = dict_a[temp_key]
#             key_list.append(temp_key)
#             get_dict_allkeys(temp_value)  # 自我调用实现无限遍历
#     elif isinstance(dict_a, list):
#         for k in dict_a:
#             if isinstance(k, dict):
#                 for x in range(len(k)):
#                     temp_key = list(k.keys())[x]
#                     temp_value = k[temp_key]
#                     key_list.append(temp_key)
#                     get_dict_allkeys(temp_value)
#     return key_list
#
#
# # get_dict_allkeys(generate_file())
# print(get_dict_allkeys(generate_file()))


import re


def is_number(str_to_num):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(str_to_num)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass
    try:
        import unicodedata  # 处理ASCii码的包
        for i in str_to_num:
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
            # return True
        return True
    except (TypeError, ValueError):
        pass
    return False


def is_float_number(strNum):
    pattern_list = [r'^\d+\.?$',  # 123.
                    r'^\.?\d+$',  # .123
                    r'^\d+\.?\d+$',  # 123.123/123123
                    r'^\d+\.?e\+?\d+$',  # 123.e123/123.e+123
                    r'^\.?\d+e\+?\d+$',  # .123e123/.123e+123
                    r'^\d+\.?\d+e\+?\d+$',  # 123.123e123/123123e123/123.123e+123/123123e+123
                    r'^\d+\.?e\-\d+$',  # 123.e-123
                    r'^\.?\d+e\-\d+$',  # .123e-123
                    r'^\d+\.?\d+e\-\d+$']  # 123.123e-123/123123e-123

    for pattern_str in pattern_list:
        pattern_float = re.compile(pattern_str)
        result_float = pattern_float.match(strNum)
        if result_float:
            return True

    return False
"""
# a = {100: {'x': 1, 'y': 2}, 101: {'x': 2, 'y': 0}, 102: {'x': 0, 'y': 3}}
# b = sorted(a.items(), key=lambda z: z[1]['x'])
# print(b)
import uuid

print(uuid.uuid4())
