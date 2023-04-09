import os
import time
import win32file
import win32con


class Monitor(object):
    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }

    FILE_LIST_DIRECTORY = 0x0001

    def __init__(self, path_to_watch):
        super().__init__()
        self.path_to_watch = path_to_watch

    def run(self):
        hDir = win32file.CreateFile(
            self.path_to_watch,
            self.FILE_LIST_DIRECTORY,
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
                full_filename = os.path.join(self.path_to_watch, filename)
                if self.ACTIONS.get(action, "Unknown") == "Created" and full_filename == r'test\1':
                    print("File created: %s" % full_filename)
                    watcher(full_filename)


def watcher(log_path):
    count = 0
    position = 0
    try:
        with open(log_path, mode='r', encoding='utf8') as f1:
            while True:
                line = f1.readline().strip()
                print(line)
                if line:
                    count += 1
                    print("count %s line %s" % (count, line))

                cur_position = f1.tell()  # 记录上次读取文件的位置
                if cur_position == position:
                    continue
                else:
                    position = cur_position
    except Exception as e:
        print(e)
        time.sleep(1)


if __name__ == '__main__':
    watcher("./2.txt")
