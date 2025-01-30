import pygame, sys
from pygame import Vector2
from settings import Settings
from food import Food
from snake import Snake


class Game:
    """A general class for managing resources and methods
     game operation."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.apple = Food()
        self.snake = Snake()
        self.screen = pygame.display.set_mode((self.settings.cell_size * self.settings.number_of_cells,
                                               self.settings.cell_size * self.settings.number_of_cells))
        pygame.display.set_caption("Retro Snake")

        # custom user event
        self.SNAKE_MOVE = pygame.USEREVENT
        pygame.time.set_timer(self.SNAKE_MOVE, 200)

    def run_game(self):
        """Start main game loop."""
        while True:
            # waiting for a key or mouse button to be pressed.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.SNAKE_MOVE:
                    self.snake.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.change_direction != "RIGHT":
                        self.snake.change_direction = "LEFT"
                        self.snake.direction = Vector2(-1, 0)
                    if event.key == pygame.K_RIGHT and self.snake.change_direction != "LEFT":
                        self.snake.change_direction = "RIGHT"
                        self.snake.direction = Vector2(1, 0)
                    if event.key == pygame.K_UP and self.snake.change_direction != "DOWN":
                        self.snake.change_direction = "UP"
                        self.snake.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN and self.snake.change_direction != "UP":
                        self.snake.change_direction = "DOWN"
                        self.snake.direction = Vector2(0, 1)

            # changing surface color
            self.screen.fill(self.settings.background_color)

            # draw apple food
            self.apple.draw(self.settings, self.screen)

            # draw snake
            self.snake.draw(self.screen, self.settings)

            # draw horizontal lines
            for cell in range(1, self.settings.number_of_cells):
                pygame.draw.line(self.screen, pygame.Color('black'),Vector2(0, self.settings.cell_size * cell),
                                 Vector2(self.settings.cell_size * self.settings.number_of_cells,self.settings.cell_size * cell), 2)

            # draw vertical lines
            for cell in range(1, self.settings.number_of_cells):
                pygame.draw.line(self.screen, pygame.Color('black'), Vector2(self.settings.cell_size * cell, 0),
                                 Vector2(self.settings.cell_size * cell, self.settings.cell_size * self.settings.number_of_cells), 2)

            # checking collision snake with apple
            if self.snake.body[0] == self.apple.position:
                self.snake.eat = True
                self.apple.new_position = True
                # checking apple position is not in snake body
                while self.apple.new_position:
                    self.apple.position = self.apple.generate_random_position()
                    if self.apple.position not in self.snake.body:
                        self.apple.new_position = False

            # snake body collision with screen edges
            if (self.snake.body[0][0] == self.settings.number_of_cells or
                self.snake.body[0][1] == self.settings.number_of_cells or
                self.snake.body[0][0] == -1 or self.snake.body[0][1] == -1):
                self.snake.new_game()

            # snake body collision with tail
            for segment in self.snake.body[1:]:
                if segment == self.snake.body[0]:
                    self.snake.new_game()

            # Display the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    # create a copy of the game and run it
    game = Game()
    game.run_game()
