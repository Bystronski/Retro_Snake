import pygame, random
from pygame import Vector2

class Food:
    """Class intended for apple management."""
    def __init__(self):
        """Initialization of the apple and its position."""
        self.position = self.generate_random_position()
        self.new_position = False

    def draw(self, settings, screen):
        """Display the apple in its current position."""
        food_rect = pygame.Rect(self.position.x * settings.cell_size, self.position.y * settings.cell_size, settings.cell_size + 2, settings.cell_size + 2)
        pygame.draw.rect(screen, (230, 22, 16), food_rect)

    def generate_random_position(self ):
        """Generate a random position."""
        x = random.randint(0,24)
        y = random.randint(0,24)
        return Vector2(x,y)
