from pico2d import *
import play_state
import math

class IDLE:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 6
        if math.fabs(self.x - play_state.Knight.x) <= 400:
            self.cur_state = RUN


    @staticmethod
    def draw(self):
        self.ground_monster_image.clip_draw(self.frame*122, 1394, 122, 220, self.x-play_state.Knight.x + 400, self.y,75,105)


class RUN:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        if self.x - play_state.Knight.x <= 0:
            self.dir = 1
        else:
            self.dir = -1
        self.x += self.dir * 5
        self.frame = (self.frame+1) % 7
        if math.fabs(self.x - play_state.Knight.x) <= 200:
            self.cur_state = READYATTACK
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(self.frame * 142, 1182, 142, 200, self.x - play_state.Knight.x + 400,
                                            self.y, 75, 105)
        else:
            self.ground_monster_image.clip_composite_draw(self.frame * 142, 1182, 142, 200, 0,'h',self.x - play_state.Knight.x + 400,
                                            self.y, 75, 105)

class READYATTACK:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 5
        if self.frame == 0:
            self.cur_state = ATTACK
        pass
    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(self.frame * 175, 749, 175, 210, self.x - play_state.Knight.x + 400,
                                            self.y, 105, 105)
        else:
            self.ground_monster_image.clip_composite_draw(self.frame * 175, 749, 175, 210,0,'h', self.x - play_state.Knight.x + 400,
                                            self.y, 105, 105)


class ATTACK:
    @staticmethod
    def enter(self):
        pass

    @staticmethod
    def exit(self):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 4
        if self.frame == 0:
            self.cur_state = RUN
        self.x += self.dir * 10
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(self.frame * 186, 615, 186, 150, self.x - play_state.Knight.x + 400,
                                            self.y, 120, 90)
        else:
            self.ground_monster_image.clip_composite_draw(self.frame * 186, 615, 186, 150, 0,'h',self.x - play_state.Knight.x + 400,
                                            self.y, 120, 90)
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
        self.frame = (self.frame + 1) % 5
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(self.frame * 199, 131, 199, 143, self.x - play_state.Knight.x + 400,
                                            self.y, 120, 90)
        else:
            self.ground_monster_image.clip_composite_draw(self.frame * 199, 131, 199, 143, 0,'h',self.x - play_state.Knight.x + 400,
                                            self.y, 120, 90)
        pass


class groundmonster:
    def __init__(self):
        self.x, self.y = 900, 120
        self.frame = 0

        self.cur_state = IDLE
        self.dir = -1
        self.life = 5
        self.cur_state.enter(self)
        self.ground_monster_image = load_image('ground_monster1.png')
    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)