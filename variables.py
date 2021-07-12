import pygame as pg
import os
WIN_SIZE = (1000, 1000)
WIN = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption("Sapper")
GRID_SIZE = 10
SIDE_SIZE = int(WIN_SIZE[1] // GRID_SIZE)
flag = pg.transform.scale(pg.image.load(os.path.join(
    "images", "flag.png")), (SIDE_SIZE, SIDE_SIZE))
