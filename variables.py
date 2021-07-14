import pygame as pg
import os
WIN_SIZE = (800, 800)
WIN = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption("Sapper")


GRID_SIZE = 20
MINES_AMOUNT = 30
SIDE_SIZE = int(WIN_SIZE[1] // GRID_SIZE)
flag = pg.transform.scale(pg.image.load(os.path.join(
    "images", "flag.png")), (SIDE_SIZE, SIDE_SIZE))
