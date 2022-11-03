from pico2d import *
import play_state
import math
import game_framework
import random

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
        global FRAMES_PER_ACTION
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 6
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        if math.fabs(self.x - play_state.knight.x) <= 400:
            self.cur_state = RUN


    @staticmethod
    def draw(self):
        self.ground_monster_image.clip_draw(int(self.frame)*122, 1394, 122, 220, self.x-play_state.knight.x + 400, self.y,75,105)


class RUN:
    @staticmethod
    def enter(self):
        global FRAMES_PER_ACTION
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        if self.x - play_state.knight.x <= 0:
            self.dir = 1
        else:
            self.dir = -1
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * 0.1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        if math.fabs(self.x - play_state.knight.x) <= 200:
            if self.timer <= 0:
                self.cur_state = READYATTACK
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(int(self.frame) * 142, 1182, 142, 200, self.x - play_state.knight.x + 400,
                                            self.y, 75, 105)
        else:
            self.ground_monster_image.clip_composite_draw(int(self.frame) * 142, 1182, 142, 200, 0,'h',self.x - play_state.knight.x + 400,
                                            self.y, 75, 105)

class READYATTACK:
    @staticmethod
    def enter(self):
        global FRAMES_PER_ACTION
        self.frame = 0
        pass

    @staticmethod
    def exit(self):
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 5
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if self.frame >= 5:
            self.cur_state = ATTACK
        pass
    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(int(self.frame) * 175, 749, 175, 210, self.x - play_state.knight.x + 400,
                                            self.y, 105, 105)
        else:
            self.ground_monster_image.clip_composite_draw(int(self.frame) * 175, 749, 175, 210,0,'h', self.x - play_state.knight.x + 400,
                                            self.y, 105, 105)


class ATTACK:
    @staticmethod
    def enter(self):
        global FRAMES_PER_ACTION
        self.frame = 0
        pass

    @staticmethod
    def exit(self):
        self.frame = 0
        pass
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 4
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        print(self.frame)
        if int(self.frame) == 0:
            self.cur_state = RUN
            self.timer = 1000
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * 0.5
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(int(self.frame) * 186, 615, 186, 150, self.x - play_state.knight.x + 400,
                                            self.y, 120, 90)
        else:
            self.ground_monster_image.clip_composite_draw(int(self.frame) * 186, 615, 186, 150, 0,'h',self.x - play_state.knight.x + 400,
                                            self.y, 120, 90)
        pass

class DIE:
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
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.ground_monster_image.clip_draw(int(self.frame) * 199, 131, 199, 143, self.x - play_state.knight.x + 400,
                                            self.y, 120, 90)
        else:
            self.ground_monster_image.clip_composite_draw(int(self.frame) * 199, 131, 199, 143, 0,'h',self.x - play_state.knight.x + 400,
                                            self.y, 120, 90)


class groundmonster:
    def __init__(self):
        self.x, self.y = 900, 120
        self.frame = 0
        self.timer = 0
        self.cur_state = IDLE
        self.dir = -1
        self.life = 5
        self.cur_state.enter(self)
        self.ground_monster_image = load_image('ground_monster1.png')
    def update(self):
        if self.timer >= 0:
            self.timer -= 1
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - play_state.knight.x + 400 - 50, self.y - 50, self.x - play_state.knight.x + 400 + 50, self.y + 50


class geo:
    def __init__(self):
        self.geonum = random.randint(1, 5)
        self.geo_image = load_image('geo_item.png')
        self.x, self.y = random.randint(play_state.GroundMonster.x - 50, play_state.GroundMonster.x + 50), play_state.GroundMonster.y

    def update(self):
        pass

    def draw(self):
        if play_state.GroundMonster.cur_state == play_state.ENEMY.DIE:
            self.geo_image.clip_draw(0,0,58,61,self.x,self.y,40,40)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20