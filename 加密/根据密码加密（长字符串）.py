from pyDes import des, CBC, PAD_PKCS5
import binascii

# 秘钥
KEY = 'mHAxsLYz'


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


key = '{"scrap": {"area": 8.0, "pixel": 3.6, "length": 3.0}, "minio": {"port": 9000, "ip": "172.16.1.214"}, "monitor_dir": {"xray": 1, "dir": "D:\\images_crf\\"}, "output_dir": {"dir": "D:\\output_crf"}, "jbz": {"min_jbz": "200"}, "database": {"special_schema": "ai_server_four_schema", "ip": "172.16.1.209", "default_schema": "yansheng", "db_name": "test", "port": 5433}, "grpc": {"server_id": 4, "server_ip": "192.168.1.110", "jpeg_encode_quality": 100, "port": 50057, "is_local_server": true}, "enhancement": {"nos": 1, "valid": true}, "partition": {"valid": true}, "simulate": {"is_simulate": true}, "seg": {"gap": 6, "valid": true, "shrink_list": [3, 5, 6], "low_value_percent": 0, "low_value_ceiling": 0, "high_value_percent": 0, "high_value_ceiling": 0}, "metadata_server": {"ip": "localhost", "port": 12379, "enable": false}, "language": "cn", "mode": "normal", "auto_test": true, "crf_serving": {"mip": "172.16.1.231", "mport": 18000, "ip": "172.16.1.231", "port": 18001}, "redis": {"ip": "172.16.1.208", "port": 6379}, "log": {"enable": true, "url": "http://172.16.1.212:8765/crf/log"}}'
test = des_encrypt(key)
print(test)
print(type(des_descrypt(test)))
print(des_descrypt(test))
