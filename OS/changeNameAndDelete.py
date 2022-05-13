import datetime
import os
import random


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


def main(src, target):
    now_time = None
    i = None
    file_path = None
    all_file_list = list()
    for file_detail in findAllFile(src):
        if 'PROC' in file_detail or 'COL' in file_detail:
            # os.remove(file_detail)
            continue
        filepath, fullflname = os.path.split(file_detail)
        sub_path = filepath.split('\\')[-1]
        if filepath != file_path:
            file_path = filepath
            now_time = datetime.datetime.now()
            i = 0

        index_time = fullflname.find('_')  # 查找 _ 的index值
        newName = fullflname.replace(fullflname[:index_time], now_time.strftime('%Y-%m-%d'))  # 用当前时间替换之前的时间
        target_path = target + '\\' + sub_path  # 根据目标的路径，构建出结果的路径

        # 判断是否为这个文件，没有就生成
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        target_detail = os.path.join(target_path, newName)

        # 判断当前的图片路径名称是不是已经存在了，存在就往前推一天
        if target_detail in all_file_list:
            newName = fullflname.replace(fullflname[:index_time],
                                         (now_time + datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))
            target_detail = os.path.join(target_path, newName)

        with open(file_detail, 'rb') as readStream:
            container = readStream.read()
            with open(target_detail, 'wb') as writeStream:
                writeStream.write(container)
        all_file_list.append(target_detail)
        i += 1


def moveFile(fileDir):
    fileDir_child = os.listdir(fileDir)
    for i in fileDir_child:
        fileDir_detail = fileDir + '\\' + i
        pathDir = os.listdir(fileDir_detail)
        picknumber = random.randint(15, 20)
        sample_list = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
        for sample_image in sample_list:
            sample_split = sample_image.split('_')
            sample_type = sample_split[0] + '_' + sample_split[1]
            for pathDir_detail in pathDir:
                if sample_type in pathDir_detail:
                    file_sample = fileDir_detail + '\\' + pathDir_detail
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
    for src_path in [public_path + r'\阶梯块结果图', public_path + r'\校准']:
        main(src_path, target)
    # moveFile(target)
