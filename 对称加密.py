"""
AES（对称）加密和解密
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

passWord = "用户密码"
key = 'aes_keysaes_keysaes_keys'
mode = AES.MODE_OFB
"""
通过 AES 的 new() 方法实例化一个对象 cryptor 
new() 的第一个参数 key 是加密和解密时使用的秘钥，长度是有限制的，一般为16, 24, 32。
第二个参数是 AES 中的一个 mode 对象，可以是 MODE_ECB,  MODE_CBC, MODE_CFB, MODE_OFB等，不同的值有不同含义，用法也有差异
后面还可以接其他参数或关键字参数，如上面的第三个参数。
"""
cryptor = AES.new(key.encode('utf-8'), mode, b'0000000000000000')
# 对要加密的信息先进行处理，如上面 mode 为 MODE_OFB 时，信息长度要处理成16的倍数。
length = 16
count = len(passWord)
if count % length != 0:
    add = length - (count % length)
else:
    add = 0

passWord = passWord + ('\0' * add)
ciphertext = cryptor.encrypt(passWord.encode('utf-8'))  # 加密时，使用 cryptor 的 encrypt() 方法对信息进行加密
result = b2a_hex(ciphertext)  # 使用 binascii 中的 b2a_hex() 对加密结果进行16进制处理
print(result.decode('utf-8'))

cryptor = AES.new(key.encode('utf-8'), mode, b'0000000000000000')  # 解密时，使用相同的 key 作为秘钥， 使用相同的 mode ，
plain_text = cryptor.decrypt(a2b_hex(result))  # 使用 cryptor 的 decrypt() 方法解密，先用 a2b_hex() 对密文进行16进制处理，解密结果与加密前相同。
print(plain_text.decode('utf-8').rstrip('\0'))
