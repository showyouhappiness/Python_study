# 元组和字典的拆包
def demo(*args, **kw):
    print(args)
    print(kw)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# 拆包语法，简化元组变量/字典变量的传递
demo(*gl_nums, **gl_dict)
