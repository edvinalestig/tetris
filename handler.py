import sys
import time

import pygame

import collisionDetector
import piece

class Handler:

    def __init__(self, game):

        # Initialize Game
        if not pygame.get_init():
            pygame.init()

        # Reference game parent object
        self.game = game

        # Create pygame drawable display
        self.display = pygame.display.set_mode((game.width, game.height))

        # Set controllable piece
        self.active_piece = piece.Piece(self)

        # Create empty piece for collision detection
        self.collision_detector = collisionDetector.CollisionDetector(self, piece.Piece(self, []))

        # Bool array of stuck pieces
        self.play_field = []

        for col in range(self.game.rows):
            arr = []

            for row in range(self.game.cols):
                arr.append(False)

            self.play_field.append(arr)


    def update(self):
        self.active_piece.update()
        self.collision_detector.piece.update()

    def draw(self):
        # update pieces
        self.display.fill(0)

        # draw pieces
        self.active_piece.draw()
        self.collision_detector.piece.draw()

        # Update display
        pygame.display.update()

    def handle(self):
        # Game Loop
        # trailing time variable
        last_time = time.time()
        while 1:
            # Current time
            now = time.time()

            # Handle events
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:

                    if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                        self.active_piece.move(piece.DIR["LEFT"])
                        self.draw()

                    elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                        self.active_piece.move(piece.DIR["RIGHT"])
                        self.draw()

                    elif e.key == pygame.K_w or e.key == pygame.K_UP:
                        self.active_piece.rotate()
                        self.draw()

                    elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        self.game.speed *= 4

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                        self.game.speed /= 4


            # Update per tick
            if now - last_time >= 1 / self.game.speed:

                # Tick game
                self.update()
                self.draw()

                # Set trailing time to current time
                last_time = now

    def spawn_piece(self):
        self.active_piece = piece.Piece(self)

    def piece_stick(self):

        # Update
        for block in self.active_piece.blocks:
            self.play_field[block.y][block.x] = True

        for row in self.play_field:
            clear_current_row = True

            for i in range(len(row)):
                if not row[i]:
                    clear_current_row = False
                    break

            if clear_current_row:
                for i in range(len(row)):
                    row[i] = False

        self.collision_detector.piece.append_piece(self.active_piece)
        self.spawn_piece()
