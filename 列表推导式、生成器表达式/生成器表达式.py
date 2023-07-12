list1 = []
for i in range(1, 11):
    list1.append(i)
print(list1)

# 生成器表达式
list3 = (i for i in range(1, 11))
print(list3)
