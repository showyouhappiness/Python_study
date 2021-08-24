from PIL import Image
import cv2

file_path = r'E:\result_images5\2021-08-18\NG\006987\D01_2108171846528_006987_Lef_0_result.jpg'

img = Image.open(file_path)
imgSize = img.size  # 大小/尺寸
w = img.width  # 图片的宽
h = img.height  # 图片的高
f = img.format  # 图像格式

img = cv2.imread(file_path)  # 读取图片信息

sp = img.shape[0:2]  # 截取长宽啊
sp1 = img.shape  # [高|宽|像素值由三种原色构成]
print(sp, sp1)
