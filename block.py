import pygame

class Block:

    def __init__(self, handler, x, y, blockSize, color=(255, 0, 0)):

        # Set handler Reference
        self.handler = handler

        # set color
        self.color = color

        # Set position
        self.x = x
        self.y = y

        # Set block size
        self.blockSize = blockSize

        # Create object visible on screen
        self.rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)

    def draw(self):
        # Draw rect to screen
        edgeSize = self.blockSize / 20

        shadeIndex = 0.33
        shadeColor = self.color[0] * shadeIndex, self.color[1] * shadeIndex, self.color[2] * shadeIndex

        x = self.x * self.blockSize
        y = self.y * self.blockSize
        width = self.blockSize
        innerWidth = self.blockSize - 2 * edgeSize

        outerRect = pygame.Rect(x, y, width, width)
        innerRect = pygame.Rect(x + edgeSize, y + edgeSize, innerWidth, innerWidth)

        pygame.draw.rect(self.handler.display, shadeColor, outerRect)
        pygame.draw.rect(self.handler.display, self.color, innerRect)

    def move(self, vec):
        self.x += vec[0]
        self.y += vec[1]

    def set_pos(self, vec):
        self.x = vec[0]
        self.y = vec[1]
