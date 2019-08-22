import pygame
from pygame import Rect, draw
import block, shape
import sys
import time

pygame.init()
size = width, height = 500, 1000
speed = [2, 2]
black = 0, 0, 0

def update():
    screen.fill(0)

    for shape in shapes:
        shape.draw()
        shape.drop()
        shape.move()

    pygame.display.update()

screen = pygame.display.set_mode(size)
# blocks = [block.Block(0, 3, screen)]
shapes = [shape.Shape(screen)]

update()

lastTime = time.time()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    now = time.time()
    if now - lastTime > 0.25:
        update()
        lastTime = now
