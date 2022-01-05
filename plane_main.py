import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print('游戏初始化')
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 创建游戏时钟
        self.clock = pygame.time.Clock()

        # 调用私有方法 创建精灵和精灵组
        self.__creat_sprite()

        # 设置定时器事件    每1s  创建一个敌机
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)

        # 设置发射子弹事件   0.5秒发射一发子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __creat_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


        pass

    def start_game(self):
        # print('游戏开始')
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SCEOND)

            # 事件监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新精灵、精灵组
            self.__update_sprites()

            # 更新显示
            pygame.display.update()


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == 256:
                PlaneGame.__game_over(self)
            elif event.type == CREAT_ENEMY_EVENT:
                # print('敌机出厂...')

                # 创建敌机
                enemy = Enemy()
                # 添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 是用键盘模块获取键盘按键
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] and not keys_pressed[pygame.K_LEFT]:
            self.hero.speed = 2
            # print('向右移动')
        elif keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = -2
            # print('向左移动')
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet, self.enemy_group, True, True)
        enemies = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        if len(enemies) > 0:
            print('英雄牺牲')
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet.update()
        self.hero.bullet.draw(self.screen)

    @staticmethod
    def __game_over(self):
        try:
            pygame.quit()
            exit()
        except Exception as result:
            # print("未知错误：%s" % result)
            pass


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
