"""
增加字典项
"""
book = {}
book['书名'] = '《三体》'
book['价格'] = '20'
book['作者'] = '刘慈欣'
book['出版社'] = '***出版社'
print(book)
print('-' * 50)
"""
修改字典项
"""
book['出版社'] = '****出版社'
print(book)
print('-' * 50)

"""
查询字典项
"""
value = book.get('书名')
print(value)

value = book['书名']
print(value)

value = book.get('书名1')
print(value)

value = book.get('书名1', '默认')  # 可以设置默认值
print(value)

# value = book['书名1']  # 找不到会报错
# print(value)

print('-' * 50)

"""
字典遍历
"""
# 如果使用for in直接遍历字典，取出的是字典的key
for i in book:
    print(i)

# 获取字典中的所有value
print(book.values())
for v in book.values():
    print(v)

# 获取字典中的所有key
print(book.keys())
for k in book.keys():
    print(k)

# 获取字典中的所有组items
print(book.items())
for item in book.items():
    print(item)

for k, v in book.items():
    print(k, v)

print('-' * 50)
"""
删除字典项
删除字典里面每一项的一个key，可以通过for in 循环，然后对每一个进行删除
books[''] = ''
"""
book.pop('出版社')
print(book)
book.popitem()
print(book)
del book['价格']  # 类似pop(key)
print(book)
book.clear()
print(book)
