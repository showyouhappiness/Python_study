import os
import shutil
import sys
import threading

import win32con
import win32file
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, QMessageBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(730, 300, 500, 280)
        self.setWindowTitle('复制文件小工具')

        self.label1 = QLabel('请输入X光机号', self)
        self.label1.setGeometry(QRect(70, 10, 160, 30))
        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.setGeometry(QRect(190, 10, 221, 30))
        self.lineEdit_1.setFont(QFont('Arial', 14))

        self.label2 = QLabel('请输入判别类型', self)
        self.label2.setGeometry(QRect(70, 50, 221, 30))
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QRect(190, 50, 221, 30))
        self.lineEdit_2.setFont(QFont('Arial', 14))

        self.label3 = QLabel('请输入时间', self)
        self.label3.setGeometry(QRect(70, 90, 145, 30))
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QRect(190, 90, 221, 30))
        self.lineEdit_3.setFont(QFont('Arial', 14))

        self.label4 = QLabel('请输入复制数量', self)
        self.label4.setGeometry(QRect(70, 130, 145, 30))
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QRect(190, 130, 221, 30))
        self.lineEdit_4.setFont(QFont('Arial', 14))

        self.label5 = QLabel('请输入所需型号', self)
        self.label5.setGeometry(QRect(70, 170, 145, 30))
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setGeometry(QRect(190, 170, 221, 30))
        self.lineEdit_5.setFont(QFont('Arial', 14))

        self.btn_2 = QPushButton('确定', self)
        self.btn_2.setGeometry(QRect(190, 210, 111, 30))

        self.btn_2.clicked.connect(self.copyImages)

        self.show()

    def openFile(self):
        pass

    def saveFile(self):
        pass

    def copyImages(self):
        if len(self.lineEdit_1.text()) == 0 or len(self.lineEdit_2.text()) == 0 or len(self.lineEdit_3.text()) == 0 \
                or (len(self.lineEdit_4.text()) == 0 and len(self.lineEdit_5.text()) == 0):
            QMessageBox.warning(self, '警告', '请按照要求填写所需内容', QMessageBox.Cancel, QMessageBox.Cancel)
        else:
            if ',' in self.lineEdit_1.text():
                device_number_list = self.splice_content(self.lineEdit_1.text())
            else:
                device_number_list = list(self.lineEdit_1.text())

            if ',' in self.lineEdit_2.text():
                detect_type_list = self.splice_content(self.lineEdit_2.text())
            else:
                detect_type_list = list(self.lineEdit_2.text())

            if ',' in self.lineEdit_3.text():
                date_time_list = self.splice_content(self.lineEdit_3.text())
            else:
                date_time_list = list(self.lineEdit_3.text())

            if ',' in self.lineEdit_5.text():
                knuckle_type_list = self.splice_content(self.lineEdit_5.text())
            else:
                knuckle_type_list = list(self.lineEdit_5.text())

            print(device_number_list,detect_type_list,date_time_list,knuckle_type_list)

            for device_number in device_number_list:
                for detect_type in detect_type_list:
                    for date_time in date_time_list:
                        for knuckle_type in knuckle_type_list:
                            print(device_number, detect_type, date_time, knuckle_type)

    def splice_content(self, text):
        content_list = text.split(',')
        return content_list

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
