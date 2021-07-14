import pygame as pg

import game
import menu
import view
import variables

WIN_SIZE = variables.WIN_SIZE
GRID_SIZE = variables.GRID_SIZE
MINES_AMOUNT = variables.MINES_AMOUNT
SIDE_SIZE = variables.SIDE_SIZE


def is_start_button_active(button_pos, button_size, mouse_pos):
    if button_pos[0] - button_size[0]/2 <= mouse_pos[0] <= button_pos[0] + button_size[0]/2\
            and button_pos[1] - button_size[1]/2 <= mouse_pos[1] <= button_pos[1] + button_size[1]/2:
        return 1
    else:
        return 0


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

    start_menu.change_status(start_menu.start_button,
                             is_start_button_active(start_menu.button_pos, start_menu.button_size, pg.mouse.get_pos()))

    if bool(start_menu.start_button.status) and mouse_pressed:
        start = True

    menu_view.update(start_menu)
    mouse_pressed = False

# Game
field = game.Mine_field(GRID_SIZE, MINES_AMOUNT, WIN_SIZE[1])
game_end = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] < WIN_SIZE[1]:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x = int(mouse_pos[0]//SIDE_SIZE)
                y = int(mouse_pos[1]//SIDE_SIZE)

                field.update(x, y, event.button)
                field.defeat_check(mouse_pos, field)

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                x = int(mouse_pos[0]//SIDE_SIZE)
                y = int(mouse_pos[1]//SIDE_SIZE)

                field.update(x, y, event.button)

    field.victory_check(field)

    if game_end:
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

    field.draw(WIN_SIZE[1])
    pg.display.update()
