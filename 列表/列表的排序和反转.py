import random

numbers = []

for i in range(8):
    ran = random.randint(1, 20)
    numbers.append(ran)
print(numbers)

# numbers.reverse()  # 反转
# print(numbers)

# numbers.sort()  #   默认升序（False），可以通过reverse参数改变
# print(numbers)

numbers.sort(reverse=True)
print(numbers)

'''
通过键盘输入一个0~20之间的整数，将整数插入到排序后的列表中
'''

# 方法一
# num = int(input('输入一个0~20之间的整数：'))
# numbers.append(num)
# numbers.sort()
# print(numbers)

# # 方法二
# num = int(input('输入一个0~20之间的整数：'))
# for i in range(len(numbers)):
#     if (numbers[i] <= num) and (numbers[i + 1] > num):
#         numbers.insert(i + 1, num)
#         break
# print(numbers)

# 方法三
number = int(input("输入一个0~20之间的整数："))
for i in numbers:
    if number <= i:
        numbers.insert(numbers.index(i), number)
        break
else:
    numbers.append(number)
