# Imports
from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y ,radius):
        super().__init__(x, y, radius)

    # Method to draw the asteroid on screen
    def draw(self, screen):
        pygame.draw.circle(screen, color = "white", center = self.position, radius = self.radius, width = 2)
    
    # Every update keep it moving in a constant direction
    def update(self, dt):
        self.position += self.velocity * dt

    # Split a larger asteroid into smaller ones when hit with a Shot
    def split(self):
        self.kill() # Kill the asteroid that got hit
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # don't split asteroid that are small

        # Get info for each new asteroid
        angle = random.uniform(20,50)
        asteroid_1_velocity = self.velocity.rotate(angle)
        asteroid_2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create 2 new asteroids
        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_1.velocity = asteroid_1_velocity * 1.2
        asteroid_2.velocity = asteroid_2_velocity * 1.2

