import os

src_path = r'E:\workImages\test_image'
target_path = r'D:\images_crf'


def copy(src, target, i):
    if os.path.isdir(src) and os.path.isdir(target):
        fileList = os.listdir(src)
        while True:
            i += 1
            for file in fileList:
                path = os.path.join(src, file)
                with open(path, 'rb') as readStream:
                    container = readStream.read()

                    path1 = os.path.join(target, str(i) + file)
                    with open(path1, 'wb') as writeStream:
                        writeStream.write(container)


copy(src_path, target_path, 0)
