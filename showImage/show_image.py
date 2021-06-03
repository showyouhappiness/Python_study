import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5 import QtGui
from show_image_widget import Ui_MainWindow
import cv2


class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.selectPic.clicked.connect(self.openimage)
        self.pic_show_label = QLabel()
        # 设置窗口尺寸
        self.pic_show_label.resize(500, 500)

    def openimage(self):
        # imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        # print(imgName)
        # jpg = QtGui.QPixmap(imgName).scaled(self.showImage.width(), self.showImage.height())
        #
        # self.showImage.setPixmap(jpg)

        # 设置展示控件

        # 通过cv读取图片
        img = cv2.imread("../yucun.gif")
        # 通道转化
        RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 将图片转化成Qt可读格式
        image = QtGui.QImage(RGBImg, RGBImg.shape[1], RGBImg.shape[0], QtGui.QImage.FormatRGB888)

        # 加载图片,并自定义图片展示尺寸
        image = QtGui.QPixmap(image).scaled(400, 400)
        # 显示图片
        self.pic_show_label.setPixmap(image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyClass()
    myWin.show()
    sys.exit(app.exec_())
