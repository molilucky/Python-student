import pygame
import sys

pygame.init()

size = width, height = 640, 480
bg = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('FishC demo')
# event_text = []

font = pygame.font.Font(None, 20)

font_height = font.get_linesize()

position = 0
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
        position += font_height
        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()
