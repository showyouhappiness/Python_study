class Cat:
    def __init__(self, name):
        self.name = name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s去了" % self.name)


# tom是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
# del tom

# 如果不适用del方法。那么所有的print执行完以后才会执行__del__
print('-' * 50)
