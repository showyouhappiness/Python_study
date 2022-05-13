from random import Random
from hashlib import md5


# 获取由4位随机大小写字母、数字组成的salt值
def create_salt():
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars)
    random = Random()
    for i in range(4):
        # 每次从chars中随机取一位
        salt += chars[random.randint(0, len_chars)]
    return salt


# 获取原始密码+salt的md5值
def create_md5(pwd, salt):
    md5_obj = md5()
    md5_obj.update((pwd + salt).encode(encoding='utf-8'))
    result = md5_obj.hexdigest()
    return result


# 原始密码
pwd = '20141124'
# 随机生成4位salt
salt = 'crf'
# 加密后的密码
md5 = create_md5(pwd, salt)
print('[pwd]', pwd)
print('[salt]', salt)
print('[md5]', md5)
