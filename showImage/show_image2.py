from PyQt5 import QtGui, QtWidgets
import cv2

# 设置展示控件
pic_show_label = QtWidgets.QLabel()
# 设置窗口尺寸
pic_show_label.resize(500, 500)

# 图片路径
img_path = "../study/yucun.gif"

# 通过cv读取图片
img = cv2.imread(img_path)
# 通道转化
RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 将图片转化成Qt可读格式
image = QtGui.QImage(RGBImg, RGBImg.shape[1], RGBImg.shape[0], QtGui.QImage.FormatRGB888)

# 加载图片,并自定义图片展示尺寸
image = QtGui.QPixmap(image).scaled(400, 400)
# 显示图片
pic_show_label.setPixmap(image)
