def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 示例
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 9
result = binary_search(arr, target)

if result != -1:
    print(f"目标值 {target} 在数组中的索引为: {result}")
else:
    print("目标值不在数组中。")
