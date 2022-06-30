import os
import sys
import pygame

from controllers.DatabaseController import insert_highscore
from controllers.HelperController import draw_text
from models.Background import Background
from views import menu


def show(clock, screen, hero):
    click = False

    insert_highscore(hero.highscore)

    while True:

        Background().draw(screen)

        draw_text(screen, f"Your Highscore: {hero.highscore}", 100, 100, 20)

        mx, my = pygame.mouse.get_pos()

        # load and render play button
        img = pygame.image.load(os.path.join('sprites/menu/buttons', 'menu.png'))
        btn_menu = img.get_rect()
        w, h = pygame.display.get_surface().get_size()
        btn_menu.x = w / 2 - btn_menu.width / 2
        btn_menu.y = h / 2 - btn_menu.height / 2
        screen.blit(img, btn_menu)

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
