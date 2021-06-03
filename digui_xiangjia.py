# 递归案例——计算数字累加
"""
定义一个函数sum_numbers
能够接收一个num的整数参数
计算1+2+3+...+num的结果
"""


def sun_numbers(num):
    if num == 1:
        return 1
    # 假设sum_numbers 能够完成 num - 1 的累加
    temp = sun_numbers(num - 1)

    # 函数内部的核心算法就是两个数字的相加
    return num + temp


print(sun_numbers(3))
