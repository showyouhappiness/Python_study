import cv2
import os

img = cv2.imread('D:\\images_crf\\23.08.52P348573W20V6I6A0SM0N00316c09R1E0Otunde.jpg', 1)
path = 'D:\\images_crf1'
cv2.imwrite(os.path.join(path, 'waka.jpg'), img)
cv2.waitKey(0)
