import util

class CollisionDetector:

    def __init__(self, handler):

        # Reference handler
        self.handler = handler

    def approve_move(self, x, y):

        if not util.pos_is_on_grid(self.handler.meta, x, y):
            return False

        if y >= 0:
            if not self.handler.grid[y][x] is None:
                return False

        return True
