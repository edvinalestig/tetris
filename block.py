import pygame
from pygame import Rect, draw


class Block:

    def __init__(self, row, col, screen):
        self.row = row
        self.col = col
        self.rect = Rect(100 * col, 100 * row, 100, 100)
        self.screen = screen
        self.isStuck = False

        self.draw()

    def draw(self):
        draw.rect(self.screen, (0, 255, 0), self.rect)


    def drop(self):

        if self.isStuck:
            return False

        if self.row >= 9:
            self.isStuck = True
            return False

        self.rect.move_ip(0, 100)
        self.row += 1

