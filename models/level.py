import os

import pygame

from controllers import helper
from kitbashing import start_kit, end_kit, hallway_kit


class Level:

    def __init__(self):
        self.pointer_x = 0
        self.pointer_y = 100

        self.tile_size = 100

        self.block_width = 100
        self.block_height = 20

        self.tile_map = []
        self.connector_index_r = -1
        self.neutral_list = []

        self.rect_array = []

        self.enemy_array = []

        self.coin_array = []

        self.goal_rect = []

    def generate_level(self):

        start = start_kit.Start_kit()
        end = end_kit.End_kit()

        self.merge_tile_maps(start, hallway_kit.Hallway_kit())
        self.merge_tile_maps(self, hallway_kit.Hallway_kit())
        self.merge_tile_maps(self, end)

        self.tile_map_to_rect_array()

    # fill tile_maps with neutral rows until both connector rows have same index
    def merge_tile_maps(self, start_kit, extension_kit):

        start_map_above_connector = start_kit.tile_map[0:start_kit.connector_index_r]
        hallway_map_above_connector = extension_kit.tile_map[0:extension_kit.connector_index_l]

        start_map_under_connector = start_kit.tile_map[start_kit.connector_index_r + 1:]
        hallway_map_under_connector = extension_kit.tile_map[extension_kit.connector_index_l + 1:]

        # evaluate which tile_map has more rows above the connector row and fill it up with neutral rows
        len_diff_above = len(start_map_above_connector) - len(hallway_map_above_connector)  # positiv, dann start größer
        # start > hallway
        if len_diff_above > 0:
            for _ in range(len_diff_above):
                extension_kit.tile_map.insert(0, extension_kit.neutral_list)
        # hallway > start
        elif len_diff_above < 0:
            for _ in range(len_diff_above * -1):
                start_kit.tile_map.insert(0, start_kit.neutral_list)

        # evaluate which tile_map has more rows under the connector row and fill it up with neutral rows
        len_diff_under = len(start_map_under_connector) - len(hallway_map_under_connector)  # positiv, dann start größer
        # start > hallway
        if len_diff_under > 0:
            for _ in range(len_diff_under):
                extension_kit.tile_map.append(extension_kit.neutral_list)
        # hallway > start
        elif len_diff_under < 0:
            for _ in range(len_diff_under * -1):
                start_kit.tile_map.append(start_kit.neutral_list)

        self.tile_map = [a + b for a, b in zip(start_kit.tile_map, extension_kit.tile_map)]
        self.neutral_list = [0] * len(self.tile_map[0])

        # search for new connector row right after modifyin tile_map
        index = 0
        for row in self.tile_map:
            if row[-1] == 9:
                self.connector_index_r = index
                break
            index = index + 1


    def tile_map_to_rect_array(self):
        for row in self.tile_map:
            for column in row:
                if column == 1:
                    # add platform
                    self.rect_array.append(
                        pygame.Rect(self.pointer_x, self.pointer_y, self.block_width, self.block_height))
                if column == 2:
                    # add block
                    self.rect_array.append(
                        pygame.Rect(self.pointer_x, self.pointer_y, self.block_width, self.block_height))
                    # add enemy
                    self.enemy_array.append(
                        pygame.Rect(self.pointer_x, self.pointer_y - self.block_height, 20, self.block_height))
                if column == 3:
                    # add wall left
                    self.rect_array.append(pygame.Rect(self.pointer_x, self.pointer_y, 20, 100))
                if column == 4:
                    # add wall right
                    self.rect_array.append(pygame.Rect(self.pointer_x + self.tile_size - 20, self.pointer_y, 20, 100))
                if column == 5:
                    # add wall ceiling
                    self.rect_array.append(
                        pygame.Rect(self.pointer_x, self.pointer_y + self.tile_size - 20, self.block_width,
                                    self.block_height))
                if column == 6:
                    # add coin
                    self.coin_array.append(
                        pygame.Rect(self.pointer_x, self.pointer_y, 20, self.block_height))
                if column == 8:
                    # add goal
                    self.goal_rect = pygame.Rect(self.pointer_x + 100 - 20, self.pointer_y, 20, 100)
                self.pointer_x += self.tile_size
            self.pointer_x = 0
            self.pointer_y += self.tile_size

    def draw(self, hero, screen):
        # draw background
        screen.fill((0, 0, 0))

        for tmp_rect in self.rect_array:
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            pygame.draw.rect(screen, (255, 255, 255), tmp_rect)

        for tmp_rect in self.enemy_array:
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            pygame.draw.rect(screen, (255, 0, 0), tmp_rect)

        for tmp_rect in self.coin_array:
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            pygame.draw.rect(screen, (255, 255, 0), tmp_rect)

        # draw goal
        self.goal_rect.x = self.goal_rect.x - hero.indeed_moved_x
        pygame.draw.rect(screen, (0, 255, 0), self.goal_rect)

        # draw hero
        if hero.is_damaged():
            pygame.draw.rect(screen, (0, 255, 0), (hero.x, hero.y, hero.width, hero.height))
        else:
            #pygame.draw.rect(screen, (255, 150, 150), (hero.x, hero.y, hero.width, hero.height))

            img = pygame.image.load(os.path.join('sprites/hero', 'hero_idle.png'))
            btn_play = img.get_rect()
            btn_play.x = hero.x
            btn_play.y = hero.y
            screen.blit(img, btn_play)

        # draw health
        helper.draw_text(screen, f"Life: {hero.health}", 10, 10)

        # draw highscore
        helper.draw_text(screen, f"Highscore: {hero.highscore}", 300, 10)

        # update display
        pygame.display.update()
