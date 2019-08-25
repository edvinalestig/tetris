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

                    if e.key == pygame.K_a:
                        self.active_piece.move(piece.DIR["LEFT"])
                        self.draw()
                        pass

                    elif e.key == pygame.K_d:
                        self.active_piece.move(piece.DIR["RIGHT"])
                        self.draw()
                        pass

                    elif e.key == pygame.K_s:
                        self.game.speed *= 4

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_s:
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

    def on_piece_stick(self):
        print("stuck")
        self.collision_detector.piece.append_piece(self.active_piece)
        self.spawn_piece()
