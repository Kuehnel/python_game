import os
import sys
import pygame

from controllers.CollisionController import handle_collision_with_environment, handle_collision_with_traps_and_enemies, \
    handle_collision_with_coin
from controllers.MovementController import handle_movement, handle_jump, handle_dash
from models.CharacterState import CharacterState
from models.Spritesheet import Spritesheet
from models.Hero import Hero
from views import gameover
from models import Level


def start(clock, screen):
    # environment
    gravity = 5

    # init level
    generated_level = Level.Level()

    # init hero
    hero = Hero()

    # TODO load images
    hero_idle_img = pygame.image.load(os.path.join('sprites/hero', 'hero_idle.png')).convert_alpha()
    hero_idle_sheet = Spritesheet(hero_idle_img)
    hero.idle_img_list = [hero_idle_sheet.get_image(0, 32, 32, 2), hero_idle_sheet.get_image(1, 32, 32, 2),
                          hero_idle_sheet.get_image(2, 32, 32, 2), hero_idle_sheet.get_image(3, 32, 32, 2)]

    hero_run_img = pygame.image.load(os.path.join('sprites/hero', 'hero_run.png')).convert_alpha()
    hero_run_sheet = Spritesheet(hero_run_img)
    hero.run_img_list = [hero_run_sheet.get_image(0, 32, 32, 2), hero_run_sheet.get_image(1, 32, 32, 2),
                         hero_run_sheet.get_image(2, 32, 32, 2), hero_run_sheet.get_image(3, 32, 32, 2),
                         hero_run_sheet.get_image(4, 32, 32, 2), hero_run_sheet.get_image(5, 32, 32, 2)]

    hero_jump_img = pygame.image.load(os.path.join('sprites/hero', 'hero_jump.png')).convert_alpha()
    hero_jump_sheet = Spritesheet(hero_jump_img)
    hero.jump_img_list = [hero_jump_sheet.get_image(0, 32, 32, 2), hero_jump_sheet.get_image(1, 32, 32, 2),
                          hero_jump_sheet.get_image(2, 32, 32, 2), hero_jump_sheet.get_image(3, 32, 32, 2),
                          hero_jump_sheet.get_image(4, 32, 32, 2), hero_jump_sheet.get_image(5, 32, 32, 2),
                          hero_jump_sheet.get_image(6, 32, 32, 2), hero_jump_sheet.get_image(9, 32, 32, 2)]

    hero_damaged_img = pygame.image.load(os.path.join('sprites/hero', 'hero_damaged.png')).convert_alpha()
    hero_damaged_sheet = Spritesheet(hero_damaged_img)
    hero.damaged_img_list = [hero_damaged_sheet.get_image(0, 32, 32, 2), hero_damaged_sheet.get_image(1, 32, 32, 2),
                             hero_damaged_sheet.get_image(2, 32, 32, 2), hero_damaged_sheet.get_image(3, 32, 32, 2)]

    hero.img_list = hero.idle_img_list

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
        handle_movement(hero)

        # handle gravity
        hero.next_y = hero.y + gravity

        # handle jump
        handle_jump(hero)

        # handle dash
        handle_dash(hero)

        # handle collision with environment
        handle_collision_with_environment(hero, generated_level.tile_array)

        # handle collision with enemy
        handle_collision_with_traps_and_enemies(hero, generated_level.trap_array, generated_level.crabby_array)

        # handle collision with coin
        handle_collision_with_coin(hero, generated_level)

        # update hero img
        hero.img_clock = hero.img_clock + 1
        if (hero.img_clock / 10).is_integer():
            hero.img_index = (hero.img_index + 1) % len(hero.img_list)
        hero.img = hero.img_list[hero.img_index]

        for crabby in generated_level.crabby_array:
            if (crabby.attack_clock / 1000).is_integer():
                crabby.change_state(CharacterState.ATTACK)
                crabby.attack_clock = 0

            if crabby.attack_clock == 150 and crabby.state == CharacterState.ATTACK:
                crabby.change_state(CharacterState.IDLE)

            crabby.attack_clock = crabby.attack_clock + 1

            crabby.img_clock = crabby.img_clock + 1

            if (crabby.img_clock / 15).is_integer():
                crabby.img_index = (crabby.img_index + 1) % len(crabby.img_list)
            crabby.img = crabby.img_list[crabby.img_index]

        if hero.is_alive():
            generated_level.draw(hero, screen)
        else:
            gameover.show(clock, screen, hero)
            break

        clock.tick(120)
