import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QFileDialog
from PyQt5.QtCore import QRect
import os
import shutil
from pandas import DataFrame


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(730, 250, 500, 210)
        self.button1 = QPushButton('标准图文件夹', self)
        self.button1.setGeometry(QRect(90, 10, 120, 30))
        self.button1.clicked.connect(self.select_folder1)
        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setGeometry(QRect(220, 10, 180, 30))

        self.button2 = QPushButton('筛选图文件夹', self)
        self.button2.setGeometry(QRect(90, 50, 120, 30))
        self.button2.clicked.connect(self.select_folder2)
        self.line_edit2 = QLineEdit(self)
        self.line_edit2.setGeometry(QRect(220, 50, 180, 30))

        self.button3 = QPushButton('对比结果文件夹', self)
        self.button3.setGeometry(QRect(90, 90, 120, 30))
        self.button3.clicked.connect(self.select_folder3)
        self.line_edit3 = QLineEdit(self)
        self.line_edit3.setGeometry(QRect(220, 90, 180, 30))

        self.button = QPushButton('确定', self)
        self.button.setGeometry(QRect(130, 170, 160, 30))

        self.button.clicked.connect(self.confirmButtonClicked)
        self.show()

    def select_folder1(self):
        folder_path = QFileDialog.getExistingDirectory(self)
        if folder_path:
            self.line_edit1.setText(folder_path)

    def select_folder2(self):
        folder_path = QFileDialog.getExistingDirectory(self)
        if folder_path:
            self.line_edit2.setText(folder_path)

    def select_folder3(self):
        folder_path = QFileDialog.getExistingDirectory(self)
        if folder_path:
            self.line_edit3.setText(folder_path)

    def confirmButtonClicked(self):
        standard = self.line_edit1.text()
        filter = self.line_edit2.text()
        output_folder = self.line_edit3.text()
        # 创建存储不一致图片的文件夹
        os.makedirs(os.path.join(output_folder), exist_ok=True)

        # 创建报表文件
        DataFrame(
            columns=['', '标准文件夹', '筛选文件夹', '相同个数', '不同个数', '正确率', '错误率', '筛选遗漏个数',
                     '漏比率']).to_csv(os.path.join(output_folder, 'report.csv'), encoding='utf_8_sig', index=False)

        # 调用函数
        compare_folders(standard, filter, output_folder)
        QApplication.quit()


def compare_folders(folder_A, folder_B, output_folder):
    # 遍历 A 文件夹中的所有子文件夹
    for subfolder_B in os.listdir(folder_B):
        path_B = os.path.join(folder_B, subfolder_B)
        if os.path.isdir(path_B):
            # 统计 A 文件夹中子文件夹中的图片数量
            files_B = os.listdir(path_B)
            count_B = len(files_B)
            if subfolder_B == '不确定':
                df = DataFrame({'': [subfolder_B],
                                '标准文件夹内图片个数': 0,
                                '筛选文件夹内图片个数': [count_B],
                                '相同个数': 0,
                                '筛选错误个数': 0,
                                '正确率': 0,
                                '错误率': 0,
                                '筛选遗漏个数': 0,
                                '漏比率': 0})
                df.to_csv(os.path.join(output_folder, 'report.csv'), mode='a', index=False,
                          encoding='utf_8_sig', header=False)

            # 遍历 B 文件夹中的所有子文件夹
            for subfolder_A in os.listdir(folder_A):
                if subfolder_A == subfolder_B:
                    path_A = os.path.join(folder_A, subfolder_A)
                    if os.path.isdir(path_A):
                        # 统计 B 文件夹中子文件夹中的图片数量
                        files_A = os.listdir(path_A)
                        count_A = len(files_A)

                        # 比较 A 文件夹和 B 文件夹中子文件夹中的图片
                        common_files = set(files_A).intersection(set(files_B))  # 交集
                        common_count = len(common_files)  # 相同个数
                        B_error_count = count_B - common_count  # B 文件夹中不一致的图片个数
                        B_miss_count = count_A - common_count  # b文件夹漏掉的图片个数

                        # 计算占比
                        common_ratio = common_count / count_A  # 正确率
                        B_error_ratio = B_error_count / count_A  # 错误率
                        B_miss_ratio = B_miss_count / count_A  # 漏比率

                        # 将结果写入报表
                        df = DataFrame({'': [subfolder_A],
                                        '标准文件夹内图片个数': [count_A],
                                        '筛选文件夹内图片个数': [count_B],
                                        '相同个数': [common_count],
                                        '筛选错误个数': [B_error_count],
                                        '正确率': [common_ratio],
                                        '错误率': [B_error_ratio],
                                        '筛选遗漏个数': [B_miss_count],
                                        '漏比率': [B_miss_ratio]})
                        df.to_csv(os.path.join(output_folder, 'report.csv'), mode='a', index=False,
                                  encoding='utf_8_sig', header=False)

                        # 将 B 文件夹中不一致的图片另存到新的文件夹
                        for file in files_B:
                            if file not in common_files:
                                src = os.path.join(path_B, file)
                                dst = os.path.join(output_folder, '错误', subfolder_B, file)
                                os.makedirs(os.path.dirname(dst), exist_ok=True)
                                shutil.copy2(src, dst)
                        # 将 B 文件夹中漏掉的图片另存到新的文件夹
                        for file in files_A:
                            if file not in common_files:
                                src = os.path.join(path_A, file)
                                dst = os.path.join(output_folder, '漏掉', subfolder_B, file)
                                os.makedirs(os.path.dirname(dst), exist_ok=True)
                                shutil.copy2(src, dst)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
