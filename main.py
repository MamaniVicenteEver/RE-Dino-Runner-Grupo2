import pygame
from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game() #

#controlar una serie de ejecuciones 
    while game.running :
        if not game.playing :#controlando los estados 
            game.show_menu(game.death_count)
