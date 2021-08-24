import urllib.request
import json

# 接受一个字符串作为参数
r = urllib.request.urlopen('http://httpbin.org/get')
# 读取response的内容
text = r.read()
print(text)
print('*' * 50)
# http返回状态码和msg
print(r.status, r.reason)
print('*' * 50)
r.close()
# 返回的内容是json格式，直接用load函数加载
obj = json.loads(text)
print(obj)
print('*' * 50)

# r.headers是一个HTTPMessage对象
print(r.headers)
print('*' * 50)

for k, v in r.headers._headers:
    print('%s: %s' % (k, v))
print('*' * 50)

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/89.0.4389.90 Safari/537.36 '
# 添加自定义的头信息
req = urllib.request.Request('http://httpbin.org/user-agent')
req.add_header('User-agent', ua)
# 接受一个urllib.request.Request对象作为参数
r = urllib.request.urlopen(req)
resp = json.load(r)
print("user-agent：", resp["user-agent"])
print('*' * 50)

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='httpbin.org',
                          uri='basic-auth/hello/123456',
                          user='hello',
                          passwd='123456')
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
r = urllib.request.urlopen('http://httpbin.org')
print(r.read().decode('utf-8'))
print('*' * 50)

# 使用GET方法传递参数
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 2})
url = 'http://httpbin.org/get?%s' % params
with urllib.request.urlopen(url) as f:
    print(json.load(f))
print('*' * 50)

# 使用POST方法传递参数
data = urllib.parse.urlencode({'name': 'hello_world', 'age': 18})
data = data.encode()
with urllib.request.urlopen('http://httpbin.org/post', data) as f:
    print(json.load(f))
print('*' * 50)

# 使用代理IP请求远程url
proxy_handler = urllib.request.ProxyHandler({'http': 'http://172.0.0.1:9000'})
opener = urllib.request.build_opener(proxy_handler)
r = opener.open('http://httpbin.org/ip')
print('11111111', r.read())
