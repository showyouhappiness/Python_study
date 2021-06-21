import os

src_path = r'E:\python'
copy_path = r'E:\test_images'
target_path = r'E:\result_images'


def copy(src, copied, target):
    if os.path.isdir(src) and os.path.isdir(copied) and os.path.isdir(target):
        # 被拷贝图片的列表
        copy_path_list = os.listdir(copied)
        for copy_list in copy_path_list:
            # 判断这个列表是不是文件夹
            copy_detail_path = os.path.join(copied, copy_list)
            # 如果是文件夹，则再次打开它
            if os.path.isdir(copy_detail_path):
                copy(src, copy_detail_path, target)
            else:
                # 需要查询的模板列表
                src_path_list = os.listdir(src)
                for src_list in src_path_list:
                    if src_list == copy_list:
                        with open(copy_detail_path, 'rb') as readStream:
                            container = readStream.read()
                            if not os.path.exists(target):
                                os.makedirs(target)
                            target_detail = os.path.join(target, src_list)
                            with open(target_detail, 'wb') as writeStream:
                                writeStream.write(container)


copy(src_path, copy_path, target_path)
