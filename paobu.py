class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s,体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步可以减肥" % self.name)
        self.weight -= .5

    def eat(self):
        print("%s爱吃零食，吃零食很容易长胖" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
