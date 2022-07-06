import os
import random

import pygame

from models.CharacterState import CharacterState
from models.Enemy import Enemy


# class that represents crabby
class Crabby(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.attack_strength = 40

        self.attack_time = random.randint(100, 500)
        self.attack_clock = 0

        self.collision_tolerance = 50

        self.movement_time = 50
        self.movement_clock = 0

        self.idle_time = random.randint(100, 500)
        self.idle_clock = 0

        self.width = 72 * 2
        self.height = 32 * 2

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

        self.run_img_list = [
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/run', '01.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/run', '02.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/run', '03.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/run', '04.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/run', '05.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
            pygame.transform.scale(
                pygame.image.load(os.path.join('sprites/enemies/crabby/run', '06.png')).convert_alpha(),
                (72 * 2, 32 * 2)),
        ]

        self.img_list = self.idle_img_list

    def get_rect(self):
        crabby_rect = pygame.Rect(self.x + self.collision_tolerance, self.y,
                                  self.width - self.collision_tolerance, self.height)
        if self.state == CharacterState.ATTACK:
            crabby_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return crabby_rect
