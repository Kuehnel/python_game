import os

from controllers.GameController import start
import pygame
import sys

from models.Hero import Hero
from views import highscore


def show(clock, screen):
    click = False

    while True:

        screen.fill((0, 0, 0))

        # get mouse position
        mx, my = pygame.mouse.get_pos()
        w, h = pygame.display.get_surface().get_size()

        # load and render play button
        img = pygame.image.load(os.path.join('sprites/buttons', 'play.png'))
        btn_play = img.get_rect()
        btn_play.x = 100
        btn_play.y = 100
        screen.blit(img, btn_play)

        # load and render highscore button
        img = pygame.image.load(os.path.join('sprites/buttons', 'play.png'))
        btn_highscore = img.get_rect()
        btn_highscore.x = 100
        btn_highscore.y = 400
        screen.blit(img, btn_highscore)

        # load and render quit button
        img = pygame.image.load(os.path.join('sprites/buttons', 'quit.png'))
        btn_quit = img.get_rect()
        btn_quit.x = 100
        btn_quit.y = 700
        screen.blit(img, btn_quit)

        # event when button clicked
        if click:
            if btn_play.collidepoint((mx, my)):
                start(clock, screen, Hero())
            if btn_highscore.collidepoint((mx, my)):
                highscore.show(clock, screen)
            if btn_quit.collidepoint((mx, my)):
                pygame.quit()
                sys.exit()

        # handle mouse + keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)
