import pygame

from models.HeroState import HeroState


class Hero:

    def __init__(self):
        self.x = 300
        self.y = 300
        self.velocity = 5
        self.width = 32
        self.height = 32

        self.jump_state = -16
        self.init_jumpstate = -16
        self.last_jump = 0

        self.dash_state = -16
        self.init_dash_state = -16
        self.dash_speed = 20
        self.last_dash = 0

        self.line_of_sight = 1

        self.grounded = False
        self.next_y = 0
        self.next_x = 0
        self.indeed_moved_x = 0
        self.collision_x = False
        self.collision_y = False

        self.health = 100
        self.damage_state = 0

        self.highscore = 0

        self.img = None
        self.img_index = 0
        self.img_list = []
        self.state = HeroState.IDLE

        self.idle_img_list = []
        self.run_img_list = []
        self.jump_img_list = []
        self.damaged_img_list = []

    def set_indeed_moved_x(self, new_x):
        self.indeed_moved_x = new_x - self.x

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
        if (now_in_ms - self.last_jump) > 500 and not self.is_jumping() and self.grounded:
            self.last_jump = now_in_ms
            return True

    def is_alive(self):
        if self.health > 0:
            return True



    def handle_collision_with_enemy(self, enemy_array):
        if self.is_damaged():
            if self.dash_state == 1:
                self.change_state(HeroState.IDLE)
            self.damage_state = self.damage_state - 1
            self.change_state(HeroState.DAMAGED)
        else:
            for rect in enemy_array:
                if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                        rect) and not self.is_dashing() and not self.is_damaged():
                    self.health -= 10  # todo set value enemy
                    self.damage_state = 60
                    self.change_state(HeroState.DAMAGED)

    def handle_collision_with_coin(self, generated_level):
        for rect in generated_level.coin_array:
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(rect):
                self.highscore += 1
                generated_level.coin_array.remove(rect)

    def handle_collision_with_environment(self, rect_array):
        next_hero_rect = pygame.Rect(self.x if self.next_x == 0 else self.next_x,
                                     self.y if self.next_y == 0 else self.next_y, self.width, self.height)

        collision_x = False
        collision_y = False

        for rect in rect_array:

            if next_hero_rect.colliderect(rect):

                self.grounded = False
                next_hero_rect_only_y = pygame.Rect(self.x, self.next_y, self.width, self.height)

                if self.next_y != 0 and next_hero_rect_only_y.colliderect(rect):
                    # collision bottom
                    if self.y < self.next_y:
                        if rect.top < next_hero_rect.bottom:
                            self.grounded = True
                            self.y = rect.top - self.height
                            collision_y = True
                    # collision top
                    if self.y > self.next_y:
                        if rect.bottom > next_hero_rect.top:
                            self.y = rect.bottom
                            print("collision top")
                            collision_y = True
                            if self.is_jumping():
                                self.jump_state = self.init_jumpstate

                next_hero_rect_only_x = pygame.Rect(self.next_x, self.y, self.width, self.height)
                if self.next_x != 0 and next_hero_rect_only_x.colliderect(rect):
                    # collision left
                    if self.x > self.next_x:
                        if rect.right > next_hero_rect.left:
                            self.set_indeed_moved_x(rect.right)
                            self.x = rect.right
                            print("collision left")
                            collision_x = True
                    # collision right
                    if self.x < self.next_x:
                        if rect.left < next_hero_rect.right:
                            self.set_indeed_moved_x(rect.left - self.width)
                            self.x = rect.left - self.width
                            print("collision right")
                            collision_x = True

        if not collision_x and self.next_x != 0:
            self.set_indeed_moved_x(self.next_x)
            self.x = self.next_x
        if not collision_y:
            self.y = self.next_y

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
