string = "Hello Python"
print(list(string))
for char in string:
    print(char)

# 字符串的常用操作------------------------------------------


hello_str = "Hello Hello"

# 统计字符串长度
print(len(hello_str))

# 统计某一个小字符串出现的次数
print(hello_str.count("llo"))

# 某一个子字符串出现的位置
print(hello_str.index("llo"))

num_str = '0123456789'
# string反转
print(num_str[-1::-1])
print(num_str[::-1])
