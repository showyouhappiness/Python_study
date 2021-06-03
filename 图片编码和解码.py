import numpy as np
import urllib
import cv2


class encode:
    img = cv2.imread('ceshi.bmp')
    print(type(img))
    # '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
    img_encode = cv2.imencode('.bmp', img)[1]
    # imgg = cv2.imencode('.png', img)
    print(type(img_encode))
    data_encode = np.array(img_encode)  # 创建一个数组
    print(type(data_encode))
    str_encode = data_encode.tobytes()
    print(type(str_encode))

    # 缓存数据保存到本地，以txt格式保存
    with open('img_encode.txt', 'wb') as f:
        f.write(str_encode)
        f.flush()

    with open('img_encode.txt', 'rb') as f:
        str_encode = f.read()
        f.tell()

    nparr = np.frombuffer(str_encode, np.uint8)
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("img_decode", img_decode)
    cv2.waitKey()


if __name__ == '__main__':
    encode = encode
