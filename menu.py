import pygame as pg
from visual_components import Button, Banner


class Start_menu:
    def __init__(self, win_size):
        # Banner
        banner_pos = (win_size[0]/2, win_size[1]/14)
        banner_color = (255, 255, 255)
        banner_text = "Sapper game"

        # Start button
        button_pos = (win_size[0]/2, win_size[1]/2)
        button_size = (250, 100)
        button_text = "Press to start"
        button_color = ((200, 200, 200), (255, 255, 255))

        # Difficult buttons
        dif_size = (200, 100)
        low_dif_color = ((50, 255, 50), (150, 255, 150))
        med_dif_color = ((50, 50, 255), (150, 150, 255))
        high_dif_color = ((255, 50, 50), (255, 150, 150))
        gap = win_size[0]/100

        low_dif_pos = (win_size[0]/2 - dif_size[0] - gap, win_size[1] * 11/14)
        med_dif_pos = (win_size[0]/2,  win_size[1] * 11/14)
        high_dif_pos = (win_size[0]/2 + dif_size[0] + gap, win_size[1] * 11/14)

        # Components
        self.name_banner = Banner(banner_pos, banner_text, banner_color, 100)

        self.start_button = Button(button_pos, button_size,
                                   button_text, button_color)

        self.low_dif_button = Button(
            low_dif_pos, dif_size, "Easy", low_dif_color)
        self.med_dif_button = Button(
            med_dif_pos, dif_size, "Medium", med_dif_color)
        self.high_dif_button = Button(
            high_dif_pos, dif_size, "Hard", high_dif_color)

    def select(self, cur_button):
        for button in self.buttons():
            button.selected = False
        cur_button.selected = True

    def buttons(self):
        return (self.start_button, self.low_dif_button,
                self.med_dif_button, self.high_dif_button)

    @staticmethod
    def change_status(button, status):
        button.status = status
