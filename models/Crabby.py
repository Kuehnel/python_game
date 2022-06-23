import os

import pygame

from models.CharacterState import CharacterState
from models.Enemy import Enemy


class Crabby(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.attack_strength = 20

        self.width = 72
        self.height = 32

        self.idle_img_list = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '01.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '02.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '03.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '04.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '05.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '06.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '07.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '08.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/idle', '09.png')).convert_alpha(),
                (72 * 2, 32 * 2)),

        ]
        self.attack_img_list = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/attack', '01.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/attack', '02.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/attack', '03.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/attack', '04.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
        ]

        self.img_list = self.idle_img_list
