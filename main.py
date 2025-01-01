# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(dt)
                return
        screen.fill("#000000")
        dt = clock.tick(60)/ 1000
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()





if __name__ == "__main__":
    main()