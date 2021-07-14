import pygame as pg

import game
import menu
import view
import variables

WIN = variables.WIN
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

del start_menu
del menu_view

# Game
sapper_game = game.Game(MINES_AMOUNT)
game_view = view.Field_view()
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

                sapper_game.update(x, y, event.button)

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                x = int(mouse_pos[0]//SIDE_SIZE)
                y = int(mouse_pos[1]//SIDE_SIZE)

                sapper_game.update(x, y, event.button)

    if sapper_game.result != 0:
        game_view.update(sapper_game.mine_field)
        WIN.blit(sapper_game.victory_label, ((WIN_SIZE[0] - sapper_game.victory_label.get_width())/2,
                                             (WIN_SIZE[1] - sapper_game.victory_label.get_height())/2))

        pg.display.update()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

    game_view.update(sapper_game.mine_field)
    pg.display.update()
