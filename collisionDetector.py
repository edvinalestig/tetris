class CollisionDetector:

    def __init__(self, handler, piece):

        # Reference handler
        self.handler = handler

        # Set collideable peice
        self.piece = piece
        self.piece.falling = False

        self.play_field = []

    def approve(self, x, y, vec):
        new_pos = x + vec[0], y + vec[1]

        if new_pos[1] > self.handler.game.rows - 1:
            return False

        if new_pos[0] < 0 or new_pos[0] > self.handler.game.cols - 1:
            return False


        if new_pos[1] > 0:
            if self.handler.play_field[new_pos[1]][new_pos[0]]:
                return False

        #for block in self.piece.blocks:
        #    if new_pos[0] == block.x and new_pos[1] == block.y:
        #        return False

        return True
