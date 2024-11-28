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
    counter = 0

    # Initialize font for the scoreboard
    pygame.font.init()
    font = pygame.font.Font(None, 36)  # Default font with size 36

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

    backgroud = pygame.image.load("pictures/purple-space-background-1440-x-1280-7j71thopjowyueye.webp")
    backgroud = pygame.transform.scale(backgroud, (SCREEN_WIDTH, SCREEN_HEIGHT))
    backgroud.set_alpha(120)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        screen.blit(backgroud, (0, 0))

        # screen.fill(backgroud)

        # Update all updatable sprites
        for update in updatable:
            update.update(dt)

        # Check collisions
        for asteroid in group_asteroid:
            if asteroid.collision(player):
                print(f"Game over! Your score: {counter}")
                sys.exit()
            for shot in group_shoot:
                if shot.collision(asteroid):
                    shot.kill()                  
                    counter += asteroid.split()

        # Draw all drawable sprites
        for drawn in drawable:
            drawn.draw(screen)

        # Render the score and display it at the top-right corner
        score_text = font.render(f"Score: {counter}", True, (255, 255, 255))  # White text
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))  # 10px padding from top-right

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main() 
