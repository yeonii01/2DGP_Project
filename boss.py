import play_state
from pico2d import *

class KEY:
    def __init__(self):
        self.x, self.y = 6200, 420
        self.keyimage = load_image('key.png')
        self.keyget = False
        self.keycount = 0
        pass

    def update(self):
        pass

    def draw(self):
        if self.keyget== False:
            self.keyimage.clip_draw(0, 0, 840, 859, self.x - play_state.knight.x + 400, self.y,40,40)
        else:
            self.keyimage.clip_draw(0, 0, 840, 859 , 40 , 450, 40, 40)
            pass

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 20, self.y - 20, self.x - play_state.knight.x + 400 + 20, self.y + 20