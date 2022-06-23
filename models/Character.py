import pygame

from models.CharacterState import CharacterState


class Character:

    def __init__(self):
        self.x = 0
        self.y = 300
        self.velocity = 2
        self.width = 0
        self.height = 0

        self.line_of_sight = 1

        self.next_y = 0
        self.next_x = 0

        self.health = 100

        self.img = None
        self.img_clock = 0
        self.img_index = 0
        self.img_list = []
        self.state = CharacterState.IDLE

        self.idle_img_list = []
        self.run_img_list = []
        self.jump_img_list = []
        self.damaged_img_list = []
        self.attack_img_list = []

    def get_rect(self):
        pygame.Rect(self.x, self.y, self.width, self.height)

    def change_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            if self.state == CharacterState.RUN:
                self.img_list = self.run_img_list
            elif self.state == CharacterState.IDLE:
                self.img_list = self.idle_img_list
            elif self.state == CharacterState.JUMP:
                self.img_list = self.jump_img_list
            elif self.state == CharacterState.DAMAGED:
                self.img_list = self.damaged_img_list
            elif self.state == CharacterState.ATTACK:
                self.img_list = self.attack_img_list
            self.img_index = 0
