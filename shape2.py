import random
import block2 as block

# Select random seed for re-creational purposes
random.seed(1231)

# Define shapes
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
    ]
]


class Shape:

    def __init__(self, game):

        # Related game object
        self.game = game

        # Array of inhabited blocks
        self.blocks = []

        self.pos = int(game.cols / 2), 0

        # Enable falling for spawned block
        self.falling = True

    def set_random_shape(self):
        self.blocks = []

        # Set shape to random shape
        random_shape = shapes[random.randint(0, len(shapes))]
        self.append_shape(random_shape, self.pos)

    def append_shape(self, shape, offset):

        if offset == None:
            offset = (0, 0)

        for pos in shape:
            self.blocks.append(block.Block(self.game, offset[0] + pos[0], offset[1] + pos[1]))

    def advance(self):

        if not self.falling:
            return

        for block in self.blocks:
            block.move(0, 1)

    def draw(self):

        for block in self.blocks:
            block.draw()