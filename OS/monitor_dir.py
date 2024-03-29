import os

import win32file
import win32con
from OS.log import f_log


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
            full_filename = os.path.join(path_to_watch, filename)
            f_log.LOGW('{} {}'.format(ACTIONS.get(action, "Unknown"), full_filename))
            if ACTIONS.get(action, "Unknown") == 'Created' or ACTIONS.get(action, "Unknown") == 'Updated':
                print(full_filename)


monitor_dir(r'X:\main')
