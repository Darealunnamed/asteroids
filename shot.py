import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)

  def draw(self, screen):
    pygame.draw.circle(surface=screen, color=SHOT_COLOR, center=self.position, radius=SHOT_RADIUS, width=SHOT_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt