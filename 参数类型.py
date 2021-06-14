def demo(num, num_list):
    # 赋值语句
    # 在函数内部，针对函数使用赋值语句，不会修改到外部的实参变量
    num = 200
    num_list = [1, 2, 3]

    print(num, num_list)


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num, gl_list)


def mutable(num_list):
    # num_list = [1, 2, 3]
    # 如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据
    # num_list.extend([1, 2, 3])
    num_list.append(9)
    print(num_list)


gl_list1 = [6, 7, 8]
mutable(gl_list1)
print(gl_list1)
