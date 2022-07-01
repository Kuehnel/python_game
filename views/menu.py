from controllers.GameController import start
import pygame
import sys

from controllers.HelperController import load_and_draw_image
from controllers.SoundController import play_main_theme
from models.Background import Background
from models.Hero import Hero
from views import highscore


def show(clock, screen):
    click = False

    play_main_theme()

    while True:

        Background().draw(screen)

        # get mouse position
        mx, my = pygame.mouse.get_pos()
        w, h = pygame.display.get_surface().get_size()
        button_position_x = 756

        # load and render play button
        btn_play = load_and_draw_image(screen, 'sprites/menu/buttons', 'play.png', button_position_x, 400, 3)

        # load and render highscore button
        btn_highscore = load_and_draw_image(screen, 'sprites/menu/buttons', 'highscore.png', button_position_x, 550, 3)

        # load and render quit button
        btn_quit = load_and_draw_image(screen, 'sprites/menu/buttons', 'quit.png', button_position_x, 700, 3)

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
