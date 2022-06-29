import os
import sys
import pygame

from controllers.DatabaseController import get_highscore_list
from controllers.HelperController import draw_text
from views import menu


def show(clock, screen):
    click = False

    while True:

        screen.fill((0, 0, 0))

        draw_text(screen, f"test", 100, 0)

        data = get_highscore_list()

        for idx, row in enumerate(data):
            draw_text(screen, row[0], 100, (idx + 1) * 100)
            draw_text(screen, row[1], 400, (idx + 1) * 100)

        mx, my = pygame.mouse.get_pos()

        # load and render play button
        img = pygame.image.load(os.path.join('sprites/buttons', 'menu.png'))
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
