import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 800, 500
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

turtle = pygame.image.load("turtle.png")
position = turtle.get_rect()

speed = [5, 0]

turtle_right = pygame.transform.rotate(turtle, 90)
turtle_top = pygame.transform.rotate(turtle, 180)
turtle_left = pygame.transform.rotate(turtle, 270)
turtle_bottom = turtle

turtle = turtle_top

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    position = position.move(speed)

    if position.right > width:
        turtle = turtle_right
        position = turtle_rect = turtle.get_rect()
        position.right = width
        position.top = 0
        speed = [0, 5]

    if position.bottom > height:
        turtle = turtle_bottom
        position = turtle_rect = turtle.get_rect()
        position.right = width
        position.bottom = height
        speed = [-5, 0]

    if position.left < 0:
        turtle = turtle_left
        position = turtle_rect = turtle.get_rect()
        position.left = 0
        position.bottom = height
        speed = [0, -5]
    if position.top < 0:
        turtle = turtle_top
        position = turtle_rect = turtle.get_rect()
        position.top = 0
        position.left = 0
        speed = [5, 0]

    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()

    clock.tick(60)
