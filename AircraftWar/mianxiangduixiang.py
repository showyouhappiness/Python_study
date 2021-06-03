class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建一个猫对象
Tom = Cat()
print(Tom)
Tom.eat()
Tom.drink()

addr = id(Tom)
# 十六进制
print("%x" % addr)
# 十进制
print("%d" % addr)
