import os

src_path = r'Z:\test'

if not os.path.exists(src_path):
    print('没有读到文件夹')
else:
    print('读到文件夹')
    src_path_list = os.listdir(src_path)
    for src_list in src_path_list:
        copy_detail_path = os.path.join(src_path, src_list)
        if os.path.isdir(copy_detail_path):
            src_path_list_son = os.listdir(copy_detail_path)
            print(src_path_list_son)
    # with open(src_path, 'rb') as readStream:
    #     container = readStream.read()
