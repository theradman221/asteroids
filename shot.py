# Imports
from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw a circle to represent each shot
    def draw(self, screen):
        pygame.draw.circle(screen, color = "white", center = self.position, radius = self.radius, width = 2)

    # Always move in a straight line
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    # Each update is just to move, keeping update / move to maintain consistensy with how other CircleShapes were designed
    def update(self, dt):
        self.move(dt)