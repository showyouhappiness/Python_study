# 导入线程模块
import datetime
import os
import random
import threading
import time


def thread_Timer(batch_num):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    src_path = r'E:\workImages\图片过滤与修改时间\result'
    result_path = r'E:\workImages\图片过滤与修改时间\test'
    batch_num_all = None
    fileDir_child = os.listdir(src_path)
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

    createTime(batch_num_all)


def createTime(batch_num):
    picknumber = random.randint(16, 20)
    interval_time = 3600 * 24 / picknumber
    print(interval_time)
    # 创建并初始化线程
    threading.Timer(interval_time, thread_Timer, args=(batch_num,)).start()


batch_num = random.randint(100, 200)
createTime(batch_num)
