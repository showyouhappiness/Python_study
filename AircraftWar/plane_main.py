from plane_sprites import *
import pygame
pygame.init()


class PlaneGame(object):
    # 飞机大战主游戏

    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        # set_mode里面的第一参数是元组，而SCREEN_RECT是一个矩形，
        # 从矩形中拿出元组 pygame给了一个方法 .size属性 可以当前文件夹下study.py中找到
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_spriters()
        # 设置定时器事件 创建敌机 间隔1S 创建子弹 .5s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_spriters(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建英雄精灵和精灵组
        # self.bullet = Hero()
        # self.bullet_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:
            # 设置游戏刷新频率，一般情况下一秒刷新60次
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        # 事件监听
        for event in pygame.event.get():
            # 判断用户是否点击了关闭按钮
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # 方法一：事件监听方法
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右")
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     print("向左")

        # 方法二：键盘模块  游戏为了保持流畅性一般使用这种方式 使用方法一要一直的点击
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值是否为1，是1则按下
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 子弹摧毁敌机
        pygame.sprite.groupcollide(
            self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemise = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, True)
        if len(enemise) > 0:

            # 让英雄牺牲
            self.hero.kill()

            # 游戏结束
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束。。。")
        pygame.quit()
        # 直接退出系统
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
