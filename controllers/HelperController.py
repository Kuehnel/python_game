import os
import sys

import pygame


def draw_text(screen, text, x, y, size):
    myfont = pygame.font.Font("font/8bit.ttf", size)
    label = myfont.render(text, True, (74, 73, 89))
    screen.blit(label, (x, y))


def load_and_draw_image(screen, folder, file_name, x, y, factor):
    img = pygame.image.load(os.path.join(folder, file_name))
    img = pygame.transform.scale(img, (img.get_width() * factor, img.get_height() * factor))
    btn_play = img.get_rect()
    btn_play.x = x
    btn_play.y = y
    screen.blit(img, btn_play)
    return btn_play


def load_image_scaled(folder, file_name, factor):
    img = pygame.image.load(os.path.join(folder, file_name))
    return pygame.transform.scale(img, (img.get_width() * factor, img.get_height() * factor)).convert_alpha()


# handle mouse + keyboard input
def handle_input():
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    return click
