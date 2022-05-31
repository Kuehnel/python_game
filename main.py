import pygame, player, level
import sys

# todo known bugs: reject button spamming with timer, set timer after enemy hit

# pygame init + conf
pygame.init()
pygame.display.set_caption("Test")
screen_width = 1800
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

# environment
gravity = 5

# init level
level = level.Level()

# init hero
hero = player.Player()

# generate level using the tile map
level.generate_level()

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

    # handle collision with environment
    hero.handle_collision_with_environment(level.rect_array)

    # handle collision with enemy
    hero.handle_collision_with_enemy(level.enemy_array)

    level.draw(hero, screen)
    clock.tick(60)