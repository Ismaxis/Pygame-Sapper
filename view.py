import pygame as pg
import variables


WIN = variables.WIN
WIN_SIZE = variables.WIN_SIZE


class Menu_view:
    def update(self, menu):
        self.draw_banner(menu.name_banner)
        self.draw_button(menu.start_button)

        pg.display.update()

    def draw_banner(self, banner):
        WIN.blit(banner.label, banner.pos)

    def draw_button(self, button):
        pg.draw.rect(WIN, button.color[button.status], button.rect)
        WIN.blit(button.label, button.label_pos)
