import variables

WIN_SIZE = variables.WIN_SIZE
WIN = variables.WIN


class Start_menu:
    win_center = (WIN_SIZE[0]/2, WIN_SIZE[1]/2)

    banner_pos = (WIN_SIZE[0]/2, WIN_SIZE[1]/14)

    button_pos = (WIN_SIZE[0]/2, WIN_SIZE[1]/2)
    button_status = False
    button_size = (250, 100)

    def change_status(self, status):
        self.button_status = status
