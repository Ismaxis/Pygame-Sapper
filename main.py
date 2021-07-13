import pygame as pg
from game import game
import variables
pg.font.init()


BANNER_FONT = pg.font.SysFont("arial", 100)
BUTTON_FONT = pg.font.SysFont("comics", 50)
WIN_SIZE = variables.WIN_SIZE
WIN = variables.WIN


class Menu:
    background = None  # todo - create bg image
    button_size = (250, 100)

    banner = BANNER_FONT.render("Sapper game", True, (255, 255, 255))

    def __init__(self):
        center = (WIN_SIZE[0]/2, WIN_SIZE[1]/2)
        self.button = StartButton(self.button_size, center)

        self.banner_pos = (
            center[0] - self.banner.get_width()/2, center[1]/7 + self.banner.get_height()/2)

        del center

    def update(self, mouse_pressed):
        if self.button.active(pg.mouse.get_pos()):
            self.button.color = (128, 128, 128)
            if mouse_pressed:
                return True
        else:
            self.button.color = (255, 255, 255)
        self.draw()

    def draw(self):
        WIN.blit(self.banner, self.banner_pos)
        self.button.draw()


class StartButton:
    color = (255, 255, 255)
    text = 'Press to start'
    label = BUTTON_FONT.render(text, True, (0, 0, 0))

    def __init__(self, size, pos):
        self.pos = pos
        self.size = size
        self.label_pos = (pos[0] - self.label.get_width()/2,
                          pos[1] - self.label.get_height()/2)
        self.rect = (pos[0] - size[0]/2, pos[1] - size[1]/2, size[0], size[1])

    def draw(self):
        pg.draw.rect(WIN, self.color, self.rect)
        WIN.blit(self.label, self.label_pos)

    def active(self, mouse_pos):
        if self.pos[0] - self.size[0]/2 <= mouse_pos[0] <= self.pos[0] + self.size[0]/2\
                and self.pos[1] - self.size[1]/2 <= mouse_pos[1] <= self.pos[1] + self.size[1]/2:
            return True


def menu():
    menu = Menu()

    mouse_pressed = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pressed = True

        if menu.update(mouse_pressed):
            WIN.fill((0, 0, 0))
            game()
        mouse_pressed = False
        pg.display.update()


input()
# launch menu
menu()
