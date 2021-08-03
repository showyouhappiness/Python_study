"""
AES（对称）加密和解密
"""
import os

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

address = r'E:\result_images3'
file_name = r'E:\result_images4'
result_name = r'E:\result_images5'
AES_key = 'aes_keysaes_keysaes_keys'
mode = AES.MODE_OFB


def Aes_encrypt(s):
    cryptor = AES.new(AES_key.encode('utf-8'), mode, b'0000000000000000')
    ciphertext = cryptor.encrypt(s)
    result = b2a_hex(ciphertext)
    en_result = result.decode('utf-8')
    return result


def Aes_decrypt(s):
    cryptor = AES.new(AES_key.encode('utf-8'), mode, b'0000000000000000')
    plain_text = cryptor.decrypt(a2b_hex(s))
    return plain_text


image_list = os.listdir(address)
for detail_image in image_list:
    detail_path = address + '/' + detail_image
    with open(detail_path, 'rb') as f:
        image_byte = f.read()
    encrypt_result = Aes_encrypt(image_byte).decode('utf-8')

    if not os.path.exists(file_name):
        os.makedirs(file_name)
    target_detail = file_name + '/' + detail_image
    with open(target_detail, 'w') as f:
        f.write(encrypt_result)

image_list = os.listdir(file_name)
for detail_image in image_list:
    detail_path = file_name + '/' + detail_image
    with open(detail_path, 'r') as f:
        read_result = f.read()
        config = Aes_decrypt(read_result)
    result_path = result_name + '/' + detail_image
    with open(result_path, 'wb') as f:
        f.write(config)
