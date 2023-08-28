int1 = -54321


def reverse_integer(int1):
    if int1 < 0:
        int1 = -int(str(-int1)[::-1])
    else:
        int1 = int(str(int1)[::-1])
    return int1


print(reverse_integer(int1))
