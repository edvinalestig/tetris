import pygame
from pygame import Rect, draw


class Block:

    def __init__(self, row, col, screen):
        self.row = row
        self.col = col
        # self.rect = Rect(100 * col, 100 * row, 100, 100)
        self.update()
        self.screen = screen
        self.isStuck = False

        self.draw()

    def draw(self):
        draw.rect(self.screen, (0, 255, 0), self.rect)

    def update(self):
        self.rect = pygame.Rect(50 * self.col, 50 * self.row, 50, 50)


    def move(self, col, row):
        self.col = col
        self.row = row
        self.update()

    def drop(self):
        return [self.col, self.row + 1]


