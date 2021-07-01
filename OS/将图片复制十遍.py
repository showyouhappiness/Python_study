import os

src_path = r'E:\workImages\test_image'
target_path = r'D:\images_crf'


def copy(i, src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        fileList = os.listdir(src)
        for file in fileList:
            path = os.path.join(src, file)
            with open(path, 'rb') as readStream:
                container = readStream.read()
                path1 = os.path.join(target, str(i) + file)
                with open(path1, 'wb') as writeStream:
                    writeStream.write(container)
        else:
            print('复制完成！')


for i in range(10):
    copy(i, src_path, target_path)