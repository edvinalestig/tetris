import pygame
import collissionDetector as cd


class Block:

    def __init__(self, game, x, y):
        self.game = game

        self.pos = x, y

        # Create object visible on screen
        self.rect = pygame.Rect(x * game.blockSize, y * game.blockSize, game.blockSize, game.blockSize)

    def draw(self):

        # Draw rect to screen
        pygame.draw.rect(self.game.display, (0, 255, 0), self.rect)

    def move(self, x, y):

        move = (x, y)

        # Move visible block x, and y steps
        if cd.aproove(move) == cd.APROOVED:
            self.rect.move_ip(x * self.game.blockSize, y * self.game.blockSize)