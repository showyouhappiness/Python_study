import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinUIform(QMainWindow):

    def __init__(self, parent=None):
        super(WinUIform, self).__init__(parent)

        self.setWindowTitle('表格测试')
        self.resize(530, 350)

        self.table = QTableWidget(10, 3)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(5):
            for j in range(2):
                col = QTableWidgetItem("{}{}col".format(i, j))
                self.table.setItem(i, j, col)

            deleteButton = QPushButton("{} 删除".format(i))
            deleteButton.clicked.connect(self.delete_clicked)
            self.table.setCellWidget(i, 2, deleteButton)

        self.setCentralWidget(self.table)

    def delete_clicked(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            self.table.removeRow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 下面两种方法都可以
    win = WinUIform()
    # win = Winform()
    win.show()
    sys.exit(app.exec_())
