import os
import glob
from datetime import datetime

signal_loss = ['set signal_id: 4', 'RETURNING casting_id:', 'set signal_id: 5', 'reset signal_id 5']
normal = ['set signal_id: 4', 'RETURNING casting_id:', 'set signal_id: 5', 'reset signal_id 5', 'reset signal_id 4']
unusual = []


def glob_log_files(src_dir):
    f = glob.glob(src_dir + '\\*')  # 获取目录下所有文件
    for file in f:
        # 判断是否为文件
        if os.path.isfile(file):
            analyse_log(file)


def analyse_log(src_file, casting_id='', cost_time=''):
    with open(src_file, encoding='UTF-8') as file:  # 读取文件
        for line in file.readlines():
            if 'set signal_id: 4' in line or 'set signal_id: 3' in line:
                cost_time1 = line.split()[0] + ' ' + line.split()[1][0:-4]
                if unusual == normal and len(unusual) > 0:
                    print('正常', casting_id)
                else:
                    if unusual == signal_loss:
                        print('拍照位离开信号丢失', casting_id)
                    elif cost_time and (datetime.strptime(cost_time1, "%Y-%m-%d %H:%M:%S") -
                                        datetime.strptime(cost_time, "%Y-%m-%d %H:%M:%S")).seconds < 1:
                        print('信号跳变', casting_id)
                    else:
                        print('其他异常', casting_id)
                # 清空列表
                unusual.clear()
                unusual.append('set signal_id: 4')
            if 'reset signal_id 4' in line:
                cost_time = line.split()[0] + ' ' + line.split()[1][0:-4]
                unusual.append('reset signal_id 4')
            if 'set signal_id: 5' in line:
                unusual.append('set signal_id: 5')
            if 'reset signal_id 5' in line:
                unusual.append('reset signal_id 5')
            if 'RETURNING casting_id:' in line:
                casting_id = line.split()[-1]
                unusual.append('RETURNING casting_id:')
                # 将符合条件的行写入到目标文件中


if __name__ == '__main__':
    glob_log_files('E:\\log\\moluoge\\log_file3')
