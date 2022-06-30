from controllers.GameController import start
import pygame
import sys

from controllers.HelperController import draw_image
from models.Hero import Hero
from views import highscore


def show(clock, screen):
    click = False

    while True:

        screen.fill((0, 0, 0))

        # get mouse position
        mx, my = pygame.mouse.get_pos()
        w, h = pygame.display.get_surface().get_size()
        button_position_x = 756

        # load and render play button
        btn_play = draw_image(screen, 'sprites/menu/buttons', 'play.png', button_position_x, 400)

        # load and render highscore button
        btn_highscore = draw_image(screen, 'sprites/menu/buttons', 'highscore.png', button_position_x, 550)

        # load and render quit button
        btn_quit = draw_image(screen, 'sprites/menu/buttons', 'quit.png', button_position_x, 700)

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
