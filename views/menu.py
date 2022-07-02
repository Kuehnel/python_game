from controllers.GameController import start
import pygame
import sys

from controllers.HelperController import load_and_draw_image, handle_input
from controllers.SoundController import play_main_theme, navigation_sound
from models.Hero import Hero
from views import highscore


def show(clock, screen, bg):
    click = False

    play_main_theme()

    while True:

        bg.draw(screen)

        # get mouse position
        mx, my = pygame.mouse.get_pos()
        button_position_x = 756

        # load and render images
        load_and_draw_image(screen, 'sprites/menu/banner', 'title_banner.png', 650, 40, 4)
        btn_play = load_and_draw_image(screen, 'sprites/menu/buttons', 'play.png', button_position_x, 400, 3)
        btn_highscore = load_and_draw_image(screen, 'sprites/menu/buttons', 'highscore.png', button_position_x, 550, 3)
        btn_quit = load_and_draw_image(screen, 'sprites/menu/buttons', 'quit.png', button_position_x, 700, 3)

        # event when button clicked
        if click:
            navigation_sound()
            if btn_play.collidepoint((mx, my)):
                start(clock, screen, Hero())
            if btn_highscore.collidepoint((mx, my)):
                highscore.show(clock, screen, bg)
            if btn_quit.collidepoint((mx, my)):
                pygame.quit()
                sys.exit()

        click = handle_input()

        pygame.display.update()
        clock.tick(60)
