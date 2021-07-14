import pygame as pg
import variables


WIN = variables.WIN
WIN_SIZE = variables.WIN_SIZE


class Menu_view:
    banner_font = pg.font.SysFont("arial", 100)
    banner_label = banner_font.render("Sapper game", True, (255, 255, 255))

    button_text = 'Press to start'
    button_font = pg.font.SysFont("comics", 50)
    button_label = button_font.render(button_text, True, (0, 0, 0))
    button_color = (255, 255, 255)

    def update(self, pos, button_size, is_active):
        self.draw_banner(pos)
        self.draw_button(pos, button_size, is_active)

        pg.display.update()

    def draw_banner(self, pos):
        banner_pos = (pos[0] - self.banner_label.get_width()/2,
                      pos[1]/7 + self.banner_label.get_height()/2)

        WIN.blit(self.banner_label, banner_pos)

    def draw_button(self, pos, button_size, is_active):
        if is_active:
            self.button_color = (128, 128, 128)
        else:
            self.button_color = (255, 255, 255)

        button_rect = (pos[0] - button_size[0]/2, pos[1] - button_size[1]/2,
                       button_size[0], button_size[1])

        button_label_pos = (pos[0] - self.button_label.get_width()/2,
                            pos[1] - self.button_label.get_height()/2)

        pg.draw.rect(WIN, self.button_color, button_rect)
        WIN.blit(self.button_label, button_label_pos)
