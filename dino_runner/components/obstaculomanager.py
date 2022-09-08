import random

from dino_runner.components.bird import Bird
from dino_runner.components.cactus import Cactus#averiguar

# from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
  def __init__(self):
    self.obstacles = []

  def update(self , game):
     if len(self.obstacles) == 0:
        self.obstacle_type_list = [Bird(), Cactus()]#averiguar 
        self.obstacles.append(random.choice(self.obstacle_type_list))#averiguar

      #  self.obstacles.append(Cactus(SMALL_CACTUS))
    
     for obstacle in self.obstacles:
        obstacle.update(game.game_speed , self.obstacles)
        if (game.player.dino_rect.colliderect(obstacle.rect)):
          # pygame.time.delay(500)
          game.playing = False
          break

  def draw(self , screen):
     for obstacle in self.obstacles:
      obstacle.draw(screen)
