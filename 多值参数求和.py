# 多值参数求和
def sun_numbers(*args):
    num = 0
    print(args)
    for n in args:
        num += n
    return num


result = sun_numbers(1, 2, 3, 4, 5)

print(result)


# 元组求和
def sun_numbers1(args):
    num = 0
    print(args)
    for n in args:
        num += n
    return num


result = sun_numbers1((1, 2, 3, 4, 5))

print(result)
