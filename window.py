import pygame

class Window:

    def __init__(self, width, height, background_color=(0,0,0)):

        # Set background_color
        self.background_color = background_color

        # Init screen
        if not pygame.get_init():
            pygame.init()

        # Set up pygame display object
        self.display = pygame.display.set_mode((width, height))

        # Set window properties
        pygame.display.set_caption("DTetris - 1.2")
        pygame.display.set_icon(pygame.image.load('tetris.png'))

    # Clear frame for next frame
    def clear_frame(self):
        self.display.fill(self.background_color)

    # Draws current frame to screen
    def draw_frame(self):
        pygame.display.update()

    def set_caption(self, caption):
        pygame.display.set_caption("DTetris - 1.2 | %s" % caption)
