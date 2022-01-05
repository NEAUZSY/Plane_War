import random
import pygame


# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 帧率
FRAME_PER_SCEOND = 60
# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprites(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprites):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')

        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprites):

    def __init__(self):
        super().__init__('./images/enemy1.png')
        # 指定敌机初始随机速度
        self.speed = random.randint(2, 3)
        # 指定敌机初始随机位置
        self.rect.bottom = 0

        # 设定水平最大值
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        # 判断是否飞出屏幕，如果是 从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print('飞出屏幕 需要在精灵组删除')
            self.kill()

    def __del__(self):
        # 打印敌机被销毁的位置
        # print('敌机被销毁了 %s' % self.rect)
        pass


class Hero(GameSprites):

    def __init__(self):
        super().__init__('./images/me1.png', 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹组
        self.bullet = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # print("发射子弹...")
        for i in (0, 1, 2):

            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullet.add(bullet)

    def __del__(self):
        print('Game Over')


class Bullet(GameSprites):
    """子弹精灵"""

    def __init__(self):
        super(Bullet, self).__init__('./images/bullet1.png', -2)

    def update(self):
        super(Bullet, self).update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print('销毁子弹')
        pass




