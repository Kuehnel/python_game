import os
import sys
import pygame

from controllers import helper
from views import menu


def show(clock, screen, hero):
    click = False

    while True:

        screen.fill((0, 0, 0))

        helper.draw_text(screen, f"Your Highscore: {hero.highscore}", 100, 100)

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
