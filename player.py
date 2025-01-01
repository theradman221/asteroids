from circleshape import CircleShape
from constants import *
import pygame
# Player class for maintaining and drawing the player
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # draw the player on the provided screen
    def draw(self, screen):
        pygame.draw.polygon(surface = screen, color = "white", points = self.triangle(), width = 2)
        
    # Figure out the triangle coordinates
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            print(f"pressed the A Key")
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            print(f"pressed the D Key")
            self.rotate(dt)