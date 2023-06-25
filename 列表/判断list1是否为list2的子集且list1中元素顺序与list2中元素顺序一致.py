def is_sublist(list1, list2):
    if len(list1) > len(list2):
        return False
    for i in range(len(list2) - len(list1) + 1):
        if list2[i:i + len(list1)] == list1:
            return True
    return False


# 示例用法
list1 = [5, 1, 2]
list2 = [4, 5, 1, 2, 3, 6, 7]
result = is_sublist(list1, list2)
print(result)  # 输出：True
