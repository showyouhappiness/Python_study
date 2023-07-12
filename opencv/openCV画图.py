import os
import cv2

if __name__ == '__main__':
    imgPath = r"./yucun.gif"
    img = cv2.imread(imgPath)
    xmin = 100
    xmax = 200
    ymin = 100
    ymax = 300
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
    cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (255, 0, 0), 2)
    cv2.imshow('src', img)
    cv2.waitKey()
