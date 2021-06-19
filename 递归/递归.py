# 递归
def sun_numbers(num):
    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return 1
    else:
        return num + sun_numbers(num - 1)


result = sun_numbers(4)
print(result)
