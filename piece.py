import random
import math

import block

shapes = [
    [
        [-1, 0],
        [-1, 1],
        [0, 0],
        [0, 1]
    ],
    [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3]
    ],
    [
        [-1, 0],
        [0, 0],
        [0, 1],
        [1, 1]
    ],
    [
        [-1, 1],
        [0, 1],
        [0, 0],
        [1, 0]
    ],
    [
        [-1, 0],
        [0, 0],
        [1, 0],
        [0, 1]
    ],
    [
        [-1, 0],
        [0, 0],
        [1, 0],
        [1, 1]
    ]
]

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 128, 0),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

DIR = {
    "LEFT": -1,
    "RIGHT": 1,
    "DOWN": 0
}

class Piece:

    def __init__(self, handler, shape = None):
        # Set Reference to handler
        self.handler = handler

        # List of blocks in shape
        self.blocks = []

        # position
        self.x = int(handler.game.cols / 2)
        self.y = -2

        # Enable block falling
        self.falling = True

        if shape is None:
            self.set_random_piece()
        else:
            self.from_shape(shape)

    def from_shape(self, shape, offset = (0, 0), color=(255, 0, 0)):
        for cordinate in shape:
            self.blocks.append(block.Block(self.handler, cordinate[0] + offset[0], cordinate[1] + offset[1], self.handler.game.blockSize, color=color))

    def set_random_piece(self):

        num = random.randint(0, len(shapes) - 1)
        self.from_shape(shapes[num], (self.x, self.y), color=colors[num])

    def update(self):
        self.move(DIR["DOWN"])

    def draw(self):
        for block in self.blocks:
            block.draw()

    def move(self, dir):
        if not self.falling:
            return

        vec = None

        if dir == DIR["DOWN"]:
            vec = (0, 1)
        elif dir == DIR["LEFT"]:
            vec = (-1, 0)
        elif dir == DIR["RIGHT"]:
            vec = (1, 0)
        else:
            return "Could not move piece"

        # Check if move is llegal
        for block in self.blocks:
            if not self.handler.collision_detector.aproove(block.x, block.y, vec):
                if dir == DIR["DOWN"]:
                    self.handler.on_piece_stick()
                return

        # Move blocks
        for block in self.blocks:
            block.move(vec)

        self.x += vec[0]
        self.y += vec[1]

    def append_piece(self, piece):
        for block in piece.blocks:
            self.blocks.append(block)

    def rotate(self):
        for block in self.blocks:

            dx = block.x - self.x
            dy = block.y - self.y

            nx = -dy
            ny = dx

            block.set_pos((self.x-dy, self.y+dx))
