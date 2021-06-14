class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("%s没有子弹了" % self.model)
            return
        # 发射  -1
        self.bullet_count -= 1
        # 提示发射信息
        print("%s正在射击，剩余%d颗子弹" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 姓名
        self.name = name

        # 枪 --默认新兵没有枪,只是一个空对象，那么就是用None
        self.gun = None

    def fire(self):
        # 判断士兵是否有枪
        # ==判断的是两个变量的值是否相等
        # is判断的是两个变量的内存地址是否一致--引用对象是否为同一个
        # if self.gun == None:
        if self.gun is None:
            return
        # 让枪装填子弹
        self.gun.add_bullet(50)
        # 让枪发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")

# 创建士兵
shibing = Soldier("士兵")
shibing.gun = ak47
shibing.fire()
