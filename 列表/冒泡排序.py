nums = [5, 1, 7, 6, 8, 2, 4, 3]
for j in range(0, len(nums) - 1):
    for i in range(0, len(nums) - 1 - j):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)
