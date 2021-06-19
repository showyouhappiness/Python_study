import os

src_path = r'E:\python'
target_path = r'E:\新建文件夹 (2)'


def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        fileList = os.listdir(src)
        for file in fileList:
            path = os.path.join(src, file)
            if os.path.isdir(path):
                copy(path, target)
            else:
                with open(path, 'rb') as readStream:
                    container = readStream.read()
                    path1 = os.path.join(target, file)
                    with open(path1, 'wb') as writeStream:
                        writeStream.write(container)
        else:
            print('复制完成！')


def delete(src):
    if os.path.isdir(src):
        fileList = os.listdir(src)
        for file in fileList:
            path = os.path.join(src, file)
            if os.path.isdir(path):
                delete(path)
                if len(os.listdir(path)) == 0:
                    os.rmdir(path)
            else:
                os.remove(path)
        print('删除成功！')


copy(src_path, target_path)
delete(src_path)
