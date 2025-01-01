from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

# Player class for maintaining and drawing the player
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

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
    
    # Apply the Left / Right rotation to the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Look for inputs and apply either rotation or movement to the Player
    def update(self, dt):
        # Remove dt time until the next shot can be shot
        self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

    # Move the player Forward / Back
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Shoot a shot
    def shoot(self):
        if self.shoot_timer <= 0:
            shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1)
            shot.rotation = self.rotation
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        