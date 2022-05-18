import pygame


class Player:
    x = 300
    y = 300
    velocity = 5
    width = 30
    height = 50

    jump_state = -16

    dash_state = -16
    dash_speed = 20

    line_of_sight = 1

    grounded = False
    next_y = 0
    next_x = 0
    collision_x = False
    collision_y = False

    health = 100

    def handle_movement (self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] and self.jump_state == -16:
            self.jump_state = 15
        if keys_pressed[pygame.K_DOWN]:
            self.next_y = self.y + self.velocity
        if keys_pressed[pygame.K_RIGHT]:
            self.line_of_sight = 1
            self.next_x = self.x + self.velocity
        if keys_pressed[pygame.K_LEFT]:
            self.line_of_sight = -1
            self.next_x = self.x - self.velocity
        if keys_pressed[pygame.K_d] and self.dash_state == -16:
            self.dash_state = 0

    def handle_jump (self):
        if self.jump_state >= -15:
            n = 1
            if self.jump_state < 0:
                n = -1
            self.next_y -= (self.jump_state ** 2) * 0.17 * n  # quadratische Formel zur Sprungberechnung
            self.jump_state -= 1

    def handle_dash (self):
        if self.dash_state >= -15:
            if self.line_of_sight == 1:
                self.next_x = self.x + self.dash_speed
            if self.line_of_sight == -1:
                self.next_x = self.x - self.dash_speed
            self.dash_state -= 1

    def handle_collision_with_enemy (hero, enemy_array):
        for rect in enemy_array:
            if pygame.Rect(hero.x, hero.y, hero.width, hero.height).colliderect(rect):
                print("hit")
                hero.health -= 10  # todo set value enemy

    def handle_collision_with_environment (hero, rect_array):
        next_hero_rect = pygame.Rect(hero.x if hero.next_x == 0 else hero.next_x,
                                     hero.y if hero.next_y == 0 else hero.next_y, hero.width, hero.height)

        collision_x = False
        collision_y = False

        for rect in rect_array:

            if next_hero_rect.colliderect(rect):

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
                            print("collision top")
                            collision_y = True
                            if hero.jump_state != -16:
                                hero.jump_state = -16

                next_hero_rect_only_x = pygame.Rect(hero.next_x, hero.y, hero.width, hero.height)
                if hero.next_x != 0 and next_hero_rect_only_x.colliderect(rect):
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

