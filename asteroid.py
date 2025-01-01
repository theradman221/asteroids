# Import the required modules
from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)

    # Method to draw the asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, color = "white", center = self.position, radius = self.radius, width = 2)
    
    # Every update keep it moving in a constant direction
    def update(self, dt):
        self.position += self.velocity * dt

    
