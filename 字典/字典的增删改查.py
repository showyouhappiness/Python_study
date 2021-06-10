"""
增加字典项
"""
book = {}
book['书名'] = '《三体》'
book['价格'] = '20'
book['作者'] = '刘慈欣'
book['出版社'] = '***出版社'
print(book)

"""
修改字典项
"""
book['出版社'] = '****出版社'
print(book)

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
