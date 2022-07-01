import os
import random

import pygame

from controllers.HelperController import load_image_scaled


class Background:

    def __init__(self):
        self.pointer_x = 0
        self.pointer_y = 0

        self.palmtree_array = []

        self.bg_img = pygame.image.load(os.path.join('sprites/island/background', 'background.png')).convert_alpha()
        self.big_clouds_img = load_image_scaled('sprites/island/background', 'big_clouds.png', 4.1)

        self.palmtree_img = load_image_scaled('sprites/island/background/palmtree', '01.png', 5)

    def init_palmtree_array(self):
        for i in range(3):
            random_number = random.randint(10, 1790)
            self.palmtree_array.append(pygame.Rect(random_number, 480, 64, 64))

    def draw(self, screen, hero=None):
        screen.blit(self.bg_img, (0, 0))
        screen.blit(self.big_clouds_img, (0, 200))

        if hero:
            for palmtree in self.palmtree_array:
                palmtree.x = palmtree.x - hero.indeed_moved_x
                screen.blit(self.palmtree_img, (palmtree.x, palmtree.y))
