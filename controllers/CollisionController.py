import pygame

from controllers.MovementController import set_indeed_moved_x
from models.HeroState import HeroState


def handle_collision_with_enemy(hero, enemy_array):
    if hero.is_damaged():
        if hero.dash_state == 1:
            hero.change_state(HeroState.IDLE)
        hero.damage_state = hero.damage_state - 1
        hero.change_state(HeroState.DAMAGED)
    else:
        for rect in enemy_array:
            if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(
                    rect) and not hero.is_dashing() and not hero.is_damaged():
                hero.health -= 10  # todo set value enemy
                hero.damage_state = 60
                hero.change_state(HeroState.DAMAGED)


def handle_collision_with_coin(hero, generated_level):
    for rect in generated_level.coin_array:
        if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(rect):
            hero.highscore += 1
            generated_level.coin_array.remove(rect)


def handle_collision_with_environment(hero, rect_array):
    next_hero_rect = pygame.Rect(hero.x if hero.next_x == 0 else hero.next_x,
                                 hero.y if hero.next_y == 0 else hero.next_y, hero.width, hero.height)

    collision_x = False
    collision_y = False

    for rect in rect_array:

        if next_hero_rect.colliderect(rect):

            hero.grounded = False
            next_hero_rect_only_y = pygame.Rect(hero.x, hero.next_y, hero.width, hero.height)

            if hero.next_y != 0 and next_hero_rect_only_y.colliderect(rect):
                # collision bottom
                if hero.y < hero.next_y:
                    if rect.top < next_hero_rect.bottom:
                        hero.grounded = True
                        hero.y = rect.top - hero.height
                        collision_y = True
                # collision top
                if hero.y > hero.next_y:
                    if rect.bottom > next_hero_rect.top:
                        hero.y = rect.bottom
                        collision_y = True
                        if hero.is_jumping():
                            hero.jump_state = hero.init_jumpstate

            next_hero_rect_only_x = pygame.Rect(hero.next_x, hero.y, hero.width, hero.height)
            if hero.next_x != 0 and next_hero_rect_only_x.colliderect(rect):
                # collision left
                if hero.x > hero.next_x:
                    if rect.right > next_hero_rect.left:
                        set_indeed_moved_x(hero, rect.right)
                        hero.x = rect.right
                        collision_x = True
                # collision right
                if hero.x < hero.next_x:
                    if rect.left < next_hero_rect.right:
                        set_indeed_moved_x(hero, rect.left - hero.width)
                        hero.x = rect.left - hero.width
                        collision_x = True

    if not collision_x and hero.next_x != 0:
        set_indeed_moved_x(hero, hero.next_x)
        hero.x = hero.next_x
    if not collision_y:
        hero.y = hero.next_y
