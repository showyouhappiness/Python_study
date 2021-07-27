import base64
import psycopg2
from Crypto.PublicKey import RSA
from Crypto import Random  # 先导入 Random ，实例化一个随机生成值的对象，所以我们每次运行的结果不一样，因为初始值是随机生成的。
from Crypto.Cipher import PKCS1_v1_5  # 用于加密

rsa = RSA.generate(1024)  # 也可以使用伪随机数来辅助生成

# 生成私钥
private_key = rsa.export_key()
with open("private_a.rsa", 'wb') as f:
    f.write(private_key)  # 将私钥写入文件中，使用时从文件中读取出来

# 生成公钥
public_key = rsa.publickey().export_key()
with open("public_a.rsa", 'wb') as f:
    f.write(public_key)  # 将公钥写入文件中，使用时从文件中读取出来
print(public_key)
print(private_key)

def encrypt_with_rsa(plain_text):
    # 先公钥加密
    with open("public_a.rsa") as f:
        key = f.read()
        pub_key = RSA.importKey(str(key))
        print("pub_key")
        print(pub_key)
        print("===========")
        cipher_pub_obj = PKCS1_v1_5.new(pub_key)
        _secret_byte_obj = base64.b64encode(cipher_pub_obj.encrypt(bytes(plain_text.encode("utf-8")))).decode('utf-8')
        return _secret_byte_obj


def query(self, query, parameters=None):
    try:
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
    except psycopg2.Error as e:
        self.connection.rollback()
        return e
    else:
        self.connection.commit()


# def decrypt_with_rsa(_secret_byte_obj):
#     # 后私钥解密
#     with open("private_a.rsa") as f:
#         key = f.read()
#         pri_key = RSA.importKey(key)
#         cipher_pri_obj = PKCS1_v1_5.new(pri_key)
#         plain_text = cipher_pri_obj.decrypt(base64.b64decode(_secret_byte_obj), 0).decode('utf-8')
#         print(plain_text)
#         return plain_text


def executer_without_signature():
    # 加解密验证
    text = "用户密码"
    Encrypted = encrypt_with_rsa(text)
    print(Encrypted)
    # assert text == decrypt_with_rsa(Encrypted)
    print("rsa test success！")


if __name__ == '__main__':
    executer_without_signature()
