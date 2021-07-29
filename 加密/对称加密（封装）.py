"""
AES（对称）加密和解密
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import json

address = r'C:\.crf-config.json'
file_name = r'C:\.crf-config'
AES_key = 'aes_keysaes_keysaes_keys'
mode = AES.MODE_OFB
"""
通过 AES 的 new() 方法实例化一个对象 cryptor 
new() 的第一个参数 key 是加密和解密时使用的秘钥，长度是有限制的，一般为16, 24, 32。
第二个参数是 AES 中的一个 mode 对象，可以是 MODE_ECB,  MODE_CBC, MODE_CFB, MODE_OFB等，不同的值有不同含义，用法也有差异
后面还可以接其他参数或关键字参数，如上面的第三个参数。
"""


def Aes_encrypt(s):
    """
    AES 加密
    """
    cryptor = AES.new(AES_key.encode('utf-8'), mode, b'0000000000000000')
    length = 16
    count = len(s)
    if count % length != 0:
        add = length - (count % length)
    else:
        add = 0
    passWord = s + ('\0' * add)
    ciphertext = cryptor.encrypt(passWord.encode('utf-8'))
    result = b2a_hex(ciphertext)
    en_result = result.decode('utf-8')
    return result


def Aes_decrypt(s):
    """
    AES 解密
    """
    cryptor = AES.new(AES_key.encode('utf-8'), mode, b'0000000000000000')
    plain_text = cryptor.decrypt(a2b_hex(s))
    de_result = plain_text.decode('utf-8').rstrip('\0')
    return de_result


with open(address, 'r') as f:
    message = f.read()
encrypt_result = Aes_encrypt(message).decode('utf-8')
with open(file_name, 'w') as f:
    f.write(encrypt_result)

with open(file_name, 'rb') as f:
    read_result = f.read()
    config = json.loads(Aes_decrypt(read_result))
print(config)
