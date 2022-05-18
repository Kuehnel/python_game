import pygame

class Level:
    pointer_x = 0
    pointer_y = 100
    tile_size = 100

    block_width = 100
    block_height = 50

    rect_array = []

    enemy_array = []

    def generate_level (self, tile_map):
        for row in tile_map:
            for column in row:
                if column == 1:
                    tmp_rect = pygame.Rect(self.pointer_x, self.pointer_y, self.block_width,
                                           self.block_height)
                    self.rect_array.append(tmp_rect)
                if column == 2:
                    tmp_rect = pygame.Rect(self.pointer_x, self.pointer_y, self.block_width,
                                           self.block_height)
                    self.enemy_array.append(tmp_rect)
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
        pygame.draw.rect(screen, (255, 255, 0), (player.x, player.y, player.width, player.height))

        # draw health
        myfont = pygame.font.SysFont("Arial", 30)
        label = myfont.render(f"{player.health}", True, (0, 255, 255))
        screen.blit(label, (10, 10))

        # update display
        pygame.display.update()
