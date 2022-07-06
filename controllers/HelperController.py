import os
import sys

import pygame


def draw_text(screen, text, x, y, size):
    myfont = pygame.font.Font("font/8bit.ttf", size)
    label = myfont.render(text, True, (74, 73, 89))
    screen.blit(label, (x, y))


def draw_image(screen, img, x, y):
    img_rect = img.get_rect()
    img_rect.x = x
    img_rect.y = y
    screen.blit(img, img_rect)
    return img_rect


def load_and_draw_image(screen, folder, file_name, x, y, factor, image_dictionary):
    if file_name in image_dictionary:
        img = image_dictionary[file_name]
    else:
        img = pygame.image.load(os.path.join(folder, file_name))
        img = pygame.transform.scale(img, (img.get_width() * factor, img.get_height() * factor))
        image_dictionary[file_name] = img
    img_rect = img.get_rect()
    img_rect.x = x
    img_rect.y = y
    screen.blit(img, img_rect)
    return img_rect


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
