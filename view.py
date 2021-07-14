import pygame as pg
import variables


WIN = variables.WIN
WIN_SIZE = variables.WIN_SIZE
GRID_SIZE = variables.GRID_SIZE
SIDE_SIZE = variables.SIDE_SIZE


class Menu_view:
    def update(self, menu):
        self.draw_banner(menu.name_banner)
        self.draw_button(menu.start_button)

        pg.display.update()

    @staticmethod
    def draw_banner(banner):
        WIN.blit(banner.label, banner.pos)

    @staticmethod
    def draw_button(button):
        pg.draw.rect(WIN, button.color[button.status], button.rect)
        WIN.blit(button.label, button.label_pos)


class Field_view:
    def update(self, field):
        # draw rects
        for line in field.field:
            for cage in line:
                self.draw_cage(cage)

        # draw lines
        for i in range(GRID_SIZE):
            pg.draw.line(WIN, (255, 255, 255),
                         (0, i * SIDE_SIZE), (WIN_SIZE[1], i * SIDE_SIZE), 3)
            pg.draw.line(WIN, (255, 255, 255),
                         (i * SIDE_SIZE, 0), (i * SIDE_SIZE, WIN_SIZE[1]), 3)

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
                hint_label, (cage.rect[0] + (SIDE_SIZE - hint_label.get_width())/2, cage.rect[1] + (SIDE_SIZE - hint_label.get_height())/2))
