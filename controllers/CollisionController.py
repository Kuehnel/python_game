import pygame

from controllers.MovementController import set_indeed_moved_x
from models.CharacterState import CharacterState


def reached_level_goal(hero, level):
    if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(level.goal_rect):
        return True


def handle_collision_with_traps_and_enemies(hero, trap_array, crabby_array, seashell_array):
    if hero.is_damaged():
        hero.damage_state = hero.damage_state - 1
        hero.change_state(CharacterState.DAMAGED)
    else:
        for seashell in seashell_array:
            if seashell.bullet:
                rect = seashell.bullet
                if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(
                        rect) and not hero.is_damaged():
                    hero.health -= seashell.attack_strength
                    hero.damage_state = 60
                    hero.change_state(CharacterState.DAMAGED)

        for enemy in trap_array:
            rect = enemy[0]
            if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(
                    rect) and not hero.is_damaged():
                hero.health -= 220
                hero.damage_state = 60
                hero.change_state(CharacterState.DAMAGED)

        for crabby in crabby_array:
            crabby_rect = pygame.Rect(crabby.x, crabby.y, crabby.width, crabby.height)
            if crabby.state == CharacterState.ATTACK:
                crabby_rect = pygame.Rect(crabby.x + crabby.collision_tolerance, crabby.y,
                                          crabby.width - crabby.collision_tolerance, crabby.height)
            if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(
                    crabby_rect) and not hero.is_damaged():
                hero.health -= crabby.attack_strength
                hero.damage_state = 60
                hero.change_state(CharacterState.DAMAGED)


def handle_collision_with_coin(hero, generated_level):
    for rect in generated_level.coin_array:
        if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(rect):
            hero.highscore += 1
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
