# 导入模块的顺序，建议按照下面顺序导入
# 官方标准模块导入
# 第三方模块导入
# 应用程序模块导入
import pygame
from plane_sprites import *

# 游戏初始化
pygame.init()

# 创建一个游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (190, 500))

# 可以在所有的绘制结束以后再update 更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.首先定义rect记录飞机的出视位置
hero_rect = pygame.Rect(200, 550, 102, 126)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)


# 游戏循环 意味着游戏正式开始
while True:
    # 设置游戏刷新频率，一般情况下一秒刷新60次就可以了,
    # 也就是tick的参数为60
    clock.tick(60)

    # 捕获事件
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)

    # 事件监听
    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            pygame.quit()

            # 直接退出系统
            exit()

    # 2.修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update  让组中的所有精灵更新位置
    enemy_group.update()

    # draw  在screen上绘制所有的精灵
    enemy_group.draw(screen)

    # 4.调用update方法更新显示
    pygame.display.update()
pygame.quit()
