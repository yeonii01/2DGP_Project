import play_state
import game_framework
from pico2d import *
import math
PIXEL_PER_METER = (10.0/ 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_KMPH*PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

class WAKE:
    @staticmethod
    def enter(self):
        global FRAMES_PER_ACTION
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 5
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if math.fabs(self.x - play_state.knight.x) <= 300:
                self.cur_state = WALK
    @staticmethod
    def draw(self):
        self.bossimage.clip_composite_draw(int(self.frame) * 430, 6916, 434, 347,0,'h', self.x - play_state.knight.x + 400,
                                            self.y, 144, 115)

class WALK:
    @staticmethod
    def enter(self):
        global FRAMES_PER_ACTION
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 10
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        if math.fabs(self.x - play_state.knight.x) <= 200:
                self.cur_state = RUN

    @staticmethod
    def draw(self):
        if self.frame < 6:
            self.bossimage.clip_composite_draw(int(self.frame) * 442, 5868, 496, 354,0,'h', self.x - play_state.knight.x + 400,
                                            self.y, 144, 115)
        else:
            self.bossimage.clip_composite_draw((int(self.frame) - 6) * 442, 5513, 496, 354,0,'h', self.x - play_state.knight.x + 400,
                                            self.y, 144, 115)
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
        self.x, self.y = 8600, 130
        self.frame = 0
        self.timer = 0
        self.cur_state = WAKE
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