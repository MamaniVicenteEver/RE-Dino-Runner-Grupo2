from distutils.command.build import build
from signal import default_int_handler
import pygame

from dino_runner.utils.constants import RUNNING 
 
class Dinosaur() :
  X_POS = 80 
  Y_POS = 310 


  def __init__(self) -> None:
       self.image = RUNNING[0]
       self.dino_rect = self.image.get_rect()
       self.dino_rect.x = self.X_POS 
       self.dino_rect.y = self.Y_POS 
       self.step_index = 0
       self.patita_izquierda = True #implementation dino caminar


  def update(self):
        pass


  def draw(self , screen):
        screen.blit(self.image, ( self.dino_rect.x , self.dino_rect.y )) 


  def run(self):
      if self.step_index < 5 :#implementation dino caminar 
            self.patita_izquierda = not self.patita_izquierda
            self.step_index = 0
      if self.patita_izquierda:
             self.image = RUNNING[0] 
      else :
            self.image = RUNNING[1]#implementation dino caminar

      self.dino_rect = self.image.get_rect()
      self.dino_rect.x = self.X_POS
      self.dino_rect.y = self.Y_POS
      self.step_index +=1 
