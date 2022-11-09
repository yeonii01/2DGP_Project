import play_state
from pico2d import *

class Obstacle:
    def __init__(self):
        self.floor_image = load_image('spike.png')
        self.x, self.y = 0, 0

    def update(self):
        pass

    def draw(self):
        self.floor_image.clip_draw(0, 0, 139, 105, self.x - play_state.knight.x + 400, 60)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 75, self.y - 50, self.x - play_state.knight.x + 400 + 70, self.y + 90