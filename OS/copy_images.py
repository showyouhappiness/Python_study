import sys
import os
import time

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, QMessageBox
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont

import threading
import win32file
import win32con


def parse_file_name(copied, target, modelWhere, pic_num, allOrOne):
    if os.path.exists(copied):
        (filepath, tempFilename) = os.path.split(copied)
        wheel_type = tempFilename[int(tempFilename.find('N')):int(tempFilename.find('R'))]
        target_detail = target + '/' + wheel_type
        if not os.path.exists(target_detail):
            os.makedirs(target_detail)
        if len(os.listdir(target_detail)) > int(pic_num) - 1:
            return
        time.sleep(1)
        if allOrOne == '全部':
            with open(copied, 'rb') as readStream:
                container_master = readStream.read()
                target_detail_path = os.path.join(target_detail, tempFilename)
                with open(target_detail_path, 'wb') as writeStream:
                    writeStream.write(container_master)
            if modelWhere == '本地':
                time.sleep(0.5)
                os.remove(copied)
        else:
            if 'I1A' in tempFilename:
                with open(copied, 'rb') as readStream:
                    container_master = readStream.read()
                    target_detail_path = os.path.join(target_detail, tempFilename)
                    with open(target_detail_path, 'wb') as writeStream:
                        writeStream.write(container_master)
                    if modelWhere == '本地':
                        time.sleep(1)
                        os.remove(copied)


def monitor_dir(path_to_watch, target, modelWhere, pic_num, allOrOne):
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
            print(full_filename, ACTIONS.get(action, "Unknown"))
            # parse_file_name(full_filename, target, modelWhere, pic_num, allOrOne)
            threading.Thread(target=parse_file_name,
                             args=(full_filename, target, modelWhere, pic_num, allOrOne)).start()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 370)
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

        self.label2 = QLabel('请输入保存总数', self)
        self.label2.setGeometry(QRect(70, 190, 221, 30))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QRect(190, 190, 221, 30))
        self.lineEdit_2.setFont(QFont('Arial', 14))

        self.label3 = QLabel('全部/一张', self)
        self.label3.setGeometry(QRect(70, 230, 145, 30))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QRect(190, 230, 221, 30))
        self.lineEdit_3.setFont(QFont('Arial', 14))

        self.btn_2 = QPushButton('确定', self)
        self.btn_2.setGeometry(QRect(190, 270, 111, 30))

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
        else:
            threading.Thread(target=monitor_dir, args=(self.lineEdit.text(), self.lineEdit_btn.text(),
                                                       self.lineEdit_1.text(), self.lineEdit_2.text(),
                                                       self.lineEdit_3.text())).start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
