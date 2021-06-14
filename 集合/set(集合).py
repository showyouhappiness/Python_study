"""
使用set去重
"""
list1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 9]
set1 = set(list1)
print(type(set1))
list2 = list(set1)
print(list2)

"""
声明集合添加元素
"""
set2 = set()  # 空集合set
print(type(set2))
print(len(set2))

"""
添加元素
"""
set2.add('三体')
print(set2)
set2.add('流浪地球')
print(set2)
set2.add('球状闪电')
print(set2)

# 无序的（不能使用index）
set1.update(set2)
print(set1)
print(set2)
set1.remove('三体')
print(set1)
set1.pop()
print(set1)
