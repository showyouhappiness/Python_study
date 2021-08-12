nums = [1, 3, 4, 0]
target = 4
result_list = []


# 解法一：
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 result_list.append([i, j])
#     return result_list

# 解法二：
def twoSum(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            result_list.append([i, j])

    return result_list


# 解法三：
# def twoSum(nums, target):
#     hashmap = {}
#     for i, num in enumerate(nums):
#         if hashmap.get(target - num) is not None:
#             result_list.append([i, hashmap.get(target - num)])
#         hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
#     return result_list


result = twoSum(nums, target)
print(result)
