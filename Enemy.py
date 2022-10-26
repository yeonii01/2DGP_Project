from pico2d import *
import play_state

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
        pass

    @staticmethod
    def draw(self):
        self.ground_monster_image.clip_draw(self.frame*122, 1394, 122, 220, self.x-play_state.Knight.x + 400, self.y,75,105)
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

class TURN:
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


class groundmonster:
    def __init__(self):
        self.x, self.y = 800, 120
        self.frame = 0
        self.event_que = []
        self.cur_state = IDLE

        self.cur_state.enter(self)
        self.ground_monster_image = load_image('ground_monster1.png')
    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)