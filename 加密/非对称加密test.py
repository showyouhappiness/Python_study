'''
非对称加密
'''
import base64
from 连接到数据库 import passwd
from Crypto import Random  # 先导入 Random ，实例化一个随机生成值的对象，所以我们每次运行的结果不一样，因为初始值是随机生成的。

"""
然后导入了 RSA ，通过 RSA 的 generate() 方法实例化一个对象 rsa 。再通过 rsa 的 exportKey() 方法和 publickey() 方法生成公钥和私钥
"""
from Crypto.PublicKey import RSA

"""
从 Crypto.Cipher 中导入 PKCS1_v1_5 ，导入时记得重命名一下，如 PKCS1_cipher ，
因为在 Crypto 的另一个模块 Crypto.Signature 中也有同名的类 PKCS1_v1_5 ，同时使用时不重命名会造成冲突。
"""
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature

random_generator = Random.new().read
"""
generate(bits, randfunc=None, e=65537) 有三个参数，在使用时需要注意。
bits 是一个字节大小的值，必须大于等于1024，通常建议写1024的倍数
randfunc 是一个随机函数，默认是 Crypto.Random.get_random_bytes ，可以自己设置，也可以保持默认。
e=65537 是公共 RSA 指数，它必须是一个正整数。FIPS 标准要求公共指数至少65537(默认)。
"""
rsa = RSA.generate(2048, random_generator)
"""
生成密钥
"""
# 生成私钥
private_key = rsa.exportKey()
with open("private_a.rsa", 'wb') as f:
    f.write(private_key)  # 将私钥写入文件中，使用时从文件中读取出来

# 生成公钥
public_key = rsa.publickey().exportKey()
with open("public_a.rsa", 'wb') as f:
    f.write(public_key)  # 将公钥写入文件中，使用时从文件中读取出来

"""
使用公钥加密和使用私钥解密
"""

# 使用公钥对用户密码进行RSA加密
password = passwd.passwd
with open("public_a.rsa") as f:
    key = f.read()
    pub_key = RSA.importKey(str(key))  # 使用 RSA 的 importKey() 方法对(从文件中读取的)公钥字符串进行处理，处理成可用的加密公钥
    cipher = PKCS1_cipher.new(pub_key)  # 实例化一个加密对象 cipher ，传入的参数是公钥
    """
    加密的信息需要先转换成字节，加密的结果也是字节，可以将结果转换成 base64 字符串。
    """
    rsa_text = base64.b64encode(cipher.encrypt(bytes(password.encode("utf-8")))).decode(
        'utf-8')  # 通过 cipher 的 encrypt() 方法对信息进行加密

# 使用私钥对内容进行RSA解密
with open("private_a.rsa") as f:
    key = f.read()
    pri_key = RSA.importKey(key)  # 使用 RSA 的 importKey() 方法对(从文件中读取的)私钥字符串进行处理，处理成可用的解密私钥
    cipher = PKCS1_cipher.new(pri_key)  # 实例化一个解密对象 cipher ，传入的参数是私钥，
    back_text = cipher.decrypt(base64.b64decode(rsa_text), 0).decode(
        'utf-8')  # 通过的 cipher 的 decrypt() 方法对信息进行解密。解密结果与加密之前保持一致

if back_text == passwd:
    print("加密成功了！！！！！！！！！")

"""
私钥生成签名和公钥验证签名
"""
# 使用私钥生成签名
with open("private_a.rsa") as f:
    key = f.read()
    pri_key = RSA.importKey(key)  # 使用 RSA 的 importKey() 方法对(从文件中读取的)私钥字符串进行处理，处理成可用的私钥用于生成签名
    signer = PKCS1_signature.new(pri_key)  # 实例化一个签名对象 signer ，传入的参数是私钥
    digest = SHA.new()  # 信息需要先转换成 sha 字符串，使用 Crypto.Hash 中的 SHA 来转换
    digest.update(password.encode("utf-8"))
    sign = signer.sign(digest)  # 通过的 signer 的 sign() 方法对信息生成签名
    signature = base64.b64encode(sign)  # 生成的签名是字节串，可以将结果转换成 base64 字符串
# 使用公钥验证签名
with open("public_a.rsa") as f:
    key = f.read()
    pub_key = RSA.importKey(str(key))  # 使用 RSA 的 importKey() 方法对(从文件中读取的)公钥字符串进行处理，处理成可用的公钥用于验证签名
    verifier = PKCS1_signature.new(pub_key)  # 实例化一个验证对象 verifier ，传入的参数是公钥
    digest = SHA.new()  # 信息需要先转换成 sha 字符串，使用 Crypto.Hash 中的 SHA 来转换
    digest.update(password.encode("utf-8"))
    # 通过的 verifier 的 verify() 方法对签名进行验证。验证结果是一个布尔值，验证成功返回 True , 不成功返回 False
