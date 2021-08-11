import os
import threading
import time

src_path = r'D:\test_images'
target_path = r'D:\images_crf'


def copy(src, target, i=0):
    copied_path = []
    if os.path.isdir(src) and os.path.isdir(target):
        fileList = os.listdir(src)
        while True:
            if i % 20 == 0 and i > 20:
                threading.Thread(target=delete_many_images, args=(copied_path,)).start()
            i += 1
            for file in fileList:
                path = os.path.join(src, file)
                with open(path, 'rb') as readStream:
                    container = readStream.read()
                    path1 = os.path.join(target, str(i) + file)
                    copied_path.append(path1)
                    with open(path1, 'wb') as writeStream:
                        time.sleep(1.2)
                        writeStream.write(container)


def delete_many_images(copied_path):
    # 先利用python的enumerate方法遍历要删除的个数 找到了counter
    for counter, index in enumerate(range(0, 21460)):
        index = index - counter
        # 删除数组里面的值
        copied_path.pop(index)
        # 遍历数组
        for k, v in enumerate(copied_path):
            # 判断数组的下标是否和index一致
            if k == index:
                os.remove(v)


copy(src_path, target_path)

# def copy(src, target, i=0):
#     copied_path = []
#     try:
#         if os.path.isdir(src) and os.path.isdir(target):
#             fileList = os.listdir(src)
#             while True:
#                 if i % 20 == 0 and i > 20:
#                     threading.Thread(target=delete_many_images, args=(copied_path,)).start()
#                 i += 1
#                 f_log.LOGW("第{}次开始复制".format(i))
#                 for file in fileList:
#                     path = os.path.join(src, file)
#                     with open(path, 'rb') as readStream:
#                         container = readStream.read()
#                         path1 = os.path.join(target, str(i) + file)
#                         copied_path.append(path1)
#                         with open(path1, 'wb') as writeStream:
#                             time.sleep(1.2)
#                             writeStream.write(container)
#                             f_log.LOGW("当前copy的文件是：{}".format(file))
#                 f_log.LOGW("第{}次结束复制".format(i))
#     except Exception as e:
#         f_log.LOGW("{}".format(e))
