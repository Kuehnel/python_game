import pygame


def draw_text(screen, text, x, y):
    myfont = pygame.font.SysFont("Arial", 30)
    label = myfont.render(text, True, (0, 255, 255))
    screen.blit(label, (x, y))
