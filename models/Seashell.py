import os

import pygame

from models.Enemy import Enemy


class Seashell(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.attack_strength = 40

        self.attack_time = 70
        self.attack_clock = 0

        self.bullet = None

        self.idle_time = 300
        self.idle_clock = 0

        self.width = 48
        self.height = 38

        self.pearl_img = pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/pearl', '1.png')).convert_alpha(),
                (32, 32))

        self.idle_img_list = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/idle', '1.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
        ]
        self.attack_img_list = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/attack', '1.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/attack', '2.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/attack', '3.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/attack', '4.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/attack', '5.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/seashell/attack', '6.png')).convert_alpha(),
                (self.width * 2, self.height * 2)),
        ]

        self.img_list = self.idle_img_list
