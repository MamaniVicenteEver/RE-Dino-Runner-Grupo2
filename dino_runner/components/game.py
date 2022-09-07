

import pygame
from dino_runner.components import text_utils
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.bird import Bird

from dino_runner.components.obstaculomanager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        #                                         alto y ancho
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.point = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart = PlayerHeartManager()
    
        self.bird_ = Bird()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.run()
        self.bird_.run()
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.bird_.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart.draw(self.screen)

        self.score()

        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):#aumentando la velocidad
        self.point += 1
        score , score_rect = text_utils.get_score_element(self.point)
        self.screen.blit(score , score_rect)