list = ['你', '好', '世', '界', '你', '喽', '你', '你']
# 删除多个元素

# 有问题
for i in list:
    if i == '你':
        list.remove(i)  # 存在漏删的问题，只要紧挨着就会漏删下一个
        '''
        原因是：每当我们删除一个之后会改变之前的列表，但是我们还是按照之前的index删除，列表的长度-1，
        所以不论下一个是什么都会跳过；前面是一个"你"，跳过了"好"，我们需要得到的也是这样，所以感觉没
        问题，但是一旦删除的元素是相邻的，那么就会出现问题。
        '''
print(list)

# 方法一：
n = 0
while n < len(list):
    if list[n] == '你':
        list.remove('你')
    else:
        n += 1

print(list)

# 方法二：
result = []
for i in list:
    if i != '你':
        result.append(i)

list = result
print(list)

# 方法三：  倒着查找，正向删除
for i in list[::-1]:
    if i == '你':
        list.remove(i)
print(list)
