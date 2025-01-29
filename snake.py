import pygame
from pygame import Vector2

class Snake:
    """Class intended for snake management"""
    def __init__(self):
        """Initialization of the snake and its position."""
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.change_direction = "RIGHT"
        self.eat = False

    def draw(self, screen, settings):
        """Draws the snake on the screen."""
        for segment in self.body:
            snake_rect = pygame.Rect(segment.x * settings.cell_size, segment.y * settings.cell_size, settings.cell_size + 2, settings.cell_size + 2)
            pygame.draw.rect(screen, (255, 168, 52), snake_rect)

    def update(self):
        """Updates the snake position."""
        if self.eat:
            self.body.insert(0,self.body[0] + self.direction)
            self.eat = False
        else:
            self.body = self.body[:-1]
            self.body.insert(0,self.body[0] + self.direction)


