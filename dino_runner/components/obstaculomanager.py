import pygame
import random
from dino_runner.components.cactus import Cactus
# from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.bird import Bird

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self,game):
        if len(self.obstacles) ==0:
            # self.obstacles.append(Cactus(SMALL_CACTUS) )
            self.obstacle_type_list = [Bird(), Cactus()]
            self.obstacles.append(random.choice(self.obstacle_type_list))

        for  obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if(game.player.dino_rect.colliderect(obstacle.rect) ):
                if not game.player.shield:
                  if not game.player.has_lives:
                    game.player_heart_manager.reduce_heart_count() #vidas descontando
                    if game.player_heart_manager.heart_count > 0:
                       game.player.has_lives = True
                       self.obstacles.pop()
                       start_transition_time = pygame.time.get_ticks()
                       game.player.lives_transition_time = start_transition_time + 1000
                    else:
                        pygame.time.delay(500)
                        game.playing = False 
                        game.death_count += 1# contador para el menu de texto
                        break 

    def draw(self, screen):
        for  obstacle in self.obstacles:
            obstacle.draw(screen) 

