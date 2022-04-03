import pygame, player, level_1
import sys

# todo known bugs: reject button spamming

pygame.init()

screen_width = 1500
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])

clock = pygame.time.Clock()
pygame.display.set_caption("Test")

hero = player.Player()

gravity = 5

# draw level_1_array
level_1 = level_1.Level_1()

for row in level_1.tile_map:
    for column in row:
        if column == 1:
            tmp_rect = pygame.Rect(level_1.pointer_x, level_1.pointer_y, level_1.block_width, level_1.block_height)
            level_1.rect_array.append(tmp_rect)
        level_1.pointer_x += level_1.tile_size
    level_1.pointer_x = 0
    level_1.pointer_y += level_1.tile_size

def draw ():
    # draw background
    screen.fill((0, 0, 0))

    for tmp_rect in level_1.rect_array:
        pygame.draw.rect(screen, (255, 255, 255), tmp_rect)

    # draw hero
    pygame.draw.rect(screen, (255, 255, 0), (hero.x, hero.y, hero.width, hero.height))

    # update display
    pygame.display.update()

# game loop
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP] and hero.jump_state == -16:
        hero.jump_state = 15
    if keys_pressed[pygame.K_DOWN]:
        hero.next_y = hero.y + hero.velocity
    if keys_pressed[pygame.K_RIGHT]:
        hero.line_of_sight = 1
        hero.next_x = hero.x + hero.velocity
    if keys_pressed[pygame.K_LEFT]:
        hero.line_of_sight = -1
        hero.next_x = hero.x - hero.velocity
    if keys_pressed[pygame.K_d] and hero.dash_state == -16:
        hero.dash_state = 0

    hero.next_y = hero.y + gravity

    # handle jump
    if hero.jump_state >= -15:
        n = 1
        if hero.jump_state < 0:
            n = -1
        hero.next_y -= (hero.jump_state**2)*0.17*n # quadratische Formel zur Sprungberechnung
        hero.jump_state -= 1

    # handle dash
    if hero.dash_state >= -15:
        if hero.line_of_sight == 1:
            hero.next_x = hero.x + hero.dash_speed
        if hero.line_of_sight == -1:
            hero.next_x = hero.x - hero.dash_speed
        hero.dash_state -= 1

    # collisionDetection
    next_hero_rect = pygame.Rect(hero.x, hero.y, hero.width, hero.height)
    if hero.next_x != 0 :
        next_hero_rect.x = hero.next_x
    if hero.next_y != 0:
        next_hero_rect.y = hero.next_y

    next_hero_rect_x = pygame.Rect(hero.next_x, hero.y, hero.width, hero.height)
    next_hero_rect_y = pygame.Rect(hero.x, hero.next_y, hero.width, hero.height)

    collision_x = False
    collision_y = False

    for rect in level_1.rect_array:

        if next_hero_rect.colliderect(rect):

            if hero.next_y != 0 and next_hero_rect_y.colliderect(rect):
                # collision bottom
                if hero.y < hero.next_y:
                    if rect.top < next_hero_rect.bottom:
                        hero.grounded = True
                        hero.y = rect.top - hero.height
                        print("collision bottom")
                        collision_y = True
                # collision top
                if hero.y > hero.next_y:
                    if rect.bottom > next_hero_rect.top:
                        hero.y = rect.bottom
                        print("collision top")
                        collision_y = True
            if hero.next_x != 0 and next_hero_rect_x.colliderect(rect):
                # collision left
                if hero.x > hero.next_x:
                    if rect.right > next_hero_rect.left:
                        hero.x = rect.right
                        print("collision left")
                        collision_x = True
                # collision right
                if hero.x < hero.next_x:
                    if rect.left < next_hero_rect.right:
                        hero.x = rect.left - hero.width
                        print("collision right")
                        collision_x = True

    if collision_x == False:
        hero.x = hero.next_x
    if collision_y == False:
        hero.y = hero.next_y

    draw()
    clock.tick(60)