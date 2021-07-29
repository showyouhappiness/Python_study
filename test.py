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

