import sys
import pygame

from controllers.DatabaseController import get_highscore_list
from controllers.HelperController import draw_text, load_and_draw_image
from models.Background import Background
from views import menu


def show(clock, screen):
    click = False

    while True:

        Background().draw(screen)

        load_and_draw_image(screen, 'sprites/menu/boards', 'bg_board.png', 548, 40, 5.5)

        load_and_draw_image(screen, 'sprites/menu/boards', 'board.png', 580, 70, 5)

        load_and_draw_image(screen, 'sprites/menu/banner', 'highscore_banner.png', 548, 0, 5.5)

        data = get_highscore_list()

        for idx, row in enumerate(data):
            draw_text(screen, row[0], 700, 170 + (idx + 1) * 40, 18)
            draw_text(screen, row[1], 950, 170 + (idx + 1) * 40, 18)

        mx, my = pygame.mouse.get_pos()

        # load and render menu button
        btn_menu = load_and_draw_image(screen, 'sprites/menu/buttons', 'menu.png', 756, 750, 3)

        if btn_menu.collidepoint((mx, my)):
            if click:
                menu.show(clock, screen)

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
