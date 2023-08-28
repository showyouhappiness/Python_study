def func(str1):
    even = []
    odd = []
    for i in str1:
        num = int(i)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even.sort(reverse=True)
    odd.sort()
    odd.extend(even)
    # 将列表转换成字符串
    str2 = ''.join(str(i) for i in odd)
    return str2


str1 = '1982376455'
print(func(str1))
