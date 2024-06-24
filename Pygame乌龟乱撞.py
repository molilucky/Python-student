import sys

import pygame

pygame.init()

size = width, height = 1280, 700

speed = [-2, 1]
bg = (255, 255, 255)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("初次见面，请大家多多关照！")

turtle = pygame.image.load('turtle.png')
# turtle2 = pygame.image.load('turtle2.png')

position = turtle.get_rect()
# position2 = turtle2.get_rect()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    position = position.move(speed)
    # position2 = position2.move(speed)

    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # if position2.left < 0 or position2.right > width:
    #     turtle2 = pygame.transform.flip(turtle, True, False)
    #     speed[0] = -speed[0]
    #
    # if position2.top < 0 or position2.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(bg)

    screen.blit(turtle, position)
    # screen.blit(turtle, position2)

    pygame.display.flip()
    clock.tick(100)
