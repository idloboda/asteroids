import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
import player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} px")
    print(f"Screen height: {SCREEN_HEIGHT} px")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # Groups
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    group_asteroid = pygame.sprite.Group()
    group_shoot = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (group_asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (group_shoot, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for thing in updatable:
            thing.update(dt)

        for thing in group_asteroid:
            if thing.collision(player):
                print("Game over!")
                sys.exit()

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()