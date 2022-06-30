import os
import sys
import pygame

from controllers.DatabaseController import insert_highscore
from controllers.HelperController import draw_text, load_and_draw_image
from models.Background import Background
from views import menu


def show(clock, screen, hero):
    click = False

    insert_highscore(hero.highscore)

    while True:

        Background().draw(screen)

        load_and_draw_image(screen, 'sprites/menu/boards', 'bg_board.png', 548, 40, 5.5)
        load_and_draw_image(screen, 'sprites/menu/boards', 'board.png', 580, 70, 5)
        load_and_draw_image(screen, 'sprites/menu/banner', 'gameover_banner.png', 548, 0, 5.5)

        draw_text(screen, f"Your Score:", 680, 240, 22)
        draw_text(screen, f"{hero.highscore}", 880, 300, 30)

        draw_text(screen, "\"May your anchor be tight,", 680, 400, 18)
        draw_text(screen, "your cork be loose,", 680, 440, 18)
        draw_text(screen, "your rum be spiced and", 680, 480, 18)
        draw_text(screen, "your compass be true.\"", 680, 520, 18)
        draw_text(screen, "- Danny Taddei -", 680, 560, 18)

        mx, my = pygame.mouse.get_pos()

        # load and render play button
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
