import pygame as pg


class Button:
    def __init__(self, pos, size, text, color):
        self.pos = pos
        self.size = size
        self.font = pg.font.SysFont("comics", 50)
        self.label = self.font.render(text, True, (0, 0, 0))
        self.color = color
        self.status = False
        self.selected = False

        self.rect = (pos[0] - self.size[0]/2, pos[1] - self.size[1]/2,
                     self.size[0], self.size[1])

        self.label_pos = (pos[0] - self.label.get_width()/2,
                          pos[1] - self.label.get_height()/2)


class Banner:
    def __init__(self, pos, text, color):
        self.font = pg.font.SysFont("arial", 100)
        self.label = self.font.render(text, True, color)

        self.pos = (pos[0] - self.label.get_width()/2,
                    pos[1] + self.label.get_height()/2)


class Start_menu:
    def __init__(self, win_size):
        banner_pos = (win_size[0]/2, win_size[1]/14)
        banner_color = (255, 255, 255)
        banner_text = "Sapper game"

        # Start button
        button_pos = (win_size[0]/2, win_size[1]/2)
        button_size = (250, 100)
        button_text = "Press to start"
        button_color = ((255, 255, 255), (128, 128, 128))

        # Difficult buttons
        dif_size = (200, 100)
        low_dif_color = ((50, 255, 50), (200, 255, 200))
        med_dif_color = ((50, 50, 255), (200, 200, 255))
        high_dif_color = ((255, 50, 50), (255, 200, 200))
        gap = win_size[0]/100

        low_dif_pos = (win_size[0]/2 - dif_size[0] - gap, win_size[1] * 11/14)
        med_dif_pos = (win_size[0]/2,  win_size[1] * 11/14)
        high_dif_pos = (win_size[0]/2 + dif_size[0] + gap, win_size[1] * 11/14)

        # Components
        self.name_banner = Banner(banner_pos, banner_text, banner_color)

        self.start_button = Button(button_pos, button_size,
                                   button_text, button_color)

        self.low_dif_button = Button(
            low_dif_pos, dif_size, "Easy", low_dif_color)
        self.med_dif_button = Button(
            med_dif_pos, dif_size, "Medium", med_dif_color)
        self.high_dif_button = Button(
            high_dif_pos, dif_size, "Hard", high_dif_color)

    def change_status(self, button, status):
        button.status = status

    def select(self, cur_button):
        for button in self.buttons():
            button.selected = False
        cur_button.selected = True

    def buttons(self):
        return (self.start_button, self.low_dif_button,
                self.med_dif_button, self.high_dif_button)
