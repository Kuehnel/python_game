import sys
import pygame
from views import menu


def show(clock, screen, hero):
    click = False

    while True:

        screen.fill((0, 0, 255))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                menu.show(clock, screen)
        pygame.draw.rect(screen, (255, 0, 0), button_1)

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
