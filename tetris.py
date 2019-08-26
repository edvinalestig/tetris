import handler

screenX = int(1920 / 1.5)
screenY = int(1080 / 1.5)

class Tetris:

    def __init__(self, cols, rows):
        # Play-field dimensions
        self.cols = cols
        self.rows = rows

        # Set size of blocks
        self.blockSize = int(min(screenX / cols, screenY / rows))

        # Calculate dimensions of window
        self.width = cols * self.blockSize
        self.height = rows * self.blockSize

        # Set speed of game
        self.speed = 1

        # Initiate handler
        self.handler = handler.Handler(self)
        self.handler.handle()

a = Tetris(10, 20)
