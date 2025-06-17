import pygame
from constants import *
from player import Player

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0 # delta time

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    # clear the screen
    screen.fill("black")
    
    player.draw(screen)
    player.update(dt)

    # update the display
    pygame.display.flip()

    


if __name__ == "__main__":
  main()