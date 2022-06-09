"""
因为是地址传递而不是值传递；int（整型），float（浮点型），str（字符串）等是值传递；list（列表）、dict（字典）、tuple（元组）则是地址传递
作为参数传入函数内部，内部修改相当于修改外部的列表。
"""
a = [1, 2, 3]


def fuc(a):
    print(id(a))
    a.append(1)
    print(a, id(a))


fuc(a)
print(a, id(a))
