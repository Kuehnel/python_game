import os
import sys
import pygame

from models.hero import Hero
from views import gameover
from models import level


def start(clock, screen):
    # environment
    gravity = 5

    # init level
    generated_level = level.Level()

    # init hero
    hero = Hero()

    # generate level using the tile map
    generated_level.generate_level()

    # game loop
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    go = False

        # handle hero movement
        hero.handle_movement()

        # handle gravity
        hero.next_y = hero.y + gravity

        # handle jump
        hero.handle_jump()

        # handle dash
        hero.handle_dash()

        # handle collision with environment
        hero.handle_collision_with_environment(generated_level.rect_array)

        # handle collision with enemy
        hero.handle_collision_with_enemy(generated_level.enemy_array)

        # handle collision with coin
        hero.handle_collision_with_coin(generated_level)

        if hero.is_alive():
            generated_level.draw(hero, screen)
        else:
            gameover.show(clock, screen, hero)
            break

        clock.tick(60)
