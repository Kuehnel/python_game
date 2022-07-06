import pygame

from controllers.DatabaseController import get_highscore_list
from controllers.HelperController import draw_text, load_and_draw_image, handle_input
from controllers.SoundController import navigation_sound
from views import menu


# show highscores
def show(clock, screen, bg):
    click = False
    image_dictionary = {}

    while True:

        bg.draw(screen)

        load_and_draw_image(screen, 'sprites/menu/boards', 'bg_board.png', 548, 40, 5.5, image_dictionary)
        load_and_draw_image(screen, 'sprites/menu/boards', 'board.png', 580, 70, 5, image_dictionary)
        load_and_draw_image(screen, 'sprites/menu/banner', 'highscore_banner.png', 548, 0, 5.5, image_dictionary)

        data = get_highscore_list()

        for idx, row in enumerate(data):
            draw_text(screen, row[0], 700, 170 + (idx + 1) * 40, 18)
            draw_text(screen, row[1], 950, 170 + (idx + 1) * 40, 18)

        mx, my = pygame.mouse.get_pos()

        # load and render menu button
        btn_menu = load_and_draw_image(screen, 'sprites/menu/buttons', 'menu.png', 756, 750, 3, image_dictionary)

        if btn_menu.collidepoint((mx, my)):
            if click:
                navigation_sound()
                menu.show(clock, screen, bg)

        click = handle_input()

        pygame.display.update()
        clock.tick(60)
