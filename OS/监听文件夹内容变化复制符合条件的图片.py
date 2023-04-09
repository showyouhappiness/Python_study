import os
import sys
import traceback

import monitor
from queue import Queue
from OS.log import f_log


def parse_file_name(copied, target):
    try:
        if 'N05117c05' in copied:
            if 'V2' in copied or 'V3' in copied:
                with open(copied, 'rb') as readStream:
                    container = readStream.read()
                    if not os.path.exists(target):
                        os.makedirs(target)
                    image_name = os.path.split(copied)
                    target_detail = os.path.join(target, image_name[1])
                    with open(target_detail, 'wb') as writeStream:
                        writeStream.write(container)
                    f_log.LOGW("Image {} download successfully".format(copied))
    except:
        f_log.LOGW("Image {} download failed".format(copied))


if __name__ == '__main__':
    queue = Queue()
    dir_one = r'Y:\\'
    dir_two = r'Z:\\'
    dir_three = r'X:\\'
    dir_four = r'W:\\'
    target_one = r'D:\Downloads\DefectX3\xray1'
    target_two = r'D:\Downloads\DefectX3\xray2'
    target_three = r'D:\Downloads\DefectX3\xray3'
    target_four = r'D:\Downloads\DefectX3\xray4'
    monitor.Monitor(dir_one, queue).start()
    monitor.Monitor(dir_two, queue).start()
    monitor.Monitor(dir_three, queue).start()
    monitor.Monitor(dir_four, queue).start()

    while True:
        try:
            info = queue.get()
            queue.task_done()
            copy_path = info.file_name
            if 'Y:\\' in copy_path:
                parse_file_name(copy_path, target_one)
            elif 'Z:\\' in copy_path:
                parse_file_name(copy_path, target_two)
            elif 'X:\\' in copy_path:
                parse_file_name(copy_path, target_three)
            elif 'W:\\' in copy_path:
                parse_file_name(copy_path, target_four)

        except KeyboardInterrupt:
            sys.exit()
        except:
            print(traceback.format_exc())
