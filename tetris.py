import pygame
from pygame import Rect, draw
import block, shape
import sys
import time

occupied = []
for y in range(20):
    row = []

    for x in range(10):
        row.append(False)

    occupied.append(row)

print(occupied)

pygame.init()
size = width, height = 500, 1000
speed = [2, 2]
black = 0, 0, 0

lastShape = None

def spawn():
    global lastShape

    cShape = shape.Shape(screen)
    shapes.append(cShape)
    lastShape = cShape

def update():
    global occupied
    screen.fill(0)

    if lastShape == None or lastShape.isStuck:
        spawn()

    for shape in shapes:
        shape.draw()
        occupied = shape.drop(occupied)
        shape.move()

    pygame.display.update()

screen = pygame.display.set_mode(size)
# blocks = [block.Block(0, 3, screen)]
shapes = []

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
