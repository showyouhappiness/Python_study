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







"""

list1 = [('000007',), ('000008',), ('000030',), ('006799',), ('006800',), ('006801',), ('006802',), ('006803',),
         ('006804',), ('006805',), ('006806',), ('006807',), ('006808',), ('006809',), ('006810',), ('006811',),
         ('006812',), ('006813',), ('006814',), ('006815',), ('006816',), ('006817',), ('006818',), ('006819',),
         ('006820',), ('006821',), ('006822',), ('006823',), ('006824',), ('006825',)]

for i, view_detail in enumerate(list1):
    print(i, view_detail[0].strip())
