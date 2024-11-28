import pygame, random
# import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
         pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        splitted_radius = self.radius - ASTEROID_MIN_RADIUS
        # pygame.Vector2(random_angle, -random_angle).rotate(self.rotation)

        asteroid_1 = Asteroid(self.position.x, self.position.y, splitted_radius)
        asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, splitted_radius)
        asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2


