from views import menu
import pygame

# todo known bugs: reject button spamming with timer, set timer after enemy hit

# pygame init + conf
pygame.init()
pygame.display.set_caption("Test")
screen_width = 1800
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

# show menu
menu.show(clock, screen)
