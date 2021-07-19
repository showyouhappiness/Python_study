import os

src_path = r'E:\python'
copy_path = r'E:\test_images'
target_path = r'E:\result_images2'

images_string = []


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


def main(src, copied, target):
    src_path_list = os.listdir(src)
    for src_list in src_path_list:
        src_name = os.path.join(src, src_list)
        result = os.path.splitext(src_list)
        for i in findAllFile(copied):
            images_string.append(i)
            filename_str = ''.join(images_string)
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
