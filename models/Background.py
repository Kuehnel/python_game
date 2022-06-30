import os

import pygame

from controllers.HelperController import load_image_scaled


class Background:

    def __init__(self):
        self.pointer_x = 0
        self.pointer_y = 0

        self.bg_img = pygame.image.load(os.path.join('sprites/island/background', 'background.png')).convert_alpha()
        self.big_clouds_img = load_image_scaled('sprites/island/background', 'big_clouds.png', 4.1).convert_alpha()

        self.big_clouds_position_x = 100

    def draw(self, screen):
        screen.blit(self.bg_img, (0, 0))
        screen.blit(self.big_clouds_img, (0, 200))
