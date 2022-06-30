import sys
import pygame

from controllers.CollisionController import handle_collision_with_environment, handle_collision_with_traps_and_enemies, \
    handle_collision_with_coin, reached_level_goal
from controllers.LevelController import generate_random_level
from controllers.MovementController import handle_movement, handle_jump
from models.Background import Background
from models.CharacterState import CharacterState
from models.Level import Level
from views import gameover

# environment
gravity = 5


def start(clock, screen, hero):

    level = Level()
    bg = Background()

    # generate level using the tile map
    generate_random_level(level)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # handle hero movement
        handle_movement(hero)

        # handle gravity
        hero.next_y = hero.y + gravity

        # handle jump
        handle_jump(hero)

        # handle collision with environment
        handle_collision_with_environment(hero, level.tile_array)

        # handle collision with enemy
        handle_collision_with_traps_and_enemies(hero, level.trap_array, level.crabby_array)

        # handle collision with coin
        handle_collision_with_coin(hero, level)

        # update hero img
        hero.img_clock = hero.img_clock + 1
        if (hero.img_clock / 10).is_integer():
            hero.img_index = (hero.img_index + 1) % len(hero.img_list)
        hero.img = hero.img_list[hero.img_index]

        for crabby in level.crabby_array:
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
            bg.draw(screen)
            level.draw(hero, screen)
        else:
            gameover.show(clock, screen, hero)
            break

        if reached_level_goal(hero, level):
            hero.x = 300
            hero.y = 300
            start(clock, screen, hero)
            break

        clock.tick(120)
