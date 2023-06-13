import os
import glob
from datetime import datetime

normal = ['detect_in: set signal_id: 4', 'RETURNING casting_id:', 'detect_out: set signal_id: 5',
          'detect_out: reset signal_id: 5', 'detect_in: reset signal_id: 4']
clear = ['detect_in: set signal_id: 4', 'detect_out: set signal_id: 5', 'detect_out: reset signal_id: 5',
         'detect_in: reset signal_id: 4']
normal1 = ['detect_in: set signal_id: 4', 'RETURNING casting_id:', 'detect_out: set signal_id: 5',
           'detect_out: reset signal_id: 5', 'detect_in: reset signal_id: 4', 'judge_in: set signal_id: 6',
           'judge_in: reset signal_id: 6']
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
            if 'detect_in: set signal_id: 4' in line or 'manual_clean: set signal_id: 3' in line:
                cost_time1 = line.split()[0] + ' ' + line.split()[1][0:-4]
                if set(normal).issubset(set(unusual)) and len(unusual) > 0:  # 判断是否为正常信号, issubset()判断是否为子集
                    print('正常', casting_id)
                else:
                    if cost_time and (datetime.strptime(cost_time1, "%Y-%m-%d %H:%M:%S") -
                                      datetime.strptime(cost_time, "%Y-%m-%d %H:%M:%S")).seconds < 1:
                        print('信号跳变', casting_id)
                    if not set(normal).issubset(set(unusual)):
                        print('信号丢失', casting_id)
                    else:
                        print('其他异常', casting_id)
                # 清空列表
                unusual.clear()
            for i in normal:
                if i in line:
                    unusual.append(i)
                    if i == 'set signal_id: 4':
                        cost_time = line.split()[0] + ' ' + line.split()[1][0:-4]
                    elif i == 'RETURNING casting_id:':
                        casting_id = line.split()[-1]
                # 将符合条件的行写入到目标文件中


if __name__ == '__main__':
    glob_log_files('E:\\log\\xinglong\\log_file10')
