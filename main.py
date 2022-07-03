from controllers.DatabaseController import create_db
from models.Background import Background
from views import menu
import pygame

# pygame init + conf
pygame.init()
pygame.display.set_caption("Pinky vs. Pirates")
screen_width = 1800
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

bg = Background()

# create highscore db
create_db()

# show menu
menu.show(clock, screen, bg)
