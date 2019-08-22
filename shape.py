import block

shapeForms = [
    [
        [1, 0],
        [0, 0],
        [0, 1],
        [1, 1]
    ]
]


class Shape:
    def __init__(self, screen):
        self.screen = screen
        self.blocks = []
        self.row = 0
        self.col = 2
        self.shape = shapeForms[0]
        self.isStuck = False

        for i in self.shape:
            self.blocks.append(block.Block(i[0] + self.row, i[1] + self.col, self.screen))

    def move(self):
        if self.isStuck:
            return False

        for block in self.blocks:
            block.move(block.col, block.row + 1)

    def drop(self, occupied):
        if self.isStuck:
            return

        cords = []
        for block in self.blocks:
            cords.append(block.drop())

        for cord in cords:
            if cord[1] > 19 or occupied[cord[1]][cord[0]] == True:
                self.isStuck = True

                for block in self.blocks:
                    occupied[block.row][block.col] = False

        return occupied

    def draw(self):
        for block in self.blocks:
            block.draw()
