import os
import threading
import time


def moveFile(fileDir):
    sample_type_list = list()
    if os.path.isdir(fileDir):
        fileList = os.listdir(fileDir)
        while True:
            for sample_image in fileList:
                sample_split = sample_image.split('_')
                sample_type = sample_split[1]
                if sample_type not in sample_type_list:
                    time.sleep(0.05)
                    sample_type_list.append(sample_type)
                    print(len(sample_type_list))
                if len(sample_type_list) % 200 == 0:
                    for pathDir_detail in fileList:
                        if sample_type in pathDir_detail:
                            file_sample = fileDir + '\\' + pathDir_detail
                            target_sample = public_path + r'/test/' + i + '/'
                            if not os.path.exists(target_sample):
                                os.makedirs(target_sample)
                            sample_result = os.path.join(target_sample, pathDir_detail)
                            with open(file_sample, 'rb') as readStream:
                                container = readStream.read()
                                with open(sample_result, 'wb') as writeStream:
                                    writeStream.write(container)


if __name__ == '__main__':
    public_path = r'E:\workImages\图片过滤与修改时间'
    target = public_path + r'\result'
    fileDir_child = os.listdir(target)
    for i in fileDir_child:
        copy_sample = target + '/' + i
        moveFile(copy_sample)
        # threading.Thread(target=moveFile, args=(copy_sample,)).start()
