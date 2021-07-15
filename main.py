import pygame as pg

import game
import menu
import view


WIN_SIZE = (800, 800)
WIN = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption("Sapper")


def check_buttons(buttons, mouse_pos):
    for button in buttons:
        if button.pos[0] - button.size[0]/2 <= mouse_pos[0] <= button.pos[0] + button.size[0]/2\
                and button.pos[1] - button.size[1]/2 <= mouse_pos[1] <= button.pos[1] + button.size[1]/2:
            return button

    return -1


start_menu = menu.Start_menu(WIN_SIZE)
menu_view = view.Menu_view()

# Start menu
start = False
mouse_pressed = False
difficut = -1
while not start:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pressed = True

    buttons = start_menu.buttons()
    active_button = check_buttons(buttons, pg.mouse.get_pos())

    if active_button == -1:
        for button in buttons:
            start_menu.change_status(button, False)
    else:
        start_menu.change_status(active_button, True)

    if buttons[0].status and mouse_pressed and difficut != -1:
        start = True

    for i, button in enumerate(buttons[1:]):
        if button.status and mouse_pressed:
            start_menu.select(buttons[i + 1])
            difficut = i + 1

    menu_view.update(WIN, start_menu)
    mouse_pressed = False

del start_menu
del menu_view

# Game
sapper_game = game.Game(difficut, WIN_SIZE)
game_view = view.Field_view()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] < WIN_SIZE[1]:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x = int(mouse_pos[0]//sapper_game.side_size)
                y = int(mouse_pos[1]//sapper_game.side_size)

                sapper_game.update(x, y, event.button)

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                x = int(mouse_pos[0]//sapper_game.side_size)
                y = int(mouse_pos[1]//sapper_game.side_size)

                sapper_game.update(x, y, event.button)

    if sapper_game.result != 0:
        game_view.update(WIN, WIN_SIZE, sapper_game.mine_field)
        WIN.blit(sapper_game.victory_label, ((WIN_SIZE[0] - sapper_game.victory_label.get_width())/2,
                                             (WIN_SIZE[1] - sapper_game.victory_label.get_height())/2))

        pg.display.update()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

    game_view.update(WIN, WIN_SIZE, sapper_game.mine_field)
    pg.display.update()
