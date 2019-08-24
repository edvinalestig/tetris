import sys
import pygame as game
import time

import shape2 as shape

class TetrisGame:

    def __init__(self, cols, rows):

        # Initialize Game
        if not game.get_init():
            game.init()

        # Play-field dimensions
        self.cols = cols
        self.rows = rows

        # Set dimensions
        # cols * blockSize = 1920 or rows * blockSize = 1080 => fit screen mode = min(screenX / cols, screenY / rows)
        self.blockSize = int(min(1920 / cols, 1080 / rows))

        # Calculate dimensions of window
        self.dim = cols * self.blockSize, rows * self.blockSize
        self.speed = 1

        # Create display from defined dimensions
        self.display = game.display.set_mode(self.dim)

        # Array of inhabited shapes
        self.shapes = [shape.Shape(self)]

        # Enter class handle loop
        self.handle()

    # Update game
    def update(self):

        # Clear display
        self.display.fill(0)

        for shape in self.shapes:
            shape.advance()
            shape.draw()

        # Update display
        game.display.update()

    def handle(self):

        self.update()

        last_time = time.time()

        # Enter game loop
        while 1:
            now = time.time()

            for e in game.event.get():
                if e.type == game.QUIT:
                    sys.exit()

            # Update per tick
            if now - last_time >= 1:
                last_time = now

                print("tick")

                # Update game
                self.update()


a = TetrisGame(11, 20)
