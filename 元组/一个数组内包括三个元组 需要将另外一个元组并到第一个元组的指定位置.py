array = [(1, 2), (3, 4), (5, 6)]  # 数组包含三个元组
tuple_to_merge = (10, 11)  # 要合并的元组
index = 1  # 要合并的位置索引

array[0] = array[0][:index] + tuple_to_merge + array[0][index:]
print(array)  # [(1, 10, 11, 2), (3, 4), (5, 6)]

x = (1,) + (2,) + (3,)
print(x)
