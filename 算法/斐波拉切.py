def fibo(num):
    numList = [0, 1]

    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    print("前%d项斐波拉切数列为：" % num, numList)


if __name__ == '__main__':
    fibo(20)
