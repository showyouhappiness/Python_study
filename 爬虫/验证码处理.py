import time
from PIL import Image
import pytesseract
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
image_url = 'https://so.gushiwen.org/RandCode.ashx'
# 下载验证码图片
session = requests.Session()  # 使用session是为了保证验证码的请求和登陆请求信息一致

for i in range(10):
    r = session.get(image_url, headers=headers)

    with open('E:/result_images/' + str(i) + '.jpg', 'wb') as fp:
        fp.write(r.content)
    time.sleep(3)
    print('下载完成第' + str(i) + '张！')


# 依次识别并保存到文件中

# 进行二值处理
def erzhihua(image, threshold):
    ''':type image:Image.Image'''
    image = image.convert('L')
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return image.point(table, '1')


# 对刚才保存的10张图片进行识别
for i in range(10):
    im = Image.open('E:/result_images/' + str(i) + '.jpg')
    im = erzhihua(im, 127)
    im.show()
    result = pytesseract.image_to_string(im, lang='eng')

    print(result)
