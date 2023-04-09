import os
from OS.log import f_log


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


def main(wheel_type, copied, target):
    for i in findAllFile(copied):
        result = os.path.split(i)
        if wheel_type in result[1] and ('V2' in result[1] or 'V3' in result[1]):
            with open(i, 'rb') as readStream:
                container = readStream.read()
                if not os.path.exists(target):
                    os.makedirs(target)
                target_detail = os.path.join(target, result[1])
                with open(target_detail, 'wb') as writeStream:
                    writeStream.write(container)
            f_log.LOGW("复制图片{}完成！！！".format(result[1]))


if __name__ == '__main__':
    wheel_type = '02212c07'
    copy_path = r'E:\test_images'
    target_path = r'E:\result_images2'
    main(wheel_type, copy_path, target_path)
