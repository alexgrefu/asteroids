import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0 # delta time

  updateble = pygame.sprite.Group()
  drawble = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()


  Player.containers = (updateble, drawble)
  Shot.containers = (shots, updateble, drawble)
  Asteroid.containers = (asteroids, updateble, drawble)
  AsteroidField.containers = (updateble)


  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  while True:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    # clear the screen
    screen.fill("black")

    updateble.update(dt)
    
    for item in asteroids:
      if item.collision(player):
        print("Game over!")
        return

    for item in asteroids:
      for bullet in shots:
        if item.collision(bullet):
          item.split()
          bullet.kill()

    for item in drawble:
      item.draw(screen)
    
    pygame.display.flip()

    


if __name__ == "__main__":
  main()