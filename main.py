# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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
    
    # Add all new Players to the updatable and drawable groups and make a new Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        # Draw all drawables
        for item in drawable:
            item.draw(screen)

        # Update the display last
        pygame.display.flip()





if __name__ == "__main__":
    main()