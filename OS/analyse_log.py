import argparse
import os
import datetime

barCodeDict = {}


def getbarcode():
    with open("E:/xinglong/xinglongbarcode.txt", encoding='UTF-8', errors='ignore') as barcodeFile:
        for barcodeLine in barcodeFile.readlines():
            time1 = barcodeLine.split(" ")
            knuckle_id = time1[-2].split(".")[1]
            barCodeDict[knuckle_id] = time1[-1]


def analyse_log(src_file, tar_file):
    knuckle_id = ""
    ft = ""
    lt = ""
    first_time = ""

    with open(tar_file, 'a+', encoding='UTF-8') as target_file:
        with open(src_file, encoding='UTF-8', errors='ignore') as file:
            for line in file.readlines():
                if 'crf_server.log' in line:
                    continue
                time = line.split(" ")
                if time[-5] != knuckle_id:
                    if lt and barCode and int((last_time - first_time).seconds) > 5:
                        print(first_time, barCode[:-1], (last_time - first_time).seconds)
                        container = "\nfirst_time：" + str(first_time) + "barCode: " + barCode[:-1] + " cost time: " + str(
                            (last_time - first_time).seconds)
                        target_file.write(container)
                    knuckle_id = time[-5]
                    barCode = barCodeDict.get(knuckle_id)
                    ft = time[2] + " " + time[3][:8]
                    first_time = datetime.datetime.strptime(ft, '%Y-%m-%d %H:%M:%S')
                else:
                    lt = time[2] + " " + time[3][:8]
                    last_time = datetime.datetime.strptime(lt, '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    DEFAULT_SRC = ''
    DEFAULT_DST = ''

    parser = argparse.ArgumentParser(description='analyse_log')

    parser.add_argument('--input', action="store", dest="input", default=DEFAULT_SRC)
    parser.add_argument('--output', action="store", dest="output", default=DEFAULT_DST)

    given_args = parser.parse_args()

    input_path = given_args.input
    output_path = given_args.output
    getbarcode()
    analyse_log(input_path, output_path)
# import datetime
#
# t1 = datetime.datetime.strptime("2016-08-24 10:30:00", "%Y-%m-%d %H:%M:%S")
# t2 = datetime.datetime.strptime("2016-08-24 12:30:00", "%Y-%m-%d %H:%M:%S")
#
# interval_time = (t2 - t1).seconds
# print(interval_time)
