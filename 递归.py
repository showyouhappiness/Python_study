# 递归
def sun_numbers(num):
    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return
    sun_numbers(num - 1)


sun_numbers(4)
