"""
AES（对称）加密和解密
"""
import os

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from minio.sse import SseCustomerKey

address = r'E:\test'
result_name = r'E:\result_images5'
AES_key = 'cai_cai_mi_ma_shi_shen_me'
key = AES_key.encode()
ssec = SseCustomerKey(key)
mode = AES.MODE_OFB

key = AES_key.encode("utf-8")  # 初始化密钥
length = AES.block_size  # 初始化数据块大小
aes = AES.new(key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
# 截断函数，去除填充的字符
unpad = lambda date: date[0:-ord(date[-1])]


def pad(text):
    """
    #填充函数，使被加密数据的字节码长度是block_size的整数倍
    """
    count = len(text)
    if count % length != 0:
        add = length - (count % length)
    else:
        add = 0
    entext = text + ('\0' * add)
    return entext


def Aes_encrypt(encrData):
    res = aes.encrypt(pad(encrData))
    msg = b2a_hex(res)
    return msg


def Aes_decrypt(decrData):
    res = a2b_hex(decrData)
    msg = aes.decrypt(res).decode("utf8")
    return unpad(msg)


def encrypt(address):
    image_list = os.listdir(address)
    for detail_image in image_list:
        detail_path = address + '/' + detail_image
        with open(detail_path, 'r') as f:
            image_byte = f.read()
        encrypt_result = Aes_encrypt(image_byte).decode('utf-8')

        if not os.path.exists(result_name):
            os.makedirs(result_name)
        target_detail = result_name + '/' + detail_image
        with open(target_detail, 'w') as f:
            f.write(encrypt_result)


encrypt(address)
