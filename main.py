import pygame as pg

import game
import menu
import view


def is_active(button_pos, button_size, mouse_pos):
    if button_pos[0] - button_size[0]/2 <= mouse_pos[0] <= button_pos[0] + button_size[0]/2\
            and button_pos[1] - button_size[1]/2 <= mouse_pos[1] <= button_pos[1] + button_size[1]/2:
        return True
    else:
        return False


start_menu = menu.Start_menu()
menu_view = view.Menu_view()

# Start menu loop
start = False
mouse_pressed = False
while not start:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = True

    start_menu.change_status(
        is_active(start_menu.button_pos, start_menu.button_size, pg.mouse.get_pos()))

    if start_menu.button_status and mouse_pressed:
        start = True

    menu_view.update(start_menu.button_pos,
                     start_menu.button_size, start_menu.button_status)
    mouse_pressed = False

# Game
game.sapper_game()
