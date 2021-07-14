import variables

GRID_SIZE = variables.GRID_SIZE


def fill(field, cur_cage):
    cur_cage.update(True, False)

    x = cur_cage.pos[0]
    y = cur_cage.pos[1]

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < GRID_SIZE and 0 <= y + j < GRID_SIZE and (i != 0 or j != 0):
                if not field.field[x + i][y + j].opened and not field.field[x + i][y + j].defused and field.field[x + i][y + j].hint == 0:
                    fill(field, field.field[x + i][y + j])
                if not field.field[x + i][y + j].opened and not field.field[x + i][y + j].defused and field.field[x + i][y + j].hint != 0:
                    field.field[x + i][y + j].update(True, False)
