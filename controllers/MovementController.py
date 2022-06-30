import pygame

from models.CharacterState import CharacterState


def set_indeed_moved_x(hero, new_x):
    hero.indeed_moved_x = new_x - hero.x


def handle_movement(hero):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE] and hero.allowed_to_jump():
        hero.jump_state = hero.init_jumpstate * -1
        hero.change_state(CharacterState.JUMP)
    if keys_pressed[pygame.K_DOWN]:
        hero.next_y = hero.y + hero.velocity
    if keys_pressed[pygame.K_RIGHT]:
        hero.line_of_sight = 1
        hero.next_x = hero.x + hero.velocity
        hero.change_state(CharacterState.RUN)
    if keys_pressed[pygame.K_LEFT]:
        hero.line_of_sight = -1
        hero.next_x = hero.x - hero.velocity
        hero.change_state(CharacterState.RUN)
    if keys_pressed[pygame.K_d] and hero.allowed_to_dash():
        hero.dash_state = 0

    if not keys_pressed[pygame.K_RIGHT] and not keys_pressed[pygame.K_LEFT] and not hero.is_jumping():
        hero.change_state(CharacterState.IDLE)


def handle_jump(hero):
    if hero.jump_state > hero.init_jumpstate:
        n = 1
        if hero.jump_state < 0:
            n = -1
        hero.next_y -= (hero.jump_state ** 2) * 0.17 * n
        hero.jump_state -= 1
        hero.grounded = False


def handle_dash(hero):
    if hero.dash_state > hero.init_dash_state and not hero.is_jumping():
        if hero.line_of_sight == 1:
            hero.next_x = hero.x + hero.dash_speed
        if hero.line_of_sight == -1:
            hero.next_x = hero.x - hero.dash_speed
        hero.dash_state -= 1
