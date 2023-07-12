import random

# 从控制台输入要出的拳 ——石头（1）剪刀（2）布（3）
player = int(input("请出拳 石头（1）剪刀（2）布（3）"))

# 电脑 随机出拳——假定电脑先一直出拳
computer = random.randint(0, 3)

# 比较胜负
# 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
# 再在每一个条件之间，使用回车，PyCharm 可以自动增加8各空格
if ((player == 1 and computer == 2) or
        (player == 2 and computer == 3) or
        (player == 3 and computer == 1)):
    print("选手赢了")
elif player == computer:
    print("双方一样，平局")
else:
    print("电脑赢了")
