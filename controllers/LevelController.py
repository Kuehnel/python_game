import random

import pygame

from kitbashing.KitCollection import KitCollection
from models.Crabby import Crabby


def generate_random_level(level):
    kit_collection = KitCollection()

    # get all class attributes (instance attributes are excluded)
    all_class_tiles = [i for i in KitCollection.__dict__.keys() if i[:1] != '_']

    # get x random numbers in range of 'all:class_tiles'
    all_class_tiles_length = len(all_class_tiles)

    level.tile_map = kit_collection.start_kit_tile_map

    for i in range(3):
        random_num = random.randint(0, all_class_tiles_length - 1)
        level.merge_tile_maps(getattr(kit_collection, all_class_tiles[random_num]))

    level.merge_tile_maps(kit_collection.end_kit_tile_map)

    tile_map_to_rect_array(level)

    level.coin_img = pygame.transform.scale(level.coin_img,
                                            (level.coin_img.get_width() * 3, level.coin_img.get_height() * 3))
    level.spikes_img = pygame.transform.scale(level.spikes_img,
                                              (level.spikes_img.get_width() * 2, level.spikes_img.get_height() * 2))
    level.goal_img = pygame.transform.scale(level.goal_img,
                                            (level.goal_img.get_width() * 3, level.goal_img.get_height() * 3))


def tile_map_to_rect_array(self):
    for row in self.tile_map:
        for column in row:
            if column == 1:
                # add floor
                self.tile_array.append(
                    [pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size, self.tile_size), 1])
            if column == 2:
                # add enemy
                self.trap_array.append(
                    [pygame.Rect(self.pointer_x, self.pointer_y + self.tile_size_small, self.tile_size_small,
                                 self.tile_size_small), 2])
            if column == 3:
                # add wall
                self.tile_array.append(
                    [pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size_small, self.tile_size), 3])
            if column == 4:
                # add crabby
                self.crabby_array.append(
                    Crabby(self.pointer_x - self.tile_size_small, self.pointer_y + self.tile_size_small + 7))
            if column == 5:
                # add wall ceiling
                self.tile_array.append(
                    [pygame.Rect(self.pointer_x, self.pointer_y + self.tile_size - self.tile_size_small, self.tile_size,
                                 self.tile_size_small), 5])
            if column == 6:
                # add coin
                self.coin_array.append(
                    pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size_small, self.tile_size_small))
            if column == 7:
                # add platform
                self.tile_array.append(
                    [pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size, self.tile_size_small), 7])
            if column == 8:
                # add goal
                self.goal_rect = pygame.Rect(self.pointer_x + self.tile_size_small, self.pointer_y,
                                             self.tile_size_small, self.tile_size)
            if column == 9:
                # add block
                self.tile_array.append(
                    [pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size, self.tile_size), 9])
            self.pointer_x += self.tile_size
        self.pointer_x = 0
        self.pointer_y += self.tile_size
