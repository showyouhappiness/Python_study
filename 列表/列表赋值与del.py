list1 = [1, 3, 5, 7, 9]
list2 = list1  # 将list2指向list1的地址 两个指向同一个地址
list2.append(11)
print(list1, list2)

# del list2  # 从地址上直接将list2移除
# print(list1)

del list1  # 从地址上直接将list1移除
print(list2)
