import pygame

FONT_STYLE = 'freesansbold.ttf'
black_ =  (0,0,0)

def get_score_element(points):
     font = pygame.font.Font(FONT_STYLE,20)

     text = font.render("points:" + str(points), True , black_)
     text_rect = text.get_rect()
     text_rect.center = (900 , 70)

     return text , text_rect