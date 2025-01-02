# Imports
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # This automatically adds a new instance to the sprite Groups in main when it is created
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Check if there is a collision between this and other, if there is return True, else False
    def collision(self, other):
        distance_1 = other.position.distance_to(self.position)
        radius = self.radius + other.radius
        if distance_1 < radius:
            return True
        else:
            return False