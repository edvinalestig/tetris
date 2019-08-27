import pygame

import util

class Block:

    def __init__(self, handler, x, y
    , color = (255, 0, 0)):

        # Reference to game handler
        self.handler = handler

        # Define position
        self.x = x
        self.y = y

        # Define color
        self.color = color

    def move(self, x, y):
        self.x = x
        self.y = y

    def move_ip(self, x, y):
        self.x += x
        self.y += y

    def draw(self):

        # Defina raw x, y, and width values
        rw = self.handler.meta.cell_width
        rx = self.x * rw
        ry = self.y * rw

        # Defina an edge on each nlock
        ew = rw / 10

        # Define rect objects to feed pygame draw function
        outer_rect = pygame.Rect(rx, ry, rw, rw)
        inner_rect = pygame.Rect(rx + ew, ry + ew, rw - 2*ew, rw - 2*ew)

        col = self.color
        shade_col = col[0] * 0.4, col[1] * 0.4, col[2] * 0.4

        pygame.draw.rect(self.handler.window.display, shade_col, outer_rect)
        pygame.draw.rect(self.handler.window.display, col, inner_rect)
