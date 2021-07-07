import os

copy_path = r'E:\workImages\x5'
target_path = r'E:\result_images1'
images_list = []


def copy(copied, target):
    if not os.path.exists(target):
        os.makedirs(target)
    if os.path.isdir(copied) and os.path.isdir(target):
        # 被拷贝图片的列表
        copy_path_list = os.listdir(copied)
        if len(copy_path_list) > 5:
            images_list.clear()
            for copy_list in copy_path_list:
                # 判断这个列表是不是文件夹
                copy_detail_path = os.path.join(copied, copy_list)
                # 如果是文件夹，则再次打开它
                if os.path.isdir(copy_detail_path):
                    copy(copy_detail_path, target)
                else:
                    images_list.append(copy_detail_path)
                    if len(images_list) == 2:
                        images_filename = os.path.split(images_list[0])[1]
                        images_list_1 = int(os.path.splitext(images_list[1])[0][-2:])
                        images_list_0 = int(os.path.splitext(images_list[0])[0][-2:])
                        if int(os.path.splitext(images_list[0])[0][-2:]) >= 58:
                            images_list_0 = int(os.path.splitext(images_list[0])[0][-2:]) - 60
                        if images_list_1 - images_list_0 == 2:
                            with open(images_list[0], 'rb') as readStream:
                                container = readStream.read()
                                target_detail = os.path.join(target, images_filename)
                                with open(target_detail, 'wb') as writeStream:
                                    writeStream.write(container)
                                images_list.pop(0)
                        else:
                            with open(images_list[0], 'rb') as readStream:
                                container = readStream.read()
                                target_detail = os.path.join(target, images_filename)
                                with open(target_detail, 'wb') as writeStream:
                                    writeStream.write(container)
                            break
        else:
            print(copy_path_list[0][:11])
            for copy_list in copy_path_list:
                copy_detail_path = os.path.join(copied, copy_list)
                with open(copy_detail_path, 'rb') as readStream:
                    container = readStream.read()
                    target_detail = os.path.join(target, copy_list)
                    with open(target_detail, 'wb') as writeStream:
                        writeStream.write(container)


copy(copy_path, target_path)
