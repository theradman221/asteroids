# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Create pygame Groups for the updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Add all new Players to the updatable and drawable groups and make a new Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (updatable,drawable,shots)

    # Create the asteroid field
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Before drawing anything black out the screen
        screen.fill("#000000")

        # Update all updatables
        dt = clock.tick(60)/ 1000
        for item in updatable:
            item.update(dt)

        # Check collisions
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                return # Quit the game if a collision with the player is detected
            
            # Kill the bullet and asteroid if there is a collision of an asteroid and a bullet, will eventually add splitting
            for bullet in shots:
                if item.collision(bullet):
                    item.split()
                    bullet.kill()

        # Draw all drawables
        for item in drawable:
            item.draw(screen)

        # Update the display last
        pygame.display.flip()





if __name__ == "__main__":
    main()