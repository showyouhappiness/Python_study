import os

src_path = r'D:\mark'
copy_path = r'D:\images'
target_path = r'D:\mark_not_found'

images_string = []
filename_str = ''


def findAllFile(base):
    global filename_str
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            images_string.append(fullname)
            filename_str = ''.join(images_string)


def main(src, copied, target):
    global filename_str
    findAllFile(copied)
    src_path_list = os.listdir(src)
    for src_list in src_path_list:
        src_name = os.path.join(src, src_list)
        result = os.path.splitext(src_list)
        if result[0] not in filename_str:
            if not os.path.exists(target):
                os.makedirs(target)
            # 复制mark图
            with open(src_name, 'rb') as readStream:
                container_mark = readStream.read()
                target_detail_path = os.path.join(target, src_list)
                with open(target_detail_path, 'wb') as writeStream:
                    writeStream.write(container_mark)


if __name__ == '__main__':
    main(src_path, copy_path, target_path)
