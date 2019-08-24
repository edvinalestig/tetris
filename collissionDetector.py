ILLEGAL = -1
STUCK = 0
APROOVED = 1


class CollissionDetector:

    def __init__(self, game, collidable_shape):

        self.game = game

        self.shape = collidable_shape

    def aproove(self, pos, move):

        if pos[1] + move[1] > self.game.rows:
            return STUCK

        return APROOVED
