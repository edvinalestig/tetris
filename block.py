import pygame

class Block:

    def __init__(self, handler, x, y, blockSize):

        # Set handler Reference
        self.handler = handler

        # Set position
        self.x = x
        self.y = y

        # Set block size
        self.blockSize = blockSize

        # Create object visible on screen
        self.rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)

    def draw(self):
        # Draw rect to screen
        pygame.draw.rect(self.handler.display, (0, 255, 0), self.rect)

    def move(self, vec):
        self.rect.move_ip(vec[0] * self.blockSize, vec[1] * self.blockSize)

        self.x += vec[0]
        self.y += vec[1]

    def set_pos(self, x, y):
        self.rect = self.rect.move(x * self.blockSize, y * self.blockSize)
