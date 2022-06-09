import os

from controllers import game
import pygame
import sys


def show(clock, screen):
    click = False

    while True:

        screen.fill((0, 0, 0))

        # get mouse position
        mx, my = pygame.mouse.get_pos()

        # load and render play button
        img = pygame.image.load(os.path.join('sprites/buttons', 'play.png'))
        btn_play = img.get_rect()
        w, h = pygame.display.get_surface().get_size()
        btn_play.x = w / 2 - btn_play.width / 2
        btn_play.y = h / 2 - btn_play.height / 2
        screen.blit(img, btn_play)

        # event when play button clicked
        if btn_play.collidepoint((mx, my)):
            if click:
                game.start(clock, screen)

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
