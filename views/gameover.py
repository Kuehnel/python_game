import pygame

from controllers.DatabaseController import insert_highscore
from controllers.HelperController import draw_text, load_and_draw_image, handle_input
from controllers.SoundController import game_over_theme, navigation_sound
from views import menu


# show game over
def show(clock, screen, hero, bg):
    click = False
    image_dictionary = {}

    game_over_theme()

    insert_highscore(hero.highscore)

    while True:

        bg.draw(screen)

        load_and_draw_image(screen, 'sprites/menu/boards', 'bg_board.png', 548, 40, 5.5, image_dictionary)
        load_and_draw_image(screen, 'sprites/menu/boards', 'board.png', 580, 70, 5, image_dictionary)
        load_and_draw_image(screen, 'sprites/menu/banner', 'gameover_banner.png', 548, 0, 5.5, image_dictionary)

        draw_text(screen, f"Your Score:", 680, 240, 22)
        draw_text(screen, f"{hero.highscore}", 880, 300, 30)

        draw_text(screen, "\"May your anchor be tight,", 680, 400, 18)
        draw_text(screen, "your cork be loose,", 680, 440, 18)
        draw_text(screen, "your rum be spiced and", 680, 480, 18)
        draw_text(screen, "your compass be true.\"", 680, 520, 18)
        draw_text(screen, "- Danny Taddei -", 680, 560, 18)

        mx, my = pygame.mouse.get_pos()

        # load and render play button
        btn_menu = load_and_draw_image(screen, 'sprites/menu/buttons', 'menu.png', 756, 750, 3, image_dictionary)

        if btn_menu.collidepoint((mx, my)):
            if click:
                navigation_sound()
                menu.show(clock, screen, bg)

        click = handle_input()

        pygame.display.update()
        clock.tick(60)
