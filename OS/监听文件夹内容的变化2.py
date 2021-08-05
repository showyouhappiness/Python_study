#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<检测文件夹变化>

# 导入watchdog对应模块
from watchdog.observers import Observer
from watchdog.events import *
# 导入时间模块
import time
from test import copy

target_path = r'E:\result_images2'


class FileEventHandler(FileSystemEventHandler):
    # 初始化魔术方法
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    # 文件或文件夹移动
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    # 创建文件或文件夹
    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
        self.copy_image(event.src_path, target_path)

    # 删除文件或文件夹
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    # 移动文件或文件夹
    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))

    def copy_image(self, copied, target):
        if '.jpg' in copied:
            copied = os.path.dirname(copied)

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


if __name__ == "__main__":
    # 实例化Observer对象
    observer = Observer()
    event_handler = FileEventHandler()
    # 设置监听目录
    dis_dir = "E:/result_images"
    observer.schedule(event_handler, dis_dir, True)
    observer.start()
    try:
        while True:
            # 设置监听频率(间隔周期时间)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
