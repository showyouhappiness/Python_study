class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s的年龄是%d" % (self.name, self.__age))


xiaomei = Women("小美")

# 私有属性在外界是不能被直接访问的
# print(xiaomei.__age)
# 私有方法同样不允许在外界直接访问
# xiaomei.__secret()


# 在python中，我们可以在名称前面加上 _类名加上私有属性或者私有方法
xiaomei._Women__secret()