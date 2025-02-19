from player import Player
from constants import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updateable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  dt = 0
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill((0, 0, 0))
    updateable.update(dt)
    for obj in drawable:
      obj.draw(screen)
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()