import datetime
import os
import time
import traceback
import pywintypes
import win32con
import win32event
import win32file
from queue import Queue

from grpc_server.module import type_define
from OS.log import f_log


def monitor_picture(path_to_watch):
    ACTIONS = {
        1: "Created",
        2: "Deleted",
        3: "Updated",
        4: "Renamed from something",
        5: "Renamed to something"
    }
    monitor_thread_exit_flag = False
    file_queue_first_x_ray = Queue()
    FILE_LIST_DIRECTORY = 0x0001
    f_log.LOGW("monitor_picture path_to_watch=%s", path_to_watch)

    while True:
        if os.path.exists(path_to_watch):
            f_log.LOGW('{} exist'.format(path_to_watch))
            break
        else:
            f_log.LOGW('{} not exist'.format(path_to_watch))
            time.sleep(1)

    hDir = win32file.CreateFile(
        path_to_watch,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS | win32con.FILE_FLAG_OVERLAPPED,
        None)

    overlapped = pywintypes.OVERLAPPED()
    overlapped.hEvent = win32event.CreateEvent(None, 0, 0, None)
    buffer = win32file.AllocateReadBuffer(1024 * 64)

    firstupdated_file = ''
    updatetimes = 0

    win32file.ReadDirectoryChangesW(hDir,
                                    buffer,
                                    True,
                                    win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                                    win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                                    overlapped)

    while monitor_thread_exit_flag is False:
        f_log.LOGI("monitor_picture start +++++++++++++++++++++++++++++")
        try:
            ret = win32event.WaitForSingleObject(overlapped.hEvent, 5000)

            if ret == win32event.WAIT_OBJECT_0:
                nbytes = win32file.GetOverlappedResult(hDir, overlapped, True)
                f_log.LOGI("XXXXXXXSSSSSS= nbytes %d", nbytes)
                if nbytes > 0:
                    for action, file in win32file.FILE_NOTIFY_INFORMATION(buffer, nbytes):
                        if ACTIONS.get(action, "Unknown") == r'Updated':
                            full_filename = os.path.join(path_to_watch, file)
                            _, extension = os.path.splitext(full_filename)
                            if not os.path.isfile(full_filename) or os.path.splitext(full_filename)[1] == '.db':
                                continue

                            if extension != '.jpg' and extension != '.bmp' and extension != '.png':
                                continue

                            if file.find('_color') >= 0 or \
                                    file.find('calibrationstepwedge') >= 0 or \
                                    file.find('calibrationsstpwedge') >= 0 or \
                                    file.find('test') > 0:
                                continue

                            if firstupdated_file == full_filename:
                                updatetimes = updatetimes + 1
                                f_log.LOGI("monitor_picture (" + firstupdated_file + ") updated " + str(
                                    updatetimes) + "times")
                            else:
                                updatetimes = 1
                                firstupdated_file = full_filename
                                file_queue_first_x_ray.put(type_define.MonitorImageData(
                                    file_name=firstupdated_file,
                                    monitor_time=datetime.datetime.now(),
                                    file_create_time=datetime.datetime.fromtimestamp(os.path.getctime(
                                        firstupdated_file)),
                                    file_modify_time=datetime.datetime.fromtimestamp(os.path.getmtime(
                                        firstupdated_file)),
                                    file_access_time=datetime.datetime.fromtimestamp(os.path.getatime(
                                        firstupdated_file))
                                ))
                                f_log.LOGW("update file {} queue size = {}".format(
                                    firstupdated_file, file_queue_first_x_ray.qsize()))

                win32file.ReadDirectoryChangesW(hDir,
                                                buffer,
                                                True,
                                                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                                                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE,
                                                overlapped)
            else:
                f_log.LOGI("monitor_picture timeout ++++++++++++++++++++++")
        except Exception as e:
            f_log.LOGW("Exception: {}".format(e))
            f_log.LOGW("{}".format(traceback.format_exc()))
            while True:
                if os.path.exists(path_to_watch):
                    f_log.LOGW('{} exist'.format(path_to_watch))
                    break
                else:
                    f_log.LOGW('{} not exist'.format(path_to_watch))

            hDir = win32file.CreateFile(
                path_to_watch,
                FILE_LIST_DIRECTORY,
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
        if not os.path.exists(path_to_watch):
            f_log.LOGW('{} not exist'.format(path_to_watch))
            while True:
                if os.path.exists(path_to_watch):
                    f_log.LOGW('{} exist'.format(path_to_watch))
                    hDir = win32file.CreateFile(
                        path_to_watch,
                        FILE_LIST_DIRECTORY,
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
                    f_log.LOGW('{} not exist'.format(path_to_watch))
                    time.sleep(1)

    f_log.LOGW("monitor_picture exit++++++++++++")


if __name__ == '__main__':
    path_to_watch = r'Z:\\test'
    monitor_picture(path_to_watch)
