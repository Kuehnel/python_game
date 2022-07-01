import sys
import pygame

from controllers.AnimationController import animate_scene
from controllers.CollisionController import reached_level_goal, handle_collision
from controllers.LevelController import generate_random_level
from controllers.MovementController import handle_movement
from models.Background import Background
from models.Level import Level
from views import gameover


def start(clock, screen, hero):
    level = Level()
    bg = Background()
    bg.init_palmtree_array()

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

        # handle collision
        handle_collision(hero, level)

        # animate scene
        animate_scene(hero, level.crabby_array, level.seashell_array)

        # draw
        if hero.is_alive():
            bg.draw(screen, hero)
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
