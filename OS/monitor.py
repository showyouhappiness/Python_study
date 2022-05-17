import datetime
import os
import threading
import time
import traceback

import pywintypes
import win32con
import win32event
import win32file


class Monitor(threading.Thread):
    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }
    FILE_LIST_DIRECTORY = 0x0001

    def __init__(self, path_to_watch,  file_queue):
        super().__init__()
        self.name = "Monitor thread"
        self.daemon = True
        self.path_to_watch = path_to_watch
        self.file_queue = file_queue
        self.monitor_thread_exit_flag = False

    def run(self):


        while True:
            if os.path.exists(self.path_to_watch):
                break
            else:
                # if self.server_state != MessageCode.M_ERROR_MONITOR_PATH_NO_EXIST:
                #     self.alarm_func(MessageCode.M_ERROR_MONITOR_PATH_NO_EXIST, '无法读取X光图像路径')
                time.sleep(1)

        hDir = win32file.CreateFile(
            self.path_to_watch,
            self.FILE_LIST_DIRECTORY,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED,
            None)

        overlapped = pywintypes.OVERLAPPED()
        overlapped.hEvent = win32event.CreateEvent(None, 0, 0, None)
        buffer = win32file.AllocateReadBuffer(1024 * 64)

        updated_file = ''
        updatetimes = 0

        win32file.ReadDirectoryChangesW(hDir,
                                        buffer,
                                        True,
                                        win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                                        win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                                        overlapped)

        while self.monitor_thread_exit_flag is False:
            try:
                ret = win32event.WaitForSingleObject(overlapped.hEvent, 5000)

                if ret == win32event.WAIT_OBJECT_0:
                    nbytes = win32file.GetOverlappedResult(hDir, overlapped, True)
                    if nbytes > 0:

                        for action, file in win32file.FILE_NOTIFY_INFORMATION(buffer, nbytes):
                            if self.ACTIONS.get(action, "Unknown") == r'Updated':
                                full_filename = os.path.join(self.path_to_watch, file)
                                _, extension = os.path.splitext(full_filename)
                                if not os.path.isfile(full_filename) or os.path.splitext(full_filename)[1] == '.db':
                                    continue

                                if extension != '.jpg' and extension != '.bmp' and extension != '.png':
                                    continue

                                if updated_file == full_filename:
                                    updatetimes = updatetimes + 1
                                else:
                                    updatetimes = 1
                                    updated_file = full_filename
                                    self.file_queue.put(type_define.MonitorData(
                                        file_name=updated_file,
                                        monitor_time=datetime.datetime.now(),
                                        file_create_time=datetime.datetime.fromtimestamp(os.path.getctime(
                                            updated_file)),
                                        file_modify_time=datetime.datetime.fromtimestamp(os.path.getmtime(
                                            updated_file)),
                                        file_access_time=datetime.datetime.fromtimestamp(os.path.getatime(
                                            updated_file))
                                    ))
                                    f_log.LOGW(f"update file {updated_file} queue size = {self.file_queue.qsize()}")

                    win32file.ReadDirectoryChangesW(hDir,
                                                    buffer,
                                                    True,
                                                    win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                                                    win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                                                    overlapped)
                else:
                    f_log.LOGI("monitor_picture timeout ++++++++++++++++++++++")
            except Exception as e:
                f_log.LOGW(f"{traceback.format_exc()}")
                while True:
                    if os.path.exists(self.path_to_watch):
                        f_log.LOGW(f'{self.path_to_watch} exist')
                        break
                    else:
                        f_log.LOGW(f'{self.path_to_watch} not exist')
                        # if self.server_state != MessageCode.M_ERROR_MONITOR_PATH_NO_EXIST:
                        #     self.alarm_func(MessageCode.M_ERROR_MONITOR_PATH_NO_EXIST, '无法读取X光图像路径')
                        time.sleep(1)

                hDir = win32file.CreateFile(
                    self.path_to_watch,
                    self.FILE_LIST_DIRECTORY,
                    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
                    None,
                    win32con.OPEN_EXISTING,
                    win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED,
                    None)
                win32file.ReadDirectoryChangesW(hDir,
                                                buffer,
                                                True,
                                                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                                                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                                                overlapped)
            f_log.LOGI("monitor_picture next+++++++++++++++++++++++++++++")
            if not os.path.exists(self.path_to_watch):
                f_log.LOGW(f'{self.path_to_watch} not exist')
                while True:
                    if os.path.exists(self.path_to_watch):
                        f_log.LOGW(f'{self.path_to_watch} exist')
                        hDir = win32file.CreateFile(
                            self.path_to_watch,
                            self.FILE_LIST_DIRECTORY,
                            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
                            None,
                            win32con.OPEN_EXISTING,
                            win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED,
                            None)
                        win32file.ReadDirectoryChangesW(hDir,
                                                        buffer,
                                                        True,
                                                        win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                                                        win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                                                        overlapped)

                        break
                    else:
                        f_log.LOGW(f'{self.path_to_watch} not exist')
                        # if self.server_state != MessageCode.M_ERROR_MONITOR_PATH_NO_EXIST:
                        #     self.alarm_func(MessageCode.M_ERROR_MONITOR_PATH_NO_EXIST, '无法读取X光图像路径')
                        time.sleep(1)

        f_log.LOGW("monitor_picture exit++++++++++++")
