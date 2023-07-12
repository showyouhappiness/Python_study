import os

src_path = r'D:\mark'
copy_path = r'D:\images'
target_path = r'D:\images_repeat'

images_string = []
filename_str = ''


def findAllFile(base):
    global filename_str
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            images_string.append(fullname)
            filename_str = ''.join(images_string)


def main(copied, target):
    global filename_str
    findAllFile(copied)
    for root, ds, fs in os.walk(copied):
        for f in fs:
            fullname = os.path.join(root, f)
            result = os.path.splitext(f)
            if filename_str.count(result[0]) == 2:
                if not os.path.exists(target):
                    os.makedirs(target)
                # 复制mark图
                with open(fullname, 'rb') as readStream:
                    container_mark = readStream.read()
                    target_detail_path = os.path.join(target, f)
                    with open(target_detail_path, 'wb') as writeStream:
                        writeStream.write(container_mark)


if __name__ == '__main__':
    main(copy_path, target_path)
