import os
import shutil

import conf
from OS.log import f_log
import win32file
import win32con


def monitor_dir(path_to_watch):
    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }

    FILE_LIST_DIRECTORY = 0x0001
    f_log.LOGW('Watching changes in {}'.format(path_to_watch))

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
            f_log.LOGW('{} {}'.format(ACTIONS.get(action, "Unknown"), filename))
            if conf.wheel_type in filename and ACTIONS.get(action, "Unknown") == 'Created':
                full_filename = os.path.join(path_to_watch, filename)
                wheel_step = "V" + conf.step
                if wheel_step in filename:
                    result_path = os.path.join(conf.save_image_path, wheel_step)
                    if not os.path.exists(result_path):
                        os.makedirs(result_path)
                    shutil.copy(full_filename, result_path)


monitor_dir(conf.original_path)
