import pygame

from controllers.MovementController import set_indeed_moved_x
from controllers.SoundController import damage_sound, collect_coin_sound
from models.CharacterState import CharacterState


def handle_collision(hero, level):
    # handle collision with environment
    handle_collision_with_environment(hero, level.tile_array)

    # handle collision with enemy
    handle_collision_with_traps_and_enemies(hero, level.trap_array, level.crabby_array, level.seashell_array)

    # handle collision with coin
    handle_collision_with_coin(hero, level)


def handle_collision_with_traps_and_enemies(hero, trap_array, crabby_array, seashell_array):
    if hero.is_damaged():
        hero.damage_state = hero.damage_state - 1
        hero.change_state(CharacterState.DAMAGED)
    else:
        collision_array = seashell_array + trap_array + crabby_array

        for enemy in collision_array:
            if hero.get_rect().colliderect(
                    enemy.get_rect()) and not hero.is_damaged():
                hero.health -= enemy.attack_strength
                hero.damage_state = 60
                hero.change_state(CharacterState.DAMAGED)

    if hero.damage_state == 60:
        damage_sound()


def handle_collision_with_coin(hero, generated_level):
    for rect in generated_level.coin_array:
        if hero.get_rect().colliderect(rect):
            collect_coin_sound()
            hero.highscore += generated_level.level_number
            generated_level.coin_array.remove(rect)


def handle_collision_with_environment(hero, tile_array):
    next_hero_rect = pygame.Rect(hero.next_x + hero.collision_tolerance, hero.next_y,
                                 hero.width - hero.collision_tolerance * 2, hero.height)

    for tile in tile_array:
        rect = tile[0]
        if next_hero_rect.colliderect(rect):

            hero.grounded = False

            next_hero_rect_only_y = pygame.Rect(hero.x + hero.collision_tolerance, hero.next_y,
                                                hero.width - hero.collision_tolerance * 2, hero.height)
            if next_hero_rect_only_y.colliderect(rect):
                # collision bottom
                if hero.y < hero.next_y:
                    hero.next_y = rect.top - hero.height
                    hero.grounded = True
                # collision top
                if hero.y > hero.next_y:
                    hero.next_y = rect.bottom
                    if hero.is_jumping():
                        hero.jump_state = hero.init_jumpstate

            next_hero_rect_only_x = pygame.Rect(hero.next_x + hero.collision_tolerance, hero.y,
                                                hero.width - hero.collision_tolerance * 2, hero.height)
            if next_hero_rect_only_x.colliderect(rect):

                # collision left
                if hero.x > hero.next_x:
                    hero.next_x = hero.x
                # collision right
                if hero.x < hero.next_x:
                    hero.next_x = hero.x

    set_indeed_moved_x(hero, hero.next_x)
    hero.x = hero.next_x
    hero.y = hero.next_y
