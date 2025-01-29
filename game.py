import pygame, sys
from pygame import Vector2
from settings import Settings

class Game:
    """A general class for managing resources and methods
     game operation."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.cell_size * self.settings.number_of_cells,
                                               self.settings.cell_size * self.settings.number_of_cells))
        pygame.display.set_caption("Retro Snake")

    def run_game(self):
        """Start main game loop."""
        while True:
            # waiting for a key or mouse button to be pressed.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # changing surface color
            self.screen.fill(self.settings.background_color)

            # draw horizontal lines
            for cell in range(1, self.settings.number_of_cells):
                pygame.draw.line(self.screen, pygame.Color('black'),Vector2(0, self.settings.cell_size * cell),
                                 Vector2(self.settings.cell_size * self.settings.number_of_cells,self.settings.cell_size * cell), 2)

            # draw vertical lines
            for cell in range(1, self.settings.number_of_cells):
                pygame.draw.line(self.screen, pygame.Color('black'), Vector2(self.settings.cell_size * cell, 0),
                                 Vector2(self.settings.cell_size * cell, self.settings.cell_size * self.settings.number_of_cells), 2)

            # Display the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    # create a copy of the game and run it
    game = Game()
    game.run_game()
