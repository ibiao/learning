
import pygame
import time
from pygame.locals import *
import random


class Base(object):
    """基类"""
    def __init__(self, screen, x, y, image):
        self.x = x                    # 图片的x坐标
        self.y = y                    # 图片的y坐标
        self.screen = screen          # 窗口
        self.image = pygame.image         # 图片



class BasePlane(Base):
    """飞机的基类"""
    def __init__(self, screen, x, y, image):
        Base.__init__(self, screen, x, y, image)
        self.bullet_list = []   # 存放发射出去的子弹

    def display(self):
        """显示"""
        # 显示飞机
        self.screen.blit(self.image, (self.x, self.y))

        # 显示所有发射出去的子弹
        for bullet in self.bullet_list:
            # 显示子弹
            bullet.display()
            # 子弹移动
            bullet.move()
            # 判断子弹是否出了窗口
            if bullet.judge():
                self.bullet_list.remove(bullet)


class HeroPlane(BasePlane):
    """英雄飞机"""
    def __init__(self, screen):
        BasePlane.__init__(self, screen, 125, 270, r"./images/feiji/hero1.png")

    def move_left(self):
        """向左移动"""
        self.x -= 10

    def move_right(self):
        """向右移动"""
        self.x += 10

    def fire(self):
        """开火"""
        self.bullet_list.append(HeroBullet(self.screen, self.x, self.y))


class EnemyPlane(BasePlane):
    """敌机"""
    def __init__(self, screen):
        BasePlane.__init__(self, screen, 0, 0, "./images/feiji/enemy0.png")
        self.direction = "right"  # 用来存储飞机默认的移动方向

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        # 判断敌机是否到达窗口边界
        if self.x > 338 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet(Base):
    """子弹基类"""
    def display(self):
        """显示"""
        self.screen.blit(self.image, (self.x, self.y))


class HeroBullet(BaseBullet):
    """英雄飞机的子弹"""
    def __init__(self, screen, x, y):
        """初始化"""
        BaseBullet.__init__(self, screen, x+40, y-20, "./images/feiji/bullet.png")

    def move(self):
        """移动"""
        self.y -= 20

    def judge(self):
        """判断是否越界"""
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        """初始化"""
        BaseBullet.__init__(self, screen, x+25, y+40, "./images/feiji/bullet1.png")

    def move(self):
        """移动"""
        self.y += 5

    def judge(self):
        """判断是否越界"""
        if self.y > 600:
            return True
        else:
            return False


def key_control(hero):
    """键盘控制"""

    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero.fire()


def main():
    # 1. 创建窗口
    screen = pygame.display.set_mode((338, 600), 0, 32)

    # 2. 创建一个背景图片
    background = pygame.image.load(r"./images/feiji/background.png")

    # 3. 创建一个飞机图片
    hero = HeroPlane(screen)

    # 4. 创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        # 加载背景图片，从(0,0)位置
        screen.blit(background, (0, 0))
        # 加载英雄飞机
        hero.display()
        # 加载敌机
        enemy.display()
        # 敌机移动
        enemy.move()
        # 敌机开火
        enemy.fire()
        # 更新显示图片
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
