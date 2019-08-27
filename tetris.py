import gamehandler as handler
import util

class Tetris:

    def __init__(self, cols, rows):

        # Set dimensions of playing field
        self.cols = cols
        self.rows = rows

        # Set width for cells in grid system
        self.cell_width = util.grid_cell_width(self.cols, self.rows)

        # Game governing and observing
        self.game_handler = handler.GameHandler(self)

        # Start the game
        self.game_handler.start()


a = Tetris(10, 20)
