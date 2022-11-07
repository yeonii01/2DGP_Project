import play_state
from pico2d import *

class Ground:
    def __init__(self):
        self.floor_image = load_image('floor.png')
        self.x, self.y = 0, 70

    def update(self):
        pass

    def draw(self):
        self.floor_image.clip_draw(0, 0, 150, 25, self.x - play_state.knight.x + 400, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 75, self.y - 10, self.x - play_state.knight.x + 400 + 70, self.y + 10