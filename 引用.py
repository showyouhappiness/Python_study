def test(num):
    print("在函数内部%d对应的内存地址是%d" % (num, id(num)))

    # 定义一个字符串变量
    result = "hello"

    print("函数要返回数据的内存地址是 %d" % id(result))

    # 将字符串变量返回,返回的是数据的引用，而不是数据本身
    return result


# 定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print("a变量保存数据的内存地址是%d" % id(a))

# 调用test函数，本质上传递的是实参保存数据的引用地址，而不是实参保存的数据
# 注意：如果函数有返回值，但是没有定义变量接收
# 程序不会报错，但是无法获得返回结果
r = test(a)
print("%s的内存地址是%d" % (r, id(r)))
test(a)


# 局部变量
def demo1():
    # 定义一个局部变量
    num = 10

    print("在demo1函数内部的变量是%d" % num)


def demo2():
    pass
    # num = 11
    # print("%d" % num)


# 在函数内部定义的变量，不能在其他位置使用
# print("%d " % num)  这里会报错 NameError: name 'num' is not defined
demo1()
demo2()

# 全局变量 --不允许直接修改
num = 10

print("%s 10" % id(num))


def demo3():
    # 希望修改全局变量的值
    # 在python中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    num = 99
    print("%s 99" % id(num))
    print("demo => %d" % num)


def demo4():
    print("demo => %d" % num)


demo3()
demo4()

# 全局变量 --不允许直接修改
num1 = 10

print("%s 10 ****" % id(num1))


def demo5():
    # 希望修改全局变量的值 -- 使用global关键字声明一下变量即可
    # global关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时,就不会创建布局变量
    global num1
    num1 = 99
    print("%s 99 ****" % id(num1))
    print("demo => %d" % num1)


def demo6():
    print("demo => %d" % num1)


demo5()
demo6()
