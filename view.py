import pygame as pg
import variables


WIN = variables.WIN
WIN_SIZE = variables.WIN_SIZE


class Menu_view:
    def update(self, menu):
        self.draw_banner(menu.name_banner)
        self.draw_button(menu.start_button)

        # Difficults buttons
        self.draw_button(menu.low_dif_button)
        self.draw_button(menu.med_dif_button)
        self.draw_button(menu.high_dif_button)

        pg.display.update()

    @staticmethod
    def draw_banner(banner):
        WIN.blit(banner.label, banner.pos)

    @staticmethod
    def draw_button(button):
        if button.selected:
            pg.draw.rect(WIN, button.color[1], button.rect)
        else:
            pg.draw.rect(WIN, button.color[button.status], button.rect)
        WIN.blit(button.label, button.label_pos)


class Field_view:
    def update(self, field):
        # draw rects
        for line in field.field:
            for cage in line:
                self.draw_cage(cage)

        # draw lines
        for i in range(field.grid_size):
            pg.draw.line(WIN, (255, 255, 255),
                         (0, i * field.side_size), (WIN_SIZE[1], i * field.side_size), 3)
            pg.draw.line(WIN, (255, 255, 255),
                         (i * field.side_size, 0), (i * field.side_size, WIN_SIZE[1]), 3)

        pg.display.update()

    @staticmethod
    def draw_cage(cage):
        # defusion
        if cage.defused:
            if cage.opened and cage.is_mine:
                color = (200, 50, 50)
                pg.draw.rect(WIN, color, cage.rect)
            WIN.blit(cage.flag, (cage.rect[0], cage.rect[1]))
            return

        # color definition
        color = (128, 128, 128)
        if cage.is_mine and cage.opened:
            color = (255, 50, 50)
        if cage.opened and not cage.is_mine:
            color = (200, 200, 200)

        pg.draw.rect(WIN, color, cage.rect)

        # hint
        if cage.opened and not cage.is_mine:
            hint_label = cage.hint_font.render(
                f'{cage.hint}', True, (255, 255, 255))
            WIN.blit(
                hint_label, (cage.rect[0] + (cage.side_size - hint_label.get_width())/2, cage.rect[1] + (cage.side_size - hint_label.get_height())/2))
