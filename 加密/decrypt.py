import base64
import os
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import json

address = r'E:\test'
file_name = r'E:\result_images4'
AES_key = 'cai_cai_mi_ma_shi_shen_me'
# AES_key = 'aes_keysaes_keysaes_keys'
mode = AES.MODE_OFB


def get_images(address):
    # encrypt_path = address + '\\encrypt\\'
    image_list = os.listdir(address)
    for detail_image in image_list:
        detail_path = address + '/' + detail_image
        with open(detail_path, 'rb') as f:
            image_byte = f.read()
            # image_byte = base64.b64encode(f.read().strip()).decode('hex')
            # image_byte = base64.b64encode(f.read()).decode('utf-8')
            result = Aes_decrypt(image_byte)
        decrypt_path = address + '\\decrypt\\'
        if not os.path.exists(decrypt_path):
            os.makedirs(decrypt_path)
        target_detail = decrypt_path + '/' + detail_image
        with open(target_detail, 'wb') as f:
            f.write(result)


unpad = lambda date: date[0:-ord(date[-1])]


def Aes_decrypt(decrData):  # 解密函数
    aes = AES.new(AES_key.encode("utf-8"), AES.MODE_ECB)  # 初始化AES,ECB模式的实例
    res = a2b_hex(decrData)
    msg = aes.decrypt(res).decode("utf8")
    return unpad(msg)


get_images(address)
