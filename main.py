from controllers.DatabaseController import create_db, insert_highscore, get_highscore_list
from views import menu
import pygame

# pygame init + conf
pygame.init()
pygame.display.set_caption("Test")
screen_width = 1800
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

# create highscore db
create_db()

# show menu
menu.show(clock, screen)
