import pygame

from kitbashing import StartKit, EndKit, HallwayKit
from models.Crabby import Crabby


def generate_level(level):
    start = StartKit.Start_kit()
    end = EndKit.End_kit()

    merge_tile_maps(level, start, HallwayKit.Hallway_kit())
    merge_tile_maps(level, level, HallwayKit.Hallway_kit())
    merge_tile_maps(level, level, end)

    tile_map_to_rect_array(level)

    level.coin_img = pygame.transform.scale(level.coin_img,
                                            (level.coin_img.get_width() * 3, level.coin_img.get_height() * 3))
    level.spikes_img = pygame.transform.scale(level.spikes_img,
                                              (level.spikes_img.get_width() * 2, level.spikes_img.get_height() * 2))
    level.goal_img = pygame.transform.scale(level.goal_img,
                                            (level.goal_img.get_width() * 3, level.goal_img.get_height() * 3))


# fill tile_maps with neutral rows until both connector rows have same index
def merge_tile_maps(level, start_kit, extension_kit):
    level.tile_map = [a + b for a, b in zip(start_kit.tile_map, extension_kit.tile_map)]
    # start_map_above_connector = start_kit.tile_map[0:start_kit.connector_index_r]
    # hallway_map_above_connector = extension_kit.tile_map[0:extension_kit.connector_index_l]
    #
    # start_map_under_connector = start_kit.tile_map[start_kit.connector_index_r + 1:]
    # hallway_map_under_connector = extension_kit.tile_map[extension_kit.connector_index_l + 1:]
    #
    # # evaluate which tile_map has more rows above the connector row and fill it up with neutral rows
    # len_diff_above = len(start_map_above_connector) - len(hallway_map_above_connector)  # positiv, dann start größer
    # # start > hallway
    # if len_diff_above > 0:
    #     for _ in range(len_diff_above):
    #         extension_kit.tile_map.insert(0, extension_kit.neutral_list)
    # # hallway > start
    # elif len_diff_above < 0:
    #     for _ in range(len_diff_above * -1):
    #         start_kit.tile_map.insert(0, start_kit.neutral_list)
    #
    # # evaluate which tile_map has more rows under the connector row and fill it up with neutral rows
    # len_diff_under = len(start_map_under_connector) - len(hallway_map_under_connector)  # positiv, dann start größer
    # # start > hallway
    # if len_diff_under > 0:
    #     for _ in range(len_diff_under):
    #         extension_kit.tile_map.append(extension_kit.neutral_list)
    # # hallway > start
    # elif len_diff_under < 0:
    #     for _ in range(len_diff_under * -1):
    #         start_kit.tile_map.append(start_kit.neutral_list)
    #
    # self.tile_map = [a + b for a, b in zip(start_kit.tile_map, extension_kit.tile_map)]
    # self.neutral_list = [0] * len(self.tile_map[0])
    #
    # # search for new connector row right after modifyin tile_map
    # index = 0
    # for row in self.tile_map:
    #     if row[-1] == 9:
    #         self.connector_index_r = index
    #         break
    #     index = index + 1


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
