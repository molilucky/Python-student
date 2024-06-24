import pygame
import sys

from pygame.locals import *

pygame.init()

size = width, height = 1280, 700
bg = (255, 255, 255)
speed = [0, 0]
ratio = 1.0

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption("初次见面，请大家多多关照！")

oturtle = pygame.image.load('turtle.png')
turtle = oturtle
oturtle_rect = oturtle.get_rect()
position = turtle_rect = oturtle_rect

l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        # 给小乌龟添加方向操作
        if event.type == KEYDOWN:
            a = 6
            if event.key == K_LEFT:
                if turtle != l_head:
                    turtle = l_head
                speed = [-a, 0]

            if event.key == K_RIGHT:
                if turtle != r_head:
                    turtle = r_head
                speed = [a, 0]

            if event.key == K_UP:
                speed = [0, -a]
            if event.key == K_DOWN:
                speed = [0, a]
            # 给小乌龟添加缩放
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                if event.key == K_EQUALS and ratio < 2:
                    ratio += 0.1
                if event.key == K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0
                turtle = pygame.transform.smoothscale(oturtle,
                                                      (int(oturtle_rect.width * ratio),
                                                       int(oturtle_rect.height * ratio)))
                l_head = turtle
                r_head = pygame.transform.flip(turtle, True, False)
                turtle_rect = turtle.get_rect()
                position.width, position.height = turtle_rect.width, turtle_rect.height
        # 调整窗口大小
        if event.type == VIDEORESIZE:
            size = width, height = event.size
            screen = pygame.display.set_mode(size, RESIZABLE)

    position = position.move(speed)

    # 碰墙转向
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()

    clock.tick(75)
