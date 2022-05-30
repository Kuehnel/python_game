import pygame

class Level:
    pointer_x = 0
    pointer_y = 100
    tile_size = 100

    block_width = 100
    block_height = 20

    rect_array = []

    enemy_array = []

    def generate_level (self, tile_map, screen_width, screen_height):

        wall_width = 20

        # invisible wall left
        self.rect_array.append(pygame.Rect(0, 0, wall_width, screen_height))
        # invisible wall right
        self.rect_array.append(pygame.Rect(screen_width - wall_width, 0, wall_width, screen_height))
        # invisible wall top
        self.rect_array.append(pygame.Rect(0, 0, screen_width, wall_width))
        # invisible wall bottom
        self.rect_array.append(pygame.Rect(0, screen_height - wall_width, screen_width, wall_width))

        for row in tile_map:
            for column in row:
                if column == 1:
                    # add block
                    self.rect_array.append(pygame.Rect(self.pointer_x, self.pointer_y, self.block_width, self.block_height))
                if column == 2:
                    # add block
                    self.rect_array.append(pygame.Rect(self.pointer_x, self.pointer_y, self.block_width, self.block_height))
                    # add enemy
                    self.enemy_array.append(pygame.Rect(self.pointer_x, self.pointer_y - self.block_height, 20, self.block_height))
                self.pointer_x += self.tile_size
            self.pointer_x = 0
            self.pointer_y += self.tile_size

    def draw (self, player, screen):
        # draw background
        screen.fill((0, 0, 0))

        for tmp_rect in self.rect_array:
            pygame.draw.rect(screen, (255, 255, 255), tmp_rect)

        for tmp_rect in self.enemy_array:
            pygame.draw.rect(screen, (255, 255, 0), tmp_rect)

        # draw hero
        pygame.draw.rect(screen, (255, 150, 150), (player.x, player.y, player.width, player.height))

        # draw health
        myfont = pygame.font.SysFont("Arial", 30)
        label = myfont.render(f"{player.health}", True, (0, 255, 255))
        screen.blit(label, (10, 10))

        # update display
        pygame.display.update()
