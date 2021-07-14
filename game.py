import pygame as pg
import random
import variables
from fill import fill
pg.font.init()


HINT_FONT = pg.font.SysFont("consolas", 25)
WIN = variables.WIN
WIN_SIZE = variables.WIN_SIZE
GRID_SIZE = variables.GRID_SIZE
MINES_AMOUNT = variables.MINES_AMOUNT
SIDE_SIZE = variables.SIDE_SIZE
GAME_END = False


class Cage:
    flag = variables.flag

    def __init__(self, pos, side_size):
        self.pos = pos
        self.side_size = side_size
        self.is_mine = False
        self.hint = 0
        self.opened = False
        self.defused = False

    def draw(self):
        rect = (self.side_size * self.pos[0],
                self.side_size * self.pos[1], self.side_size, self.side_size)

        # defusion
        if self.defused:
            if self.opened and self.is_mine:
                color = (200, 50, 50)
                pg.draw.rect(WIN, color, rect)
            WIN.blit(self.flag, (rect[0], rect[1]))
            return

        # color definition
        color = (128, 128, 128)
        if self.is_mine and self.opened:
            color = (255, 50, 50)
        if self.opened and not self.is_mine:
            color = (200, 200, 200)

        pg.draw.rect(WIN, color, rect)

        # hint
        if self.opened and not self.is_mine:
            hint_label = HINT_FONT.render(
                f'{self.hint}', True, (255, 255, 255))
            WIN.blit(
                hint_label, (rect[0] + (self.side_size - hint_label.get_width())/2, rect[1] + (self.side_size - hint_label.get_height())/2))


class Mine_field:
    def __init__(self, grid_size, mines_amount, section_size):
        self.field = []  # array of
        self.grid_size = grid_size
        self.side_size = section_size / self.grid_size
        self.mines_amount = mines_amount
        self.defuse_amount = 0

        # generate grid
        for i in range(grid_size):
            self.field.append([])
            for j in range(grid_size):
                self.field[i].append(Cage((i, j), self.side_size))

        # placing mines
        for _ in range(mines_amount):
            while True:
                x = random.randint(0, grid_size - 1)
                y = random.randint(0, grid_size - 1)
                if self.field[x][y].is_mine == False:
                    self.field[x][y].is_mine = True
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + i < grid_size and 0 <= y + j < grid_size and (i != 0 or j != 0):
                                self.field[x + i][y + j].hint += 1
                    break
                else:
                    continue
        print()

    def draw(self, section_size):
        # draw rects
        for line in self.field:
            for cage in line:
                cage.draw()

        # draw lines
        for i in range(self.grid_size):
            pg.draw.line(WIN, (255, 255, 255),
                         (0, i * self.side_size), (section_size, i * self.side_size), 3)
            pg.draw.line(WIN, (255, 255, 255),
                         (i * self.side_size, 0), (i * self.side_size, section_size), 3)

    def open(self, mouse_pos):
        x = int(mouse_pos[0]//self.side_size)
        y = int(mouse_pos[1]//self.side_size)

        if not self.field[x][y].opened and not self.field[x][y].defused and self.field[x][y].hint == 0:
            fill(self, self.field[x][y])

        elif not self.field[x][y].defused:
            self.field[x][y].opened = True

    def defuse(self, mouse_pos):
        x = int(mouse_pos[0]//self.side_size)
        y = int(mouse_pos[1]//self.side_size)

        if not self.field[x][y].defused:
            self.defuse_amount += 1

            if self.defuse_amount <= self.mines_amount and not self.field[x][y].opened:
                self.field[x][y].defused = True
            else:
                self.defuse_amount -= 1
                # place for message what amount of defusions is maximum

        elif self.field[x][y].defused:
            self.defuse_amount -= 1
            self.field[x][y].defused = False

    def defeat_check(self, mouse_pos, field):
        global GAME_END

        x = int(mouse_pos[0]//self.side_size)
        y = int(mouse_pos[1]//self.side_size)

        if self.field[x][y].is_mine and not self.field[x][y].defused:
            victory_label = pg.font.SysFont(
                "consolas", 200).render("Defeat!", True, (255, 40, 80))

            for line in field.field:
                for cage in line:
                    cage.opened = True

            field.draw(WIN_SIZE[1])
            WIN.blit(victory_label, ((WIN_SIZE[0] - victory_label.get_width())/2,
                                     (WIN_SIZE[1] - victory_label.get_height())/2))

            pg.display.update()
            GAME_END = True

    def victory_check(self, field):
        global GAME_END

        victory = True
        for line in field.field:
            for cage in line:
                if cage.is_mine and not cage.defused:
                    victory = False

        if victory:
            victory_label = pg.font.SysFont(
                "consolas", 200).render("Win!", True, (40, 255, 80))

            for line in field.field:
                for cage in line:
                    cage.opened = True

            field.draw(WIN_SIZE[1])
            WIN.blit(victory_label, ((WIN_SIZE[0] - victory_label.get_width())/2,
                                     (WIN_SIZE[1] - victory_label.get_height())/2))

            pg.display.update()
            GAME_END = True


def sapper_game():
    field = Mine_field(GRID_SIZE, MINES_AMOUNT, WIN_SIZE[1])
    while True:
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                if mouse_pos[0] < WIN_SIZE[1]:
                    field.open(mouse_pos)
                    field.defeat_check(mouse_pos, field)

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:

                if mouse_pos[0] < WIN_SIZE[1]:
                    field.defuse(mouse_pos)

        field.victory_check(field)

        if GAME_END:
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()

        field.draw(WIN_SIZE[1])
        pg.display.update()
