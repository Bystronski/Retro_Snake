import pygame
from pygame import Vector2

class Snake:
    """Class intended for snake management"""
    def __init__(self):
        """Initialization of the snake and its position."""
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]

    def draw(self, screen, settings):
        """Draws the snake on the screen."""
        for segment in self.body:
            snake_rect = pygame.Rect(segment.x * settings.cell_size, segment.y * settings.cell_size, settings.cell_size + 2, settings.cell_size + 2)
            pygame.draw.rect(screen, (98, 156, 68), snake_rect)
