import pygame as pg


class Menu_view:
    def update(self, win, menu):
        win.fill((0, 0, 0))
        self.draw_banner(win, menu.name_banner)
        self.draw_button(win, menu.start_button)

        # Difficults buttons
        self.draw_button(win, menu.low_dif_button)
        self.draw_button(win, menu.med_dif_button)
        self.draw_button(win, menu.high_dif_button)

        pg.display.update()

    @staticmethod
    def draw_banner(win, banner):
        win.blit(banner.label, banner.pos)

    @staticmethod
    def draw_button(win, button):
        if button.selected:
            pg.draw.rect(win, button.color[1], button.rect)
        else:
            pg.draw.rect(win, button.color[button.status], button.rect)
        win.blit(button.label, button.label_pos)


class Field_view:
    def update(self, win, win_size, field):
        win.fill((0, 0, 0))

        # draw rects
        for line in field.field:
            for cage in line:
                self.draw_cage(win, cage)

        # draw lines
        for i in range(field.grid_size):
            pg.draw.line(win, (255, 255, 255),
                         (0, i * field.side_size), (win_size[1] - 3, i * field.side_size), 3)
            pg.draw.line(win, (255, 255, 255),
                         (i * field.side_size, 0), (i * field.side_size, win_size[1]), 3)

    @staticmethod
    def draw_cage(win, cage):
        # defusion
        if cage.defused:
            if cage.opened and cage.is_mine:
                color = (200, 50, 50)
                pg.draw.rect(win, color, cage.rect)
            else:
                color = cage.close_color
                pg.draw.rect(win, color, cage.rect)
            win.blit(cage.flag, (cage.rect[0], cage.rect[1]))
            return

        # color definition
        color = (128, 128, 128)
        if cage.is_mine and cage.opened:
            color = (255, 50, 50)
        if cage.opened and not cage.is_mine:
            color = (200, 200, 200)

        pg.draw.rect(win, color, cage.rect)

        # hint
        if cage.opened and not cage.is_mine:
            hint_label = cage.hint_font.render(
                f'{cage.hint}', True, (255, 255, 255))
            win.blit(
                hint_label, (cage.rect[0] + (cage.side_size - hint_label.get_width())/2, cage.rect[1] + (cage.side_size - hint_label.get_height())/2))


class Panel_view:
    def update(self, win, win_size, panel):
        pg.draw.rect(win, (0, 0, 0), panel.get_rect(win_size))

        banner_pos = panel.banner_pos(win_size)
        self.draw_banner(win, panel.defuse_banner.label, banner_pos)

    @staticmethod
    def draw_banner(win, label, pos):
        win.blit(label, pos)
