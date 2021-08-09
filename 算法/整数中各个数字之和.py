class Number:
    n = int(input('请输入即将要输入的数字的整数部分的位数：'))
    x1 = eval(input('请输入你想要的数字： '))
    # 设置number用于计算各个位上的数字之和
    number = 0

    # 利用循环计算各个数字之和
    while n >= 1:
        if (n - 1) != 0:
            # 用于计算x1的末尾数字
            number1 = x1 % 10
            number += number1
        else:
            # 此时说明只有最后一位数字
            number += x1
        # 更新x1的数值
        x1 = int(x1 / 10)
        n = n - 1
    print(number)


if __name__ == '__main__':
    Number = Number
