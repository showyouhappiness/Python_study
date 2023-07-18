tuple1 = (1, 2, 3, 4, 5)  # 元组1
tuple2 = (10, 11, 12)  # 元组2
index = 2  # 要合并的位置索引

list1 = list(tuple1)  # 将元组1转换为列表
list1[index:index] = list(tuple2)  # 在指定位置索引插入元组2的元素
merged_tuple = tuple(list1)  # 将列表转换回元组

print(merged_tuple)  # (1, 2, 10, 11, 12, 3, 4, 5)
