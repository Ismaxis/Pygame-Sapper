import pygame as pg
import random
import variables
from fill import fill
pg.font.init()


WIN = variables.WIN
WIN_SIZE = variables.WIN_SIZE
GRID_SIZE = variables.GRID_SIZE
MINES_AMOUNT = variables.MINES_AMOUNT
SIDE_SIZE = variables.SIDE_SIZE


class Cage:
    flag = variables.flag
    hint_font = pg.font.SysFont("consolas", 25)

    close_color = (128, 128, 128)
    open_color = (200, 200, 200)
    mine_color = (255, 50, 50)

    def __init__(self, pos):
        self.pos = pos
        self.is_mine = False
        self.hint = 0
        self.opened = False
        self.defused = False
        self.rect = (SIDE_SIZE * self.pos[0],
                     SIDE_SIZE * self.pos[1], SIDE_SIZE, SIDE_SIZE)
        self.color = self.close_color

    def update(self, open, defuse):
        self.opened = open
        self.defused = defuse

        if open and not self.is_mine:
            self.color = self.mine_color

        elif open:
            self.color = self.open_color


class Mine_field:
    def __init__(self, mines_amount):
        self.field = []  # array of
        self.defuse_amount = 0

        # generate grid
        for i in range(GRID_SIZE):
            self.field.append([])
            for j in range(GRID_SIZE):
                self.field[i].append(Cage((i, j)))

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

    def update(self, x, y, button):
        if button == 1:
            if not self.field[x][y].opened and not self.field[x][y].defused and self.field[x][y].hint == 0:
                fill(self, self.field[x][y])

            elif not self.field[x][y].defused:
                self.field[x][y].update(True, False)

        elif button == 3:
            if not self.field[x][y].defused:
                self.defuse_amount += 1

                if self.defuse_amount <= MINES_AMOUNT and not self.field[x][y].opened:
                    self.field[x][y].update(False, True)
                else:
                    self.defuse_amount -= 1
                    # place for message what amount of defusions is maximum

            elif self.field[x][y].defused:
                self.defuse_amount -= 1
                self.field[x][y].update(False, False)


class Game:
    def __init__(self, mines_amount):
        self.mine_field = Mine_field(mines_amount)
        self.result = 0
        self.victory_label = None

    def update(self, x, y, button):
        self.mine_field.update(x, y, button)
        if button == 1:
            self.defeat_check(x, y)
        elif button == 3:
            self.victory_check()

    def defeat_check(self, x, y):
        if self.mine_field.field[x][y].is_mine and not self.mine_field.field[x][y].defused:
            self.result = -1

            self.victory_label = pg.font.SysFont(
                "consolas", 200).render("Defeat!", True, (255, 40, 80))

            for line in self.mine_field.field:
                for cage in line:
                    cage.opened = True

    def victory_check(self):
        for line in self.mine_field.field:
            for cage in line:
                if cage.is_mine and not cage.defused:
                    return

        self.result = 1

        self.victory_label = pg.font.SysFont(
            "consolas", 200).render("Win!", True, (40, 255, 80))

        for line in self.mine_field.field:
            for cage in line:
                cage.opened = True
