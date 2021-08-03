from Crypto.Cipher import AES
import requests
import os
import base64
r = requests.get('https://comic.hangxianglx.cn/qualityFifty/9ed74f6d6dc83ef5152/71ed0e1afbcc37978.jpg',timeout = (2,2))
viChapter = "958DB2E92B361F373BFB35CCCC296FBB"
keyChapter = "C2A830A5E687678418F88F652984E925"
# 16进制转二进制
viChapter = bytes.fromhex(viChapter)
keyChapter = bytes.fromhex(keyChapter)
cipher = AES.new(keyChapter, AES.MODE_CBC, viChapter)
text_decrypted = cipher.decrypt(r.content)
print(text_decrypted)
b64_byt = base64.b64encode(text_decrypted)
print(b64_byt)
if not os.path.exists('./' + "4" + '/'): # 判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs('./' + "4" + '/') # makedirs 创建文件时如果路径不存在会创建这个路径
with open('./' + "4" + '/' + str(3) + '.jpg', 'wb') as file:
    file.write(text_decrypted)