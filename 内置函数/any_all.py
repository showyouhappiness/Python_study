numbers = [0, 1, 2, 3, 4]

result = any(numbers)
print(result)  # 输出 True，因为列表中至少有一个非零元素

str1 = ['1', '2', '', None]

result = all(str1)
print(result)  # 输出 False，因为列表中有一个元素为空字符串、None
