import pygame, player, level_1
import sys

# todo known bugs: reject button spamming with timer, set timer after enemy hit

# pygame init + conf
pygame.init()
pygame.display.set_caption("Test")
screen_width = 1500
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

# environment
gravity = 5

# init level
level_1 = level_1.Level_1()

# init hero
hero = player.Player()

# generate level using the tile map
level_1.generate_level(level_1.tile_map)

# game loop
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # handle hero movement
    hero.handle_movement()

    # handle gravity
    hero.next_y = hero.y + gravity

    # handle jump
    hero.handle_jump()

    # handle dash
    hero.handle_dash()

    # handle collision with enemy
    hero.handle_collision_with_enemy(level_1.enemy_array)

    # handle collision with environment
    hero.handle_collision_with_environment(level_1.rect_array, level_1.enemy_array)

    level_1.draw(hero, screen)
    clock.tick(60)