import os
import glob

normal = ['set signal_id: 4', 'RETURNING casting_id:', 'set signal_id: 5', 'reset signal_id 4', 'reset signal_id 5']
unusual = []


def glob_log_files(src_dir):
    f = glob.glob(src_dir + '\\*')  # 获取目录下所有文件
    for file in f:
        # 判断是否为文件
        if os.path.isfile(file):
            analyse_log(file, 'E:\\log\\chengdu\\log_file7\\log_file7.txt')


def analyse_log(src_file, tar_file):
    with open(tar_file, 'a+', encoding='UTF-8') as target_file:  # 追加写入
        with open(src_file, encoding='UTF-8') as file:  # 读取文件
            for line in file.readlines():
                if 'set signal_id: 4' in line or 'reset signal_id 4' in line or 'set signal_id: 5' in line or \
                        'reset signal_id 5' in line or 'RETURNING casting_id:' in line:
                    # 将符合条件的行写入到目标文件中
                    target_file.write(line)


if __name__ == '__main__':
    glob_log_files('E:\\log\\chengdu\\log_file7')
