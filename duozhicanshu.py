"""
参数名前增加一个*可以接受元组
参数名前增加两个*可以接受字典
一般再给多值参数命名时，习惯使用以下两个名字
*args -- 存放元组参数，前面一个*
**kw -- 存放字典参数，前面两个*
"""


def demo(num, *args, **kw):
    print(num)
    print(args)
    print(kw)


demo(1, 2, 3, 4, 5, name="小明", age=18)
