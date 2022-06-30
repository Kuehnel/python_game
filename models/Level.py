import os

import pygame

from controllers.HelperController import draw_text, load_image_scaled


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
        self.coin_array = []

        self.goal_rect = None

        self.lifebar_img = load_image_scaled('sprites/hero/hud', 'lifebar.png', 3).convert_alpha()
        self.platform_img = pygame.image.load(os.path.join('sprites/island', 'platform.png')).convert_alpha()
        self.coin_img = pygame.image.load(os.path.join('sprites/collectables', 'coin.png')).convert_alpha()
        self.spikes_img = pygame.image.load(os.path.join('sprites/traps', 'spikes.png')).convert_alpha()
        self.floor_img = pygame.image.load(os.path.join('sprites/island', 'floor.png')).convert_alpha()
        self.floor_left_img = pygame.image.load(os.path.join('sprites/island', 'floor_left.png')).convert_alpha()
        self.block_img = pygame.image.load(os.path.join('sprites/island', 'block.png')).convert_alpha()
        self.wall_img = pygame.image.load(os.path.join('sprites/island', 'wall.png')).convert_alpha()
        self.goal_img = pygame.image.load(os.path.join('sprites/island', 'goal.png')).convert_alpha()

    def merge_tile_maps(self, next_tile_map):
        self.tile_map = [a + b for a, b in zip(self.tile_map, next_tile_map)]

    def draw(self, hero, screen):

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

        for trap in self.trap_array:
            tmp_rect = trap[0]
            enemy_type = trap[1]
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            if enemy_type == 2:
                screen.blit(self.spikes_img, (tmp_rect.x, tmp_rect.y))

        for crabby in self.crabby_array:
            crabby.x = crabby.x - hero.indeed_moved_x
            screen.blit(crabby.img, (crabby.x, crabby.y))

        for tmp_rect in self.coin_array:
            tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
            screen.blit(self.coin_img, (tmp_rect.x, tmp_rect.y))

        # draw goal
        self.goal_rect.x = self.goal_rect.x - hero.indeed_moved_x
        screen.blit(self.goal_img, (self.goal_rect.x, self.goal_rect.y))

        # draw hero
        if hero.line_of_sight == 1:
            screen.blit(hero.img, (hero.x, hero.y))
        else:
            img = pygame.transform.flip(hero.img, True, False)  # flip hero img
            img.set_colorkey((0, 0, 0))
            screen.blit(img, (hero.x, hero.y))

        # draw health
        screen.blit(self.lifebar_img, (20, 10))
        pygame.draw.rect(screen, (255, 0, 255), (73, 52, hero.health, 2 * 3))

        # draw highscore
        draw_text(screen, f"{hero.highscore}", 1600, 30)

        # update display
        pygame.display.update()
