from signal import default_int_handler
import pygame

from dino_runner.utils.constants import BIRD

class Bird() :
  X_POS = 880
  Y_POS = 260
  x_birt = 25
  def __init__(self) -> None:
       self.image = BIRD[0]
       self.dino_rect = self.image.get_rect()
       self.dino_rect.x = self.X_POS
       self.dino_rect.y = self.Y_POS
       self.step_index = 0
       self.feet_movement = True

  def update(self):
        pass

  def draw(self , screen):
        screen.blit(self.image, ( self.dino_rect.x , self.dino_rect.y ))

  def run(self):
        if self.step_index < 5 :
          self.feet_movement = not self.feet_movement
          self.step_index = 0
        if self.feet_movement:
          self.image = BIRD[0]
        else:
          self.image = BIRD[1]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1
        self.X_POS -= self.x_birt
