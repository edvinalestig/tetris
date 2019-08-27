class PointSystem:

    def __init__(self, handler):

        # Reference handler
        self.handler = handler

        # Define points
        self.points = 0

    def rows_cleared(self, rows):

        pts = 0

        if rows is 1:
            pts = 40
        elif rows is 2:
            pts = 100
        elif rows is 3:
            pts = 300
        elif rows is 4:
            pts = 1200
        elif rows > 4:
            pts = 1200
        else:
            pts = 0

        self.points += pts * (self.handler.level + 1)

        self.handler.window.set_caption("%i points" % self.points)
