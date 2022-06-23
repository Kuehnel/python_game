import pygame

from models.HeroState import HeroState


class Hero:

    def __init__(self):
        self.x = 300
        self.y = 300
        self.velocity = 2
        self.width = 64
        self.height = 64

        self.jump_state = -16
        self.init_jumpstate = -16
        self.last_jump = 0

        self.dash_state = -16
        self.init_dash_state = -16
        self.dash_speed = 20
        self.last_dash = 0

        self.line_of_sight = 1

        self.grounded = False
        self.next_y = 300
        self.next_x = 300
        self.indeed_moved_x = 0
        self.collision_x = False
        self.collision_y = False

        self.health = 100
        self.damage_state = 0

        self.highscore = 0

        self.img = None
        self.img_clock = 0
        self.img_index = 0
        self.img_list = []
        self.state = HeroState.IDLE

        self.idle_img_list = []
        self.run_img_list = []
        self.jump_img_list = []
        self.damaged_img_list = []


    def is_damaged(self):
        if self.damage_state > 0:
            return True
        return False

    def is_dashing(self):
        if self.dash_state > self.init_dash_state:
            return True

    def allowed_to_dash(self):
        now_in_ms = pygame.time.get_ticks()
        if (now_in_ms - self.last_dash) > 1000 and not self.is_dashing():
            self.last_dash = now_in_ms
            return True

    def is_jumping(self):
        if self.jump_state > self.init_jumpstate:
            return True

    def allowed_to_jump(self):
        now_in_ms = pygame.time.get_ticks()
        if (now_in_ms - self.last_jump) > 750 and not self.is_jumping():
            self.last_jump = now_in_ms
            return True

    def is_alive(self):
        if self.health > 0:
            return True

    def change_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            if self.state == HeroState.RUN:
                self.img_list = self.run_img_list
            elif self.state == HeroState.IDLE:
                self.img_list = self.idle_img_list
            elif self.state == HeroState.JUMP:
                self.img_list = self.jump_img_list
            elif self.state == HeroState.DAMAGED:
                self.img_list = self.damaged_img_list
            self.img_index = 0
