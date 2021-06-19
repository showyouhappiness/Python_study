import os

src_path = r'E:\新建文件夹'
target_path = r'E:\新建文件夹 (2)'


def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        fileList = os.listdir(src)
        for file in fileList:
            path = os.path.join(src, file)
            with open(path, 'rb') as readStream:
                container = readStream.read()
                path1 = os.path.join(target, file)
                with open(path1, 'wb') as writeStream:
                    writeStream.write(container)
        else:
            print('复制完成！')


copy(src_path, target_path)
