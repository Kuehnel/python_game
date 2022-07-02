import os

import pygame

from models.Character import Character
from models.Spritesheet import Spritesheet


class Hero(Character):

    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 700
        self.width = 64
        self.height = 64
        self.collision_tolerance = 9

        self.jump_state = -16
        self.init_jumpstate = -16
        self.last_jump = 0

        self.grounded = False
        self.next_y = 300
        self.next_x = 300
        self.indeed_moved_x = 0

        self.health = 225
        self.damage_state = 0

        self.highscore = 0

        self.load_images()

        self.img_list = self.idle_img_list


    def is_damaged(self):
        if self.damage_state > 0:
            return True
        return False

    def is_jumping(self):
        if self.jump_state > self.init_jumpstate:
            return True

    def allowed_to_jump(self):
        now_in_ms = pygame.time.get_ticks()
        if (now_in_ms - self.last_jump) > 650 and not self.is_jumping():
            self.last_jump = now_in_ms
            return True

    def is_alive(self):
        if self.health > 0 and self.y < 900:
            return True

    def load_images(self):
        hero_idle_sheet = Spritesheet(pygame.image.load(os.path.join('sprites/hero', 'hero_idle.png')).convert_alpha())
        self.idle_img_list = [hero_idle_sheet.get_image(0, 32, 32, 2), hero_idle_sheet.get_image(1, 32, 32, 2),
                              hero_idle_sheet.get_image(2, 32, 32, 2), hero_idle_sheet.get_image(3, 32, 32, 2)]

        hero_run_sheet = Spritesheet(pygame.image.load(os.path.join('sprites/hero', 'hero_run.png')).convert_alpha())
        self.run_img_list = [hero_run_sheet.get_image(0, 32, 32, 2), hero_run_sheet.get_image(1, 32, 32, 2),
                             hero_run_sheet.get_image(2, 32, 32, 2), hero_run_sheet.get_image(3, 32, 32, 2),
                             hero_run_sheet.get_image(4, 32, 32, 2), hero_run_sheet.get_image(5, 32, 32, 2)]

        hero_jump_sheet = Spritesheet(pygame.image.load(os.path.join('sprites/hero', 'hero_jump.png')).convert_alpha())
        self.jump_img_list = [hero_jump_sheet.get_image(0, 32, 32, 2), hero_jump_sheet.get_image(1, 32, 32, 2),
                              hero_jump_sheet.get_image(2, 32, 32, 2), hero_jump_sheet.get_image(3, 32, 32, 2),
                              hero_jump_sheet.get_image(4, 32, 32, 2), hero_jump_sheet.get_image(5, 32, 32, 2),
                              hero_jump_sheet.get_image(6, 32, 32, 2), hero_jump_sheet.get_image(9, 32, 32, 2)]

        hero_damaged_sheet = Spritesheet(
            pygame.image.load(os.path.join('sprites/hero', 'hero_damaged.png')).convert_alpha())
        self.damaged_img_list = [hero_damaged_sheet.get_image(0, 32, 32, 2), hero_damaged_sheet.get_image(1, 32, 32, 2),
                                 hero_damaged_sheet.get_image(2, 32, 32, 2), hero_damaged_sheet.get_image(3, 32, 32, 2)]
