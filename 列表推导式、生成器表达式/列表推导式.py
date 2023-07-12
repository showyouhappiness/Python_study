list1 = []
for i in range(1, 11):
    list1.append(i)
print(list1)

# 列表推导式
list2 = [i for i in range(1, 11)]
print(list2)

# 0-100之间所有的偶数存放在列表中
list4 = [i for i in range(0, 101, 2)]
print(list4)

list5 = [i for i in range(0, 101) if i % 2 == 0]
print(list5)

# [结果1 if 条件 else 结果2 for 变量 in 可迭代的]
words = ['hello', 'world']
list6 = [word if word.startswith('h') else word.upper() for word in words]
print(list6)

# 二维
a = [(x, y) for x in range(1, 3) for y in range(3)]
print(a)

# 三维
b = [(x, y, z) for x in range(1, 3) for y in range(3) for z in range(4, 6)]
print(b)

# 将[1,2,3,4,...,100]分成[[1,2,3],[4,5,6]...]
c = [[i, i + 1, i + 2] if i <= 98 else [i for i in range(i, 101)] for i in range(1, 101, 3)]
print(c)

test = [['hello', 'world'], ['python', 'java']]
# 将有两个l的放到新列表中
d = [j for i in test for j in i if j.count('l') >= 2]
print(d)
