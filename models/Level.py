import os

import pygame

from controllers.HelperController import load_image_scaled


class Level:

    def __init__(self):
        self.pointer_x = 0
        self.pointer_y = 100

        self.tile_size = 96
        self.tile_size_small = 32

        self.tile_map = []
        self.tile_array = []

        self.trap_array = []
        self.crabby_array = []
        self.seashell_array = []
        self.coin_array = []

        self.goal_rect = None

        self.lifebar_img = load_image_scaled('sprites/hero/hud', 'lifebar.png', 3)
        self.platform_img = pygame.image.load(os.path.join('sprites/island', 'platform.png')).convert_alpha()
        self.coin_img = load_image_scaled('sprites/collectables', 'coin.png', 3)
        self.spikes_img = pygame.image.load(os.path.join('sprites/traps', 'spikes.png')).convert_alpha()
        self.floor_img = pygame.image.load(os.path.join('sprites/island', 'floor.png')).convert_alpha()
        self.block_img = pygame.image.load(os.path.join('sprites/island', 'block.png')).convert_alpha()
        self.wall_img = pygame.image.load(os.path.join('sprites/island', 'wall.png')).convert_alpha()
        self.goal_img = load_image_scaled('sprites/island', 'goal.png', 3)
        self.ship_img = load_image_scaled('sprites/island', 'ship.png', 12)

    def merge_tile_maps(self, next_tile_map):
        self.tile_map = [a + b for a, b in zip(self.tile_map, next_tile_map)]

