import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
  def __init__(self ,image , type_):
    self.image = image #
    self.type_ = type_

    self.rect = self.image[self.type_].get_rect()
    self.rect.x = SCREEN_WIDTH
  
  def update(self , game_speed , obtacles):
    self.rect.x -= game_speed
    if(self.rect.x < -self.rect.width): 
      obtacles.pop()

  def draw(self , screen):
    screen.blit(self.image[self.type_],(self.rect))

