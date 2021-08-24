import requests

# GET请求
r = requests.get('http://httpbin.org/get')
print(r.status_code, r.reason)
print(r.text)
print('*' * 50)

# 带参数的GET请求
r = requests.get('http://httpbin.org/get', params={'a': '1', 'b': '2'})
print(r.json())
print('*' * 50)

# POST请求
r = requests.post('http://httpbin.org/post', params={'a': '1', 'b': '2'})
print(r.json())
print('*' * 50)

# 自定义headers请求
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/89.0.4389.90 Safari/537.36 '
# }
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/89.0.4389.90 Safari/537.36 '
headers = {'User-Agent': ua}
req = requests.get('http://httpbin.org/headers', headers=headers)
print('自定义headers请求', r.json())
print('*' * 50)

# 待cookies的请求
cookies = dict(userid='123456', token='!Q@W#E$R%T12345qwert')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print('带cookies的请求', r.json())
print('*' * 50)

# Basic-auth认证请求
r = requests.get('http://httpbin.org/basic-auth/hello/123456', auth=('hello', '123456'))
print('Basic-auth认证请求', r.json())
print('*' * 50)

# 主动跑出状态码异常
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# bad_r.raise_for_status()
print('*' * 50)

# 使用requests.Session对象请求
# 创建一个Session对象
s = requests.Session()
# Session对象会保存服务器返回的set-cookies头信息里面的内容
s.get('http://httpbin.org/cookies/set/userid/123456789')
s.get('http://httpbin.org/cookies/set/token/qwertyuiop')
# 下一次请求会将本地所有的cookies信息自动添加到请求头信息里面
r = s.get('http://httpbin.org/cookies')
print('检查session中的cookies', r.json())
print('*' * 50)

# 设置超时
r = requests.get('http://httpbin.org/delay/4', timeout=5)
print(r.text)
# 如果为5s或者超过5s，就报错
# r1 = requests.get('http://httpbin.org/delay/5', timeout=5)
# print(r1.text)
print('*' * 50)

# 在requests中使用代理
print('不使用代理：', requests.get('http://httpbin.org/ip').json())
print('使用代理：', requests.get(
    'http://httpbin.org/ip',
    proxies={'http': 'http://172.16.1.75:9000'}
).json())

