import os

src_path = r'E:\python'
target_path = r'E:\新建文件夹 (2)'


def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        fileList = os.listdir(src)
        # 变量列表
        for file in fileList:
            # 拼接路径
            path = os.path.join(src, file)
            # 判断是文件夹还是文件
            if os.path.isdir(path):
                # 递归调用copy
                target_path1 = os.path.join(target_path, file)
                os.mkdir(target_path1)
                copy(path, target)
                target_path1 = os.path.join(target_path, file)
                if not os.path.exists(target_path1):
                    os.makedirs(target_path1)
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
