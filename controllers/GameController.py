import sys

import pygame

from controllers.AnimationController import animate_scene
from controllers.CollisionController import handle_collision
from controllers.LevelController import generate_random_level
from controllers.MovementController import handle_movement
from controllers.SoundController import play_main_theme, goal_sound
from models.Background import Background
from models.CharacterState import CharacterState
from models.Level import Level
from views import gameover, menu


def start(clock, screen, hero):
    level = Level()
    bg = Background()
    bg.init_palmtree_array()

    play_main_theme()

    freeze_time = 0

    # generate level using the tile map
    generate_random_level(level)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                menu.show(clock, screen, bg)
                break

        if freeze_time == 0:
            # handle hero movement
            handle_movement(hero)

            # handle collision
            handle_collision(hero, level)

            # animate scene
            animate_scene(hero, level.crabby_array, level.seashell_array)

        # draw
        if hero.is_alive():
            bg.draw(screen, hero)
            level.draw(hero, screen, (freeze_time > 0))
        else:
            gameover.show(clock, screen, hero, bg)
            break

        if freeze_time == 0 and hero.x > level.goal_rect.x + 20:
            freeze_time = 100
            hero.indeed_moved_x = 0
            hero.change_state(CharacterState.IDLE)
            goal_sound()

        if freeze_time > 0:
            freeze_time = freeze_time - 1

        if freeze_time == 1:
            start_next_level(screen, clock, hero)
            break

        clock.tick(120)


def start_next_level(screen, clock, hero):
    hero.x, hero.next_x = 300, 300
    hero.y, hero.next_y = 300, 300
    start(clock, screen, hero)
