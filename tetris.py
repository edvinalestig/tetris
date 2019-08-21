import pygame
from pygame import Rect, draw
import block
import sys
import time

pygame.init()
size = width, height = 500, 1000
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

blocks = [block.Block(0, 3, screen)]

lastTime = time.time()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    now = time.time()

    if now - lastTime > 1:

        screen.fill(0)

        
        for block in blocks:
            block.draw()
            block.drop()

        pygame.display.update()

        lastTime = now
