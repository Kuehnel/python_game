import os

import pygame


def draw_text(screen, text, x, y):
    myfont = pygame.font.SysFont("Arial", 30)
    label = myfont.render(text, True, (0, 255, 255))
    screen.blit(label, (x, y))


def draw_image(screen, folder, file_name, x, y):
    img = pygame.image.load(os.path.join(folder, file_name))
    img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
    btn_play = img.get_rect()
    btn_play.x = x
    btn_play.y = y
    screen.blit(img, btn_play)

    return btn_play
