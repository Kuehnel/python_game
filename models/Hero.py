import pygame

from models.Character import Character


class Hero(Character):

    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 300
        self.width = 64
        self.height = 64
        self.collision_tolerance = 9

        self.jump_state = -16
        self.init_jumpstate = -16
        self.last_jump = 0

        self.dash_state = -16
        self.init_dash_state = -16
        self.dash_speed = 20
        self.last_dash = 0

        self.grounded = False
        self.next_y = 300
        self.next_x = 300
        self.indeed_moved_x = 0

        self.health = 100
        self.damage_state = 0

        self.highscore = 0


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
