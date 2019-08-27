import sys
import time
import pygame

import util
import window
import collisiondetector as col_det
import piece

import pointsystem

class GameHandler:

    def __init__(self, meta):

        # Meta info about the game
        self.meta = meta

        # Set pace of game in updates per second
        self.level = 0
        self.pace = 4

        # Current status of the playing field
        self.grid = util.empty_grid(meta.cols, meta.rows)

        # Drawable window
        self.window = window.Window(self.meta.cell_width * meta.cols, self.meta.cell_width * meta.rows)

        # Collision detector
        self.collision_detector = col_det.CollisionDetector(self)

        # Active controllable piece
        self.active_piece = piece.Piece(self)

        # Point system
        self.point_system = pointsystem.PointSystem(self)

        # Array of inhabiting pieces
        self.pieces = []

    def restart(self):
        # Current status of the playing field
        self.grid = util.empty_grid(self.meta.cols, self.meta.rows)

        # Active controllable piece
        self.active_piece = piece.Piece(self)

    def spawn_piece(self):

        # If there is no existing piece
        if not self.active_piece is None:

            # What rows are changed during the sticking of current block?
            affected = [False] * self.meta.rows

            # Create hitbox
            for block in self.active_piece.blocks:
                self.grid[block.y][block.x] = block
                affected[block.y] = True

            deleted_rows = 0
            # Find and delete necessary rows
            for y in range(len(self.grid)):
                if affected[y]:
                    row_full = True
                    # Check if row is full
                    for x in range(len(self.grid[y])):
                        if self.grid[y][x] is None:
                            row_full = False
                            break

                    # Delete row
                    if row_full:
                        deleted_rows += 1

                        for x in range(len(self.grid[y])):
                            self.grid[y][x] = None

                        # Move rows above delted row down
                        for ro in range(y - 1, 0, -1):
                            for xo in range(len(self.grid[ro])):
                                self.grid[ro + 1][xo] = self.grid[ro][xo]
                                if not self.grid[ro][xo] is None:
                                    self.grid[ro][xo].move_ip(0, 1)

            self.point_system.rows_cleared(deleted_rows)


        # Spawn new block
        self.active_piece = piece.Piece(self)

    def update(self):

        # Try to advance active piece, if unsuccessful, spawn new piece
        if not self.active_piece.advance():

            if self.active_piece.pos['y'] <= 0:
                self.restart()
            else:
                self.spawn_piece()

    # Draw game objects
    def draw(self):
        # Clear the current frame
        self.window.clear_frame()

        # Draw active piece
        self.active_piece.draw()

        # Draw all stuck blocks
        for row in self.grid:
            for block in row:
                if not block is None:
                    block.draw()

        # Draw the current frame
        self.window.draw_frame()

    # Handle all type of game events such as inputs
    # TODO: Fix keyboard events and tidy up code
    def __handle_events(self, events):

        # Loop through queued events
        for e in events:

            # Close screen event
            if e.type == pygame.QUIT:
                sys.exit()

            # Keydown events
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    self.active_piece.rotate()
                    self.draw()
                elif e.key == pygame.K_a:
                    self.active_piece.move_ip(-1, 0)
                    self.draw()
                elif e.key == pygame.K_d:
                    self.active_piece.move_ip(1, 0)
                    self.draw()
                elif e.key == pygame.K_s:
                    self.pace *= 4

            # Keyup events
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_s:
                    self.pace /= 4

    # Start game loop
    def start(self):

        last_time = time.time()

        # Game loop
        while 1:
            now = time.time()

            # Handle all types of game events
            self.__handle_events(pygame.event.get())

            # If time delta since last update surpass ups time -> update
            if not self.pace:
                continue

            if now - last_time >= 1 / self.pace:
                last_time = now

                # Update game variables and then draw to screen
                self.update()
                self.draw()
