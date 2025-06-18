import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle =random.uniform(20, 50)
      first_direction = self.velocity.rotate(random_angle)
      second_direction = self.velocity.rotate(-random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
      second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
      first_new_asteroid.velocity = first_direction
      second_new_asteroid.velocity = second_direction
