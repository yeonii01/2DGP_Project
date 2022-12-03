import play_state
from pico2d import *

class Ground:
    def __init__(self):
        self.floor_image = load_image('floor.png')
        self.x, self.y = 0, 70

    def update(self):
        pass

    def draw(self):
        self.floor_image.clip_draw(0, 0, 150, 25, self.x - play_state.knight.x + 400, self.y - play_state.elev.savey)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 75, self.y - 10, self.x - play_state.knight.x + 400 + 70, self.y + 10



class FGround:
    def __init__(self):
        self.floor_image = load_image('fground.png')
        self.x, self.y = 0, 140
    def update(self):
        pass
    def draw(self):
        self.floor_image.clip_draw(0, 0, 172, 74, self.x - play_state.knight.x + 400, self.y - play_state.elev.savey, 150, 60)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 75, self.y - 30, self.x - play_state.knight.x + 400 + 70, self.y + 20


class SecondGround:
    def __init__(self):
        self.floor_image = load_image('floor.png')
        self.x, self.y = 0, 70

    def update(self):
        pass

    def draw(self):
        self.floor_image.clip_draw(0, 0, 150, 25, self.x - play_state.knight.x + 400, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 75, self.y - 10, self.x - play_state.knight.x + 400 + 70, self.y + 10

class Elevator:
    def __init__(self):
        self.image = load_image('elev.png')
        self.sFloor = False
        self.x, self.y, self.savex, self.plusy = 4200, 70, 0, 0
        self.savey,dir = 0, 1
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 235, 182, self.x - play_state.knight.x + 400, self.y+self.plusy, 175, 136)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 80, self.y + self.plusy - 10, self.x - play_state.knight.x + 400 + 80, self.y + self. plusy + 10
