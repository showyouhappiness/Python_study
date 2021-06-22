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
        src_name = os.path.join(src, src_list)
        result = os.path.splitext(src_list)
        for i in findAllFile(copied):
            if result[0] in i:
                if not os.path.exists(target):
                    os.makedirs(target)
                N_index = result[0].find('N')
                R_index = result[0].find('R')
                wheel_type = result[0][int(N_index):int(R_index)]
                target_detail = target + '/' + wheel_type
                if not os.path.exists(target_detail):
                    os.makedirs(target_detail)
                # 复制原图
                with open(i, 'rb') as readStream:
                    container_master = readStream.read()
                    target_detail_path = os.path.join(target_detail, result[0]+'.jpg')
                    with open(target_detail_path, 'wb') as writeStream:
                        writeStream.write(container_master)
                # 复制mark图
                with open(src_name, 'rb') as readStream:
                    container_mark = readStream.read()
                    target_detail_path = os.path.join(target_detail, result[0] + '_mark.jpg')
                    with open(target_detail_path, 'wb') as writeStream:
                        writeStream.write(container_mark)


if __name__ == '__main__':
    main(src_path, copy_path, target_path)
