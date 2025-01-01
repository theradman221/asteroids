import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    """
    The AsteroidField class manages the continuous spawning of asteroids
    at random edges of the screen, sending them into the playable space
    with randomized velocity, size, and optional rotation.

    It extends pygame.sprite.Sprite to integrate seamlessly
    with the pygame sprite system. The class provides a
    flexible configuration for spawn rates, edges, and more.
    """

    # Predefined edges with direction vectors and spawn-position lambdas
    # The direction vector is used to define velocity, while the lambda
    # defines a random position along that edge.
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """
        Initializes the AsteroidField sprite, setting up the internal timer
        used for spawning asteroids on a fixed schedule.
        """
        # Register with the containers set by the main game
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.spawn_rate = ASTEROID_SPAWN_RATE  # allows for dynamic adjustments

    def spawn(self, radius, position, velocity):
        """
        Spawns a single asteroid with the given radius, position, and velocity.

        :param radius: float - radius of the new asteroid
        :param position: pygame.Vector2 - x, y spawn coordinates
        :param velocity: pygame.Vector2 - velocity vector
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

        # Optional random rotation speed for more variety
        asteroid.spin_speed = random.uniform(-ASTEROID_SPIN_MAX, ASTEROID_SPIN_MAX)
        # If you want random coloring or type, do it here:
        # asteroid.color = random.choice( [ (255,0,0), (0,255,0), (0,0,255) ] )

    def spawn_cluster(self, base_position, cluster_size=3):
        """
        Spawns a small cluster of asteroids around a base position for a
        chaotic surprise effect.

        :param base_position: pygame.Vector2 - the cluster's approximate center
        :param cluster_size: int - number of asteroids in the cluster
        """
        for _ in range(cluster_size):
            offset = pygame.Vector2(
                random.uniform(-CLUSTER_RADIUS, CLUSTER_RADIUS),
                random.uniform(-CLUSTER_RADIUS, CLUSTER_RADIUS),
            )
            cluster_pos = base_position + offset
            cluster_speed = random.randint(40, 100)
            # direction is random
            direction = pygame.Vector2(1, 0).rotate(random.randint(0, 359))
            velocity = direction * cluster_speed
            radius = random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MIN_RADIUS * ASTEROID_KINDS)
            self.spawn(radius, cluster_pos, velocity)

    def update(self, dt):
        """
        Handles the regular updates for the AsteroidField,
        spawning new asteroids on a timed interval.

        :param dt: float - delta time since last update call
        """
        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_rate:
            self.spawn_timer = 0.0

            # Randomly decide if we spawn a single asteroid or a cluster
            spawn_as_cluster = random.random() < CLUSTER_SPAWN_CHANCE

            if spawn_as_cluster:
                # Spawn a cluster around a random edge position
                edge = random.choice(self.edges)
                base_position = edge[1](random.uniform(0, 1))
                self.spawn_cluster(base_position, cluster_size=random.randint(2, 5))
            else:
                # Single-asteroid spawn path
                edge = random.choice(self.edges)

                speed = random.randint(40, 100)
                velocity = edge[0] * speed
                # slight random rotation of velocity
                velocity = velocity.rotate(random.randint(-30, 30))

                position = edge[1](random.uniform(0, 1))

                # pick an asteroid kind
                kind = random.randint(1, ASTEROID_KINDS)
                radius = ASTEROID_MIN_RADIUS * kind
                self.spawn(radius, position, velocity)
