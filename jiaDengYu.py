def demo(num, num_list):
    # num = num + num
    num += num

    # num_list = num_list + num_list 表面上和下面的+=功能一样，其实输出的结果不同

    # 列表变量使用+=不会做相加再赋值的操作
    # 本质上是在调用列表的extend方法 将另外一个列表整合到当前列表中  不会修改变量的引用
    num_list += num_list
    # num_list.extend(num_list) 和上面的语句一个是功能
    print(num, num_list)


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num, gl_list)
