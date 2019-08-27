import random

import block

structures = [
    {
        "structure": [[1, 1],
                      [1, 1]],
        "offset": {"x": 0, "y": -2},
        "rotation_axis": {"x": 0.5, "y": 0.5},
        "color": (255, 255, 0)
    },
    {
        "structure": [[1, 1, 1, 1]],
        "offset": {"x": -1, "y": -1},
        "rotation_axis": {"x": 1.5, "y": 0.5},
        "color": (0, 255, 255)
    },
    {
        "structure": [[1],
                      [1, 1, 1]],
        "offset": {"x": -1, "y": -2},
        "rotation_axis": {"x": 1, "y": 1},
        "color": (0, 0, 255)
    },
    {
        "structure": [[0, 0, 1],
                      [1, 1, 1]],
        "offset": {"x": -1, "y": -2},
        "rotation_axis": {"x": 1, "y": 1},
        "color": (255, 128, 0)
    },
    {
        "structure": [[0, 1, 1],
                      [1, 1]],
        "offset": {"x": -1, "y": -2},
        "rotation_axis": {"x": 1, "y": 1},
        "color": (0, 255, 0)
    },
    {
        "structure": [[1, 1],
                      [0, 1, 1]],
        "offset": {"x": -1, "y": -2},
        "rotation_axis": {"x": 1, "y": 1},
        "color": (255, 0, 0)
    },
    {
        "structure": [[0, 1],
                      [1, 1, 1]],
        "offset": {"x": -1, "y": -2},
        "rotation_axis": {"x": 1, "y": 1},
        "color": (255, 0, 255)
    }
]

class Piece:

    def __init__(self, handler, falling = True):#structures[random.randint(0, len(structures) - 1)]):

        # Reference to game handler
        self.handler  = handler

        # Define position
        self.pos = {"x": int(handler.meta.cols / 2) - 1, "y": 0}
        self.offset = {"x": 0, "y": 0}

        # Set falling status
        self.falling = falling

        # Define array of inhabiting blocks
        self.blocks = []

        # define shape position
        self.create_structure(structures[random.randint(0, len(structures) - 1)])
        #self.create_structure(structures[len(structures) - 1])

    def advance(self):
        if not self.move_ip(0, 1):
            return 0
        return 1

    def draw(self):
        for block in self.blocks:
            block.draw()

    def move_ip(self, x, y):
        # Check for collision if move were to be made, if detected, return 0 without moving
        for block in self.blocks:
            if not self.handler.collision_detector.approve_move(block.x + x, block.y + y):
                return 0

        # Update piece position
        self.pos['x'] += x
        self.pos['y'] += y

        # Move each block
        for block in self.blocks:
            block.move_ip(x, y)

        return 1

    def rotate(self):

        # TODO: Issue with rotation axis being -0.5 off expected value

        # Calculate a relative x and y
        rx = self.pos['x'] + self.offset['x'] + self.rotation_axis_offset['x']
        ry = self.pos['y'] + self.offset['y'] + self.rotation_axis_offset['y']

        new_pos = []
        for block in self.blocks:

            # Calculate block offset from rotation axis
            dx = block.x - rx
            dy = block.y - ry

            # Define new position for block (set offset of x to offset of y for 90 deg rotation)
            np = {"block": block, "x": int(rx - dy), "y": int(ry + dx)}

            # Check for collision if move were to be made, if detected, return 0 without moving
            if not self.handler.collision_detector.approve_move(np['x'], np['y']):
                return 0

            # Append new position to array for later use
            new_pos.append(np)

        # Set new position for each block
        for pos in new_pos:
            pos['block'].move(pos['x'], pos['y'])

        return 1

    # Create structure from preset
    def create_structure(self, structure):

        self.offset = structure['offset']
        self.rotation_axis_offset = structure['rotation_axis']

        # TODO: make look nicer
        blueprint = structure['structure']

        # Create structure of blocks
        for y in range(len(blueprint)):
            for x in range(len(blueprint[y])):

                if blueprint[y][x]:
                    xc = self.pos['x'] + self.offset['x'] + x
                    yc = self.pos['y'] + self.offset['y'] + y

                    self.blocks.append(block.Block(self.handler, xc, yc, color = structure['color']))
