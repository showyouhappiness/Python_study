class flower():
    for i in range(100, 1000):
        a = i // 100
        b = (i - a * 100) // 10
        c = (i - a * 100 - b * 10)
        if i == pow(a, 3) + pow(b, 3) + pow(c, 3):
            print(i)


if __name__ == '__main__':
    flower = flower()
