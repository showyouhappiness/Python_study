import os

# N02212c07 V2 V3
# copy_path = r'E:\test_images\test'
# target_path = r'E:\result_images2'


def copy(copied, target):
    if os.path.isdir(copied) and os.path.isdir(target):
        # 被拷贝图片的列表
        copy_path_list = os.listdir(copied)
        for copy_list in copy_path_list:
            # 判断这个列表是不是文件夹
            copy_detail_path = os.path.join(copied, copy_list)
            # 如果是文件夹，则再次打开它
            if os.path.isdir(copy_detail_path):
                copy(copy_detail_path, target)
            else:
                # 需要查询的模板列表
                if 'N02212c07' in copy_detail_path:
                    if 'V2' in copy_detail_path or 'V3' in copy_detail_path:
                        with open(copy_detail_path, 'rb') as readStream:
                            container = readStream.read()
                            if not os.path.exists(target):
                                os.makedirs(target)
                            target_detail = os.path.join(target, copy_list)
                            with open(target_detail, 'wb') as writeStream:
                                writeStream.write(container)