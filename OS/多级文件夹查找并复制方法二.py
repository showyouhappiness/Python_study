import os

src_path = r'E:\python'
copy_path = r'E:\test_images'
target_path = r'E:\result_images'


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


def main(src, copied, target):
    src_path_list = os.listdir(src)
    for src_list in src_path_list:
        for i in findAllFile(copied):
            if src_list in i:
                with open(i, 'rb') as readStream:
                    container = readStream.read()
                    if not os.path.exists(target):
                        os.makedirs(target)
                    target_detail = os.path.join(target, src_list)
                    with open(target_detail, 'wb') as writeStream:
                        writeStream.write(container)


if __name__ == '__main__':
    main(src_path, copy_path, target_path)
