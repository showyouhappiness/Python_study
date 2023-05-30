import os

import threading
import win32file
import win32con
import conf
from log import f_log
import shutil


def parse_file_name(copied):
    if os.path.exists(copied):
        if 'V1' in copied:
            (filepath, tempFilename) = os.path.split(copied)
            wheel_type = tempFilename[int(tempFilename.find('N')):int(tempFilename.find('R'))]
            # 判断目标文件夹是否存在
            if not os.path.exists(conf.tag_path):
                os.makedirs(conf.tag_path)
            if 'f' in wheel_type:
                # 复制文件
                try:
                    shutil.copy(copied, conf.tag_path)
                    f_log.LOGW(f'copy file: {copied} to {conf.tag_path} success')
                except Exception as e:
                    f_log.LOGE(f'copy file error: {e}')


def monitor_dir(path_to_watch):
    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }

    FILE_LIST_DIRECTORY = 0x0001
    print('Watching changes in', path_to_watch)

    hDir = win32file.CreateFile(
        path_to_watch,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
    )
    while 1:

        results = win32file.ReadDirectoryChangesW(
            hDir,
            1024,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
            win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
            win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
            win32con.FILE_NOTIFY_CHANGE_SIZE |
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
            win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None)
        for action, filename in results:
            full_filename = os.path.join(path_to_watch, filename)
            if ACTIONS.get(action, "Unknown") == 'Created':
                # 使用线程执行
                threading.Timer(1, function=parse_file_name, args=(full_filename,)).start()


monitor_dir(conf.copy_path)
