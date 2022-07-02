import pygame

from models.CharacterState import CharacterState


def animate_scene(hero, crabby_array, seashell_array):
    # update hero
    animate_hero(hero)

    # update crabby
    for crabby in crabby_array:
        animate_crabby(crabby)

    # update seashell
    for seashell in seashell_array:
        animate_seashell(seashell)


def animate_hero(hero):
    hero.img_clock += 1
    if (hero.img_clock / 10).is_integer():
        hero.img_index = (hero.img_index + 1) % len(hero.img_list)
    hero.img = hero.img_list[hero.img_index]


def animate_crabby(crabby):
    if crabby.state == CharacterState.IDLE:
        crabby.idle_clock += 1
        if crabby.idle_clock == crabby.idle_time:
            crabby.change_state(CharacterState.ATTACK)
            crabby.idle_clock = 0

    if crabby.state == CharacterState.RUN:
        crabby.movement_clock += 1
        if crabby.line_of_sight == 1:
            crabby.x += crabby.velocity
        else:
            crabby.x -= crabby.velocity

        if crabby.movement_clock == crabby.movement_time:
            crabby.line_of_sight = -1
        if crabby.movement_clock == crabby.movement_time * 2:
            crabby.movement_clock = 0
            crabby.line_of_sight = 1
            crabby.change_state(CharacterState.IDLE)
    if crabby.state == CharacterState.ATTACK:
        crabby.attack_clock += 1
        if crabby.attack_clock == crabby.attack_time:
            crabby.attack_clock = 0
            crabby.change_state(CharacterState.RUN)

    crabby.img_clock += 1

    if (crabby.img_clock / 15).is_integer():
        crabby.img_index = (crabby.img_index + 1) % len(crabby.img_list)
    crabby.img = crabby.img_list[crabby.img_index]


def animate_seashell(seashell):
    if seashell.state == CharacterState.IDLE:
        seashell.idle_clock += 1
        if seashell.idle_clock == seashell.idle_time:
            seashell.change_state(CharacterState.ATTACK)
            seashell.idle_clock = 0
    if seashell.state == CharacterState.ATTACK:
        if seashell.attack_clock == 0:
            seashell.bullet = pygame.Rect(seashell.x + seashell.width, seashell.y + seashell.height, 32, 32)
        seashell.attack_clock += 1
        if seashell.bullet:
            seashell.bullet.x = seashell.bullet.x - 10
        if seashell.attack_clock == seashell.attack_time:
            seashell.bullet = None
            seashell.attack_clock = 0
            seashell.change_state(CharacterState.IDLE)

    seashell.img_clock += +1

    if (seashell.img_clock / 15).is_integer():
        seashell.img_index = (seashell.img_index + 1) % len(seashell.img_list)
    seashell.img = seashell.img_list[seashell.img_index]
