import os

import pygame

from controllers.HelperController import draw_text
from kitbashing import StartKit, EndKit, HallwayKit


class Level:

    def __init__(self):
        self.pointer_x = 0
        self.pointer_y = 100

        self.tile_size = 96
        self.tile_size_small = 32

        self.tile_map = []
        self.connector_index_r = -1
        self.neutral_list = []

        self.tile_array = []

        self.enemy_array = []

        self.coin_array = []

        self.goal_rect = []

        self.bg_img = pygame.image.load(os.path.join('sprites/island/background', 'background.png')).convert_alpha()
        self.platform_img = pygame.image.load(os.path.join('sprites/island', 'platform.png')).convert_alpha()
        self.coin_img = pygame.image.load(os.path.join('sprites/collectables', 'coin.png')).convert_alpha()
        self.spikes_img = pygame.image.load(os.path.join('sprites/enemies', 'spikes.png')).convert_alpha()
        self.floor_img = pygame.image.load(os.path.join('sprites/island', 'floor.png')).convert_alpha()
        self.floor_left_img = pygame.image.load(os.path.join('sprites/island', 'floor_left.png')).convert_alpha()
        self.block_img = pygame.image.load(os.path.join('sprites/island', 'block.png')).convert_alpha()
        self.wall_img = pygame.image.load(os.path.join('sprites/island', 'wall.png')).convert_alpha()

    def generate_level(self):

        start = StartKit.Start_kit()
        end = EndKit.End_kit()

        self.merge_tile_maps(start, HallwayKit.Hallway_kit())
        self.merge_tile_maps(self, HallwayKit.Hallway_kit())
        self.merge_tile_maps(self, end)

        self.tile_map_to_rect_array()

        self.coin_img = pygame.transform.scale(self.coin_img,
                                               (self.coin_img.get_width() * 3, self.coin_img.get_height() * 3))
        self.spikes_img = pygame.transform.scale(self.spikes_img,
                                                 (self.spikes_img.get_width() * 2, self.spikes_img.get_height() * 2))

    # fill tile_maps with neutral rows until both connector rows have same index
    def merge_tile_maps(self, start_kit, extension_kit):

        self.tile_map = [a + b for a, b in zip(start_kit.tile_map, extension_kit.tile_map)]
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
                    self.enemy_array.append(
                        pygame.Rect(self.pointer_x, self.pointer_y + self.tile_size_small, self.tile_size_small, self.tile_size_small))
                if column == 3:
                    # add wall left
                    self.tile_array.append(
                        [pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size_small, self.tile_size), 3])
                if column == 4:
                    # add wall right
                    self.tile_array.append(
                        [pygame.Rect(self.pointer_x + self.tile_size - self.tile_size_small, self.pointer_y, self.tile_size_small, self.tile_size), 4])
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
                    self.goal_rect = pygame.Rect(self.pointer_x + self.tile_size - self.tile_size_small, self.pointer_y, self.tile_size_small, self.tile_size)
                if column == 9:
                    # add block
                    self.tile_array.append(
                        [pygame.Rect(self.pointer_x, self.pointer_y, self.tile_size, self.tile_size), 9])
                self.pointer_x += self.tile_size
            self.pointer_x = 0
            self.pointer_y += self.tile_size

    def draw(self, hero, screen):
        # draw background
        screen.blit(self.bg_img, (0, 0))

        for tile in self.tile_array:
            tmp_rect = tile[0]
            tile_type = tile[1]
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            if tile_type == 1:
                screen.blit(self.floor_img, (tmp_rect.x, tmp_rect.y))
            elif tile_type == 3:
                screen.blit(self.wall_img, (tmp_rect.x, tmp_rect.y))
            elif tile_type == 7:
                screen.blit(self.platform_img, (tmp_rect.x, tmp_rect.y))
            elif tile_type == 9:
                screen.blit(self.block_img, (tmp_rect.x, tmp_rect.y))
            else:
                pygame.draw.rect(screen, (255, 255, 255), tmp_rect)

        for tmp_rect in self.enemy_array:
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            screen.blit(self.spikes_img, (tmp_rect.x, tmp_rect.y))

        for tmp_rect in self.coin_array:
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            screen.blit(self.coin_img, (tmp_rect.x, tmp_rect.y))

        # draw goal
        self.goal_rect.x = self.goal_rect.x - hero.indeed_moved_x
        pygame.draw.rect(screen, (0, 255, 0), self.goal_rect)

        # draw hero
        if hero.line_of_sight == 1:
            screen.blit(hero.img, (hero.x, hero.y))
        else:
            img = pygame.transform.flip(hero.img, True, False)  # flip hero img
            img.set_colorkey((0, 0, 0))
            screen.blit(img, (hero.x, hero.y))

        # draw health
        draw_text(screen, f"Life: {hero.health}", 10, 10)

        # draw highscore
        draw_text(screen, f"Highscore: {hero.highscore}", 300, 10)

        # update display
        pygame.display.update()
