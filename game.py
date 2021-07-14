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


class Cage:
    flag = variables.flag

    def __init__(self, pos):
        self.pos = pos
        self.is_mine = False
        self.hint = 0
        self.opened = False
        self.defused = False

    def draw(self):
        rect = (SIDE_SIZE * self.pos[0],
                SIDE_SIZE * self.pos[1], SIDE_SIZE, SIDE_SIZE)

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
                hint_label, (rect[0] + (SIDE_SIZE - hint_label.get_width())/2, rect[1] + (SIDE_SIZE - hint_label.get_height())/2))


class Mine_field:
    def __init__(self, mines_amount):
        self.field = []  # array of
        self.defuse_amount = 0

        # generate grid
        for i in range(GRID_SIZE):
            self.field.append([])
            for j in range(GRID_SIZE):
                self.field[i].append(Cage((i, j), SIDE_SIZE))

        # placing mines
        for _ in range(mines_amount):
            while True:
                x = random.randint(0, GRID_SIZE - 1)
                y = random.randint(0, GRID_SIZE - 1)
                if self.field[x][y].is_mine == False:
                    self.field[x][y].is_mine = True
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + i < GRID_SIZE and 0 <= y + j < GRID_SIZE and (i != 0 or j != 0):
                                self.field[x + i][y + j].hint += 1
                    break
                else:
                    continue

    def draw(self):
        # draw rects
        for line in self.field:
            for cage in line:
                cage.draw()

        # draw lines
        for i in range(GRID_SIZE):
            pg.draw.line(WIN, (255, 255, 255),
                         (0, i * SIDE_SIZE), (WIN_SIZE[1], i * SIDE_SIZE), 3)
            pg.draw.line(WIN, (255, 255, 255),
                         (i * SIDE_SIZE, 0), (i * SIDE_SIZE, WIN_SIZE[1]), 3)

    def update(self, x, y, button):
        pass

    def open(self, mouse_pos):

        if not self.field[x][y].opened and not self.field[x][y].defused and self.field[x][y].hint == 0:
            fill(self, self.field[x][y])

        elif not self.field[x][y].defused:
            self.field[x][y].opened = True

    def defuse(self, mouse_pos):
        x = int(mouse_pos[0]//SIDE_SIZE)
        y = int(mouse_pos[1]//SIDE_SIZE)

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
        x = int(mouse_pos[0]//SIDE_SIZE)
        y = int(mouse_pos[1]//SIDE_SIZE)

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

    def victory_check(self, field):
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

            field.draw()
            WIN.blit(victory_label, ((WIN_SIZE[0] - victory_label.get_width())/2,
                                     (WIN_SIZE[1] - victory_label.get_height())/2))

            pg.display.update()
