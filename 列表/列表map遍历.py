array = ['abced', 'fghi', 'qwert', 'plmkij', 'majiangboqqqq']


def hasStr(str):
    return str.find('majiangbo') != -1


print(list(map(hasStr, array)).count(bool(True)))
print(list(map(hasStr, array)))

str = 'majiangbo'

for i in array:
    if str in i:
        print(True)
    else:
        print(False)

# python 2  返回列表
print(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) # [1, 4, 9, 16, 25]
print(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) # 列表推导式
# python 3 返回迭代器
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))) # [1, 4, 9, 16, 25]
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))) # 可以接受多个参数

print(list(map(lambda x: x * x / 100, [1, 2, 3, 4, 5])))
total_used = sum(map(lambda x: x * x / 100, [1, 2, 3, 4, 5]))
print(total_used)