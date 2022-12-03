import play_state
from pico2d import *

PIXEL_PER_METER = (10.0/ 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_KMPH*PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

class IDLE:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        pass

    @staticmethod
    def draw(self):
        pass
class RUN:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        pass

    @staticmethod
    def draw(self):
        pass

class READYATTACK:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        pass

    @staticmethod
    def draw(self):
        pass
class ATTACK:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        pass

    @staticmethod
    def draw(self):
        pass

class DIE:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        pass
    @staticmethod
    def draw(self):
        pass


class BOSS:
    def __init__(self):
        self.x, self.y = 1700, 120
        self.frame = 0
        self.timer = 0
        self.cur_state = IDLE
        self.dir = -1
        self.life = 7
        self.cur_state.enter(self)
        self.bossimage = load_image('boss_sprite.png')

    def update(self):
        if self.timer >= 0:
            self.timer -= 1
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 50, self.y - 50, self.x - play_state.knight.x + 400 + 50, self.y + 50

class KEY:
    def __init__(self):
        self.x, self.y = 6200, 420
        self.keyimage = load_image('key.png')
        self.onoff = True
        self.keyget = False
        pass

    def update(self):
        pass

    def draw(self):
        if self.onoff == True:
            if self.keyget== False:
                self.keyimage.clip_draw(0, 0, 840, 859, self.x - play_state.knight.x + 400, self.y,40,40)
            else:
                self.keyimage.clip_draw(0, 0, 840, 859, 40, 450, 40, 40)

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 20, self.y - 20, self.x - play_state.knight.x + 400 + 20, self.y + 20