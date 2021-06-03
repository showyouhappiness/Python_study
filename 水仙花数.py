i = int(input("100到一个数字范围："))
for num in range(100, i):
    gewei = num % 10
    shiwei = num // 10 % 10
    baiwei = num // 100

    if gewei ** 3 + shiwei ** 3 + baiwei ** 3 == num:
        print(num)
