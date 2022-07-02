import random

import pygame

from controllers.HelperController import draw_text
from kitbashing.KitCollection import KitCollection
from models.Crabby import Crabby
from models.Seashell import Seashell
from models.Trap import Trap


def draw(level, hero, screen, freeze, level_number):
    for tile in level.tile_array:
        tmp_rect = tile[0]
        tile_type = tile[1]
        tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
        if tile_type == 1:
            screen.blit(level.floor_img, (tmp_rect.x, tmp_rect.y))
        elif tile_type == 3:
            screen.blit(level.wall_img, (tmp_rect.x, tmp_rect.y))
        elif tile_type == 7:
            screen.blit(level.platform_img, (tmp_rect.x, tmp_rect.y))
        elif tile_type == 9:
            screen.blit(level.block_img, (tmp_rect.x, tmp_rect.y))
        elif tile_type == 99:
            screen.blit(level.ship_img, (tmp_rect.x, tmp_rect.y))

    for trap in level.trap_array:
        trap.x = trap.x - hero.indeed_moved_x
        screen.blit(trap.img, (trap.x, trap.y))

    for crabby in level.crabby_array:
        crabby.x = crabby.x - hero.indeed_moved_x
        screen.blit(crabby.img, (crabby.x, crabby.y))

    for seashell in level.seashell_array:
        if seashell.bullet:
            screen.blit(seashell.pearl_img, (seashell.bullet.x, seashell.bullet.y))
        seashell.x = seashell.x - hero.indeed_moved_x
        screen.blit(seashell.img, (seashell.x, seashell.y))

    for tmp_rect in level.coin_array:
        tmp_rect.x = tmp_rect.x - hero.indeed_moved_x
        screen.blit(level.coin_img, (tmp_rect.x, tmp_rect.y))

    # draw goal
    level.goal_rect.x = level.goal_rect.x - hero.indeed_moved_x
    screen.blit(level.goal_img, (level.goal_rect.x, level.goal_rect.y))

    # draw hero
    if hero.line_of_sight == 1:
        screen.blit(hero.img, (hero.x, hero.y))
    else:
        img = pygame.transform.flip(hero.img, True, False)  # flip hero img
        img.set_colorkey((0, 0, 0))
        screen.blit(img, (hero.x, hero.y))

    # draw health
    screen.blit(level.lifebar_img, (20, 10))
    pygame.draw.rect(screen, (255, 0, 255), (73, 52, hero.health, 2 * 3))

    # draw highscore
    draw_text(screen, f"HIGHSCORE: {hero.highscore}", 1400, 50, 20)

    # draw level_number
    draw_text(screen, f"Level: {level_number}", 1000, 50, 20)

    if freeze:
        draw_text(screen, "level accomplished!", 500, 200, 50)

    # update display
    pygame.display.update()


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
        all_class_tiles.pop(random_num)
        all_class_tiles_length = all_class_tiles_length - 1

    level.merge_tile_maps(kit_collection.end_kit_tile_map)

    tile_map_to_rect_array(level)


def tile_map_to_rect_array(level):
    level.tile_array.append(
        [pygame.Rect(-710, 50, 735, 972), 99])
    for row in level.tile_map:
        for column in row:
            if column == 1:
                # add floor
                level.tile_array.append(
                    [pygame.Rect(level.pointer_x, level.pointer_y, level.tile_size, level.tile_size), 1])
            if column == 2:
                # add trap
                level.trap_array.append(
                    Trap(level.pointer_x, level.pointer_y + level.tile_size_small))
            if column == 3:
                # add wall
                level.tile_array.append(
                    [pygame.Rect(level.pointer_x, level.pointer_y, level.tile_size_small, level.tile_size), 3])
            if column == 4:
                # add crabby
                level.crabby_array.append(
                    Crabby(level.pointer_x - level.tile_size_small, level.pointer_y + level.tile_size_small + 7))
            if column == 5:
                # add seashell
                level.seashell_array.append(
                    Seashell(level.pointer_x, level.pointer_y + 23))
            if column == 6:
                # add coin
                level.coin_array.append(
                    pygame.Rect(level.pointer_x + level.tile_size_small - 8, level.pointer_y + level.tile_size_small,
                                level.tile_size_small, level.tile_size_small))
            if column == 7:
                # add platform
                level.tile_array.append(
                    [pygame.Rect(level.pointer_x, level.pointer_y, level.tile_size, level.tile_size_small), 7])
            if column == 8:
                # add goal
                level.goal_rect = pygame.Rect(level.pointer_x - level.tile_size, level.pointer_y,
                                              level.tile_size_small, level.tile_size)
            if column == 9:
                # add block
                level.tile_array.append(
                    [pygame.Rect(level.pointer_x, level.pointer_y, level.tile_size, level.tile_size), 9])
            level.pointer_x += level.tile_size
        level.pointer_x = 0
        level.pointer_y += level.tile_size
