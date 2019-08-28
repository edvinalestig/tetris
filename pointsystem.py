import math

class PointSystem:

    def __init__(self, handler):

        # Define level
        self.level = 0

        # Reference handler
        self.handler = handler

        # Define points
        self.points = 0

        #
        self.lines_cleared = 0

    def reset(self):
        self.points = 0
        self.handler.pace = 60 / 48
        self.level = 0
        self.lines_cleared = 0
        self.handler.window.set_caption("%i points" % self.points)

    def rows_cleared(self, rows):

        # Update lines cleared in total
        self.lines_cleared += rows

        row_pts = [0, 40, 100, 300, 1200]
        level_paces = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1]

        # Update total points gained
        self.points += row_pts[min(rows, len(row_pts) - 1)] * (self.level + 1)

        # Set level depending on lines cleared
        self.level = int(self.lines_cleared / 1)

        # Set pace depending on level
        self.handler.pace = (60 / level_paces[min(self.level, len(level_paces))])

        # Set caption of game window to display points and levelsssssssssssss
        self.handler.window.set_caption("Level %i | %i points" % (self.level, self.points))
