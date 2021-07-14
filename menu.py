import variables
import pygame as pg

WIN_SIZE = variables.WIN_SIZE
WIN = variables.WIN


class Button:
    def __init__(self, pos, size, text, color):
        self.size = size
        self.font = pg.font.SysFont("comics", 50)
        self.label = self.font.render(text, True, (0, 0, 0))
        self.color = color
        self.status = 0

        self.rect = (pos[0] - self.size[0]/2, pos[1] - self.size[1]/2,
                     self.size[0], self.size[1])

        self.label_pos = (pos[0] - self.label.get_width()/2,
                          pos[1] - self.label.get_height()/2)

    def change_status(self, status):
        self.status = status


class Banner:
    def __init__(self, pos, text, color):
        self.font = pg.font.SysFont("arial", 100)
        self.label = self.font.render(text, True, color)

        self.pos = (pos[0] - self.label.get_width()/2,
                    pos[1]/7 + self.label.get_height()/2)


class Start_menu:
    banner_pos = (WIN_SIZE[0]/2, WIN_SIZE[1]/14)
    banner_color = (255, 255, 255)
    banner_text = "Sapper game"

    button_pos = (WIN_SIZE[0]/2, WIN_SIZE[1]/2)
    button_status = False
    button_size = (250, 100)
    button_text = "Press to start"
    button_color = ((255, 255, 255), (128, 128, 128))

    name_banner = Banner(banner_pos, banner_text, banner_color)

    start_button = Button(button_pos, button_size, button_text, button_color)

    def change_status(self, button, status):
        button.change_status(status)
