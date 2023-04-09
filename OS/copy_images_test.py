import os
import shutil
import sys
import threading

import win32con
import win32file
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, QMessageBox


def parse_file_name(copied, modelWhere, allOrOne, v_num_input, target_detail):
    v_num_list = v_num_input.split(',')
    v_num = copied[int(copied.find('V')) + 1:int(copied.find('I'))]
    if os.path.exists(copied) and v_num in v_num_list:
        if not os.path.exists(target_detail):
            os.makedirs(target_detail)
        (filepath, tempFilename) = os.path.split(copied)
        target_detail_path = os.path.join(target_detail, tempFilename)
        if modelWhere == '本地':
            if allOrOne == '一张':
                v_num_v = 'V' + str(v_num)
                download_image = os.listdir(target_detail)
                for images in download_image:
                    if v_num_v in images:
                        return
            shutil.move(copied, target_detail_path)
            print('from', copied, 'move to', target_detail_path)
        else:
            shutil.copy(copied, target_detail_path)
            print('from', copied, 'copy to', target_detail_path)


def creat_file(filename, target, path_to_watch, pic_num, modelWhere, allOrOne, v_num_input):
    wheel_type = filename[int(filename.find('N')):int(filename.find('R'))]
    batch_num = filename[int(filename.find('P')):int(filename.find('W'))]
    target_path = target + '/' + wheel_type
    target_detail = target + '/' + wheel_type + '/' + batch_num
    full_filename = os.path.join(path_to_watch, filename)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if not os.path.exists(target_detail) and len(os.listdir(target_path)) <= int(pic_num):
        os.makedirs(target_detail)
    if len(os.listdir(target_path)) > int(pic_num):
        if os.path.isdir(target_detail):
            try:
                os.rmdir(target_detail)
            except OSError as err:
                print(err)
        return
    parse_file_name(full_filename, modelWhere, allOrOne, v_num_input, target_detail)


def monitor_dir(path_to_watch, target, modelWhere, pic_num, allOrOne, v_num_input, wheel_type_list):
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

        wheel_type_list_detail = wheel_type_list.split(',')
        for wheel_type in wheel_type_list_detail:
            for action, filename in results:
                if ACTIONS.get(action, "Unknown") == 'Created':
                    if wheel_type != '' and wheel_type not in filename:
                        continue
                thread = threading.Thread(target=creat_file, args=(filename, target, path_to_watch, pic_num, modelWhere,
                                                                   allOrOne, v_num_input))
                thread.start()
                thread.join()


def local_file(path_to_watch, target, modelWhere, pic_num, allOrOne, v_num_input, wheel_type_list):
    fileList = os.listdir(path_to_watch)
    wheel_type_list_detail = wheel_type_list.split(',')
    for wheel_type in wheel_type_list_detail:
        for filename in fileList:
            if wheel_type != '' and wheel_type not in filename:
                continue
            thread = threading.Thread(target=creat_file,
                                      args=(
                                          filename, target, path_to_watch, pic_num, modelWhere, allOrOne, v_num_input))
            thread.start()
            thread.join()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(730, 300, 500, 450)
        self.setWindowTitle('复制文件小工具')

        self.btn = QPushButton('请选择复制地址', self)
        self.btn.setGeometry(QRect(70, 70, 111, 30))
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(190, 70, 221, 30))
        self.lineEdit.setFont(QFont('Arial', 14))

        self.btn_1 = QPushButton('请选择保存地址', self)
        self.btn_1.setGeometry(QRect(70, 110, 111, 30))
        self.lineEdit_btn = QLineEdit(self)
        self.lineEdit_btn.setGeometry(QRect(190, 110, 221, 30))
        self.lineEdit_btn.setFont(QFont('Arial', 14))

        self.label1 = QLabel('产线/本地', self)
        self.label1.setGeometry(QRect(70, 150, 160, 30))
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setGeometry(QRect(190, 150, 221, 30))
        self.lineEdit_1.setFont(QFont('Arial', 14))

        self.label2 = QLabel('请输入复制数量', self)
        self.label2.setGeometry(QRect(70, 190, 221, 30))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QRect(190, 190, 221, 30))
        self.lineEdit_2.setFont(QFont('Arial', 14))

        self.label3 = QLabel('全部/一张', self)
        self.label3.setGeometry(QRect(70, 230, 145, 30))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QRect(190, 230, 221, 30))
        self.lineEdit_3.setFont(QFont('Arial', 14))

        self.label4 = QLabel('请输入保存步数', self)
        self.label4.setGeometry(QRect(70, 270, 145, 30))
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QRect(190, 270, 221, 30))
        self.lineEdit_4.setFont(QFont('Arial', 14))

        self.label5 = QLabel('请输入所需型号', self)
        self.label5.setGeometry(QRect(70, 310, 145, 30))
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setGeometry(QRect(190, 310, 221, 30))
        self.lineEdit_5.setFont(QFont('Arial', 14))

        self.btn_2 = QPushButton('确定', self)
        self.btn_2.setGeometry(QRect(190, 350, 111, 30))

        self.btn.clicked.connect(self.openFile)
        self.btn_1.clicked.connect(self.saveFile)
        self.btn_2.clicked.connect(self.copyImages)

        self.show()

    def openFile(self):
        directory = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "D://")
        if directory:
            self.lineEdit.setText(directory)

    def saveFile(self):
        directory = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "D://")
        if directory:
            self.lineEdit_btn.setText(directory)

    def copyImages(self):
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit_btn.text()) == 0 or len(self.lineEdit_1.text()) == 0 \
                or len(self.lineEdit_2.text()) == 0 or len(self.lineEdit_3.text()) == 0:
            QMessageBox.warning(self, '警告', '请填写所有的内容', QMessageBox.Cancel, QMessageBox.Cancel)
        elif (self.lineEdit_1.text() not in ['产线', '本地']) or (self.lineEdit_3.text() not in ['全部', '一张']):
            QMessageBox.warning(self, '警告', '请填写正确的内容', QMessageBox.Cancel, QMessageBox.Cancel)
        else:
            if self.lineEdit_1.text() == '本地':
                threading.Thread(target=local_file,
                                 args=(self.lineEdit.text(), self.lineEdit_btn.text(),
                                       self.lineEdit_1.text(), self.lineEdit_2.text(),
                                       self.lineEdit_3.text(), self.lineEdit_4.text(),
                                       self.lineEdit_5.text())).start()
            else:
                threading.Thread(target=monitor_dir,
                                 args=(self.lineEdit.text(), self.lineEdit_btn.text(),
                                       self.lineEdit_1.text(), self.lineEdit_2.text(),
                                       self.lineEdit_3.text(), self.lineEdit_4.text(),
                                       self.lineEdit_5.text())).start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
