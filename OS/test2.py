# 导入线程模块
import datetime
import os
import random
import threading
import time


def thread_Timer(batch_num, test_time):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d")
    src_path = r'D:\标准'
    result_path = r'D:\随机'
    batch_num_all = None
    fileDir_child = os.listdir(src_path)
    if test_time != now_time:
        test_time = now_time
        batch_num = random.randint(100, 200)
    for i in fileDir_child:
        copy_sample = src_path + '/' + i
        batch_num_all = batch_num + random.randint(220, 250)
        if os.path.isdir(copy_sample):
            fileList = os.listdir(copy_sample)
            sample_list = random.sample(fileList, 1)
            type_detail = '_' + sample_list[0].split('_')[1] + '_'
            for sample_image in fileList:
                if type_detail in sample_image:
                    split_name = sample_image.split('_')
                    split_name[0] = now_time
                    split_name[1] = str(batch_num_all)
                    new_name = '_'.join(split_name)
                    sample_image_path = copy_sample + '\\' + sample_image
                    with open(sample_image_path, 'rb') as readStream:
                        container = readStream.read()
                        result_image = result_path + '\\' + i + '\\' + new_name
                        with open(result_image, 'wb') as writeStream:
                            writeStream.write(container)

        random_time = random.randint(3, 8)
        time.sleep(random_time * 60)
    picknumber = random.randint(16, 20)
    print(picknumber)
    interval_time = 3600 * 24 / picknumber
    print(interval_time)
    createTime(batch_num_all, 60.0, test_time)


def createTime(batch_num, interval_time=10.0, test_time=None):
    # 创建并初始化线程
    threading.Timer(interval_time, thread_Timer, args=(batch_num, test_time)).start()


batch_num = random.randint(100, 200)
createTime(batch_num)
