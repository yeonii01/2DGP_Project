from pico2d import *
from Map import map
import game_framework
import play_state

RD, LD, RU, LU, UD, DD, UU, DU, Z, X, C, A = range(12)
event_name = ['RD','LD','RU','LU', 'UD', 'DD','UU','DU', 'Z','X','C', 'A']

key_event_table = {
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN,SDLK_c): C,
    (SDL_KEYDOWN, SDLK_z): Z,
    (SDL_KEYDOWN, SDLK_x): X,
    (SDL_KEYDOWN, SDLK_a): A

}

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
    def enter(self,event):
        # self.dir = 0
        self.frame = 0
        self.pre_state = IDLE
        global FRAMES_PER_ACTION
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 2
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 304, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 304, 80, 80, 400, self.y)

class LIFEUP:
    @staticmethod
    def enter(self,event):
        self.pre_state = LIFEUP
        # self.dir = 0
        self.frame = 0
        global FRAMES_PER_ACTION
        self.itemnum -= 5
        self.lifecount = 0
        pass

    @staticmethod
    def exit(self, event):
        self.life += 1
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 6
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%6 + 6
        self.lifecount += 1
        if self.lifecount >= 500:
            self.life += 1
            self.cur_state = IDLE
            self.lifecount = 0
    @staticmethod
    def draw(self):
        self.image_r.clip_draw(int(self.frame) * 80, 544, 80, 80, 400, self.y)
        self.lifeup_image.clip_draw(0,0,91,83,400,self.y,100,100)
        pass

class UP:
    @staticmethod
    def enter(self,event):
        self.pre_state = UP
        # self.dir = self.face_dir
        self.frame = 0
        global FRAMES_PER_ACTION

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 3
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3 + 3

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 304, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 304, 80, 80, 400, self.y)
class DOWN:
    @staticmethod
    def enter(self,event):
        self.pre_state = DOWN
        # self.dir = self.face_dir
        self.frame = 0
        global FRAMES_PER_ACTION
        FRAMES_PER_ACTION = 3
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3 + 7


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 623, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 623, 80, 80, 400, self.y)

class RUN:
    @staticmethod
    def enter(self,event):
        global FRAMES_PER_ACTION
        print(self.pre_state)

        self.frame = 0
        if self.pre_state != RUNJUMP:
            self.dir = 0
        else:
            print(self.dir)
        if event == RD:
            self.face_dir = 1
            self.dir += 1
        elif event == LD:
            self.face_dir = -1
            self.dir -= 1
        elif event == RU:
            self.face_dir = 1
            self.dir -= 1
        elif event == LU:
            self.face_dir = -1
            self.dir += 1
        # print(self.dir)
        self.pre_state = RUN
    @staticmethod
    def exit(self, event):
        self.face_dir = self.dir
        # print(self.face_dir)
        pass
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 9
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * 0.3

    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 942, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 942, 80, 80, 400, self.y)
class ATTACK:
    @staticmethod
    def enter(self, event):
        global FRAMES_PER_ACTION
        # self.dir = self.face_dir
        self.frame = 0
        self.pre_state = ATTACK
        pass

    @staticmethod
    def exit(self, event):
        # self.face_dir = self.dir
        pass
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 5
        self.frame = self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if int(self.frame) >= 5:
            self.frame = 0
            self.cur_state = IDLE

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 623, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 623, 80, 80, 400, self.y)

class JUMP:
    @staticmethod
    def enter(self, event):
        global FRAMES_PER_ACTION
        self.frame = 0
        self.savey = self.y
        self.pre_state = JUMP
    @staticmethod
    def exit(self, event):
        self.dir = self.face_dir
        self.frame = 0
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 12
        self.frame = self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.jumpcount = int(self.frame)
        if self.frame >= 12:
            self.jumpcount = 0
            self.y = self.savey
            self.dir = self.face_dir
            self.cur_state = RUN
            self.savey = 0
        if self.jumpcount <= 6:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.jumpcount <= 12 and self.jumpcount >= 6:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 223, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 223, 80, 80, 400, self.y)

class RUNJUMP:
    @staticmethod
    def enter(self, event):
        global FRAMES_PER_ACTION
        self.frame = 0
        self.savey = self.y
        self.pre_state = RUNJUMP
    @staticmethod
    def exit(self, event):
        self.frame = 0
        self.dir = self.face_dir
        pass
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 12
        self.frame = self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.jumpcount = self.frame
        if self.frame >= 12:
            self.pre_state = RUNJUMP
            self.jumpcount = 0
            self.y = self.savey
            self.dir = self.face_dir
            self.cur_state = RUN
        elif self.jumpcount <= 6:
            self.y += RUN_SPEED_PPS * game_framework.frame_time
        elif self.jumpcount <= 12 and self.jumpcount >= 6:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * 0.6

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 223, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 223, 80, 80, 400, self.y)

class RUSH:
    @staticmethod
    def enter(self, event):
        self.pre_state = RUSH
        global FRAMES_PER_ACTION
        self.frame = 0
        pass

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 12
        self.frame = self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.dashframe = (self.frame/2) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * 0.6
        if self.frame >= 12:
            self.frame = 0
            self.cur_state = IDLE
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 223, 80, 80, 400, self.y)
            self.dash_image_right.clip_draw(int(self.dashframe) * 80, 0, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 223, 80, 80, 400, self.y)
            self.dash_image_left.clip_draw(int(self.dashframe)*80,0,80,80,400,self.y)

class JUMPRUSH:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        global FRAMES_PER_ACTION
        # self.dir = self.face_dir
        pass

    @staticmethod
    def exit(self, event):
        # self.dir = self.face_dir
        pass
    @staticmethod
    def do(self):
        FRAMES_PER_ACTION = 12
        self.frame = self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.dashframe = (self.frame/2) % 5
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time * 0.6
        if self.frame >= 12:
            if self.jumpcount < 6:
                self.jumpcount = 12 - self.jumpcount
                self.frame = self.jumpcount
            else:
                self.frame = self.jumpcount
            if self.pre_state == JUMP:
                self.cur_state = JUMP
            elif self.pre_state == RUNJUMP:
                self.cur_state = RUNJUMP
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(int(self.frame) * 80, 223, 80, 80, 400, self.y)
            self.dash_image_right.clip_draw(int(self.dashframe) * 80, 0, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - int(self.frame) * 80, 223, 80, 80, 400, self.y)
            self.dash_image_left.clip_draw(int(self.dashframe)*80,0,80,80,400,self.y)



next_state = {
    IDLE:   {RU: IDLE,  LU: IDLE,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK, A:LIFEUP },
    UP:     {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:IDLE, UU: IDLE,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK, A:LIFEUP },
    DOWN:   {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:UP, UU: UP, DU: IDLE, DD: IDLE, C: RUSH, Z: JUMP, X:ATTACK, A:LIFEUP  },
    RUSH:   {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK, A:LIFEUP },
    JUMP:   {RU: RUNJUMP,  LU: RUNJUMP,  RD: RUNJUMP, UD: RUNJUMP, UU: IDLE, DU: IDLE, DD:IDLE, C:JUMPRUSH, Z:IDLE, X:IDLE, A:LIFEUP},
    RUNJUMP: {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD: IDLE, UU: IDLE, DU:IDLE, DD:IDLE, C:JUMPRUSH, Z:IDLE, X:IDLE, A:LIFEUP},
    JUMPRUSH: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UD: UP, UU: UP, DU: DOWN, DD: DOWN, C: RUSH, Z: JUMP, X: ATTACK, A:LIFEUP},
    RUN:    {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE,UD: IDLE, UU: IDLE, DU: IDLE, DD: IDLE, X: ATTACK, Z: RUNJUMP, C: RUSH, A:LIFEUP},
    ATTACK: {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP,X:ATTACK, A:LIFEUP },
    LIFEUP: {RU: IDLE,  LU: IDLE,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK, A:IDLE }
}
class knight:
    def __init__(self):
        self.x, self.y = 400, 110
        self.frame = 0
        self.dashframe = 0
        self.jumpcount = 0
        self.dir, self.face_dir = 0, 1
        self.savey = 0
        self.itemnum = 0
        self.life = 5
        self.lifecount = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.pre_state = IDLE

        self.image_r = load_image('knight_sprite.png')
        self.image_l = load_image('knight_sprite_left.png')
        self.dash_image_left = load_image('dash_left.png')
        self.dash_image_right = load_image('dash_right.png')
        self.hp_image = load_image('hp.png')
        self.lifeup_image = load_image('lifeup_effect.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.pre_state = event
            if self.frame !=0 and (self.cur_state == JUMP or self.cur_state == JUMPRUSH or self.cur_state == RUNJUMP or self.cur_state == RUSH):
                self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        for i in range(self.life):
            self.hp_image.clip_draw(0, 0, 40, 50, 100 + 50*i, 550)
        # draw_rectangle(*self.get_bb())
    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if self.cur_state == JUMPRUSH or self.cur_state == RUSH or self.cur_state == ATTACK or self.cur_state == LIFEUP:
                pass
            elif self.cur_state == JUMP or self.cur_state == RUNJUMP:
                if event.key == RU or event.key == LU or event.key == LD or event.key == RD or event.key == SDLK_c:
                    self.add_event(key_event)
            else:
                if key_event == A:
                    if self.itemnum>=5:
                        self.add_event(key_event)
                else:
                    self.add_event(key_event)

    def get_bb(self):
        return 370, self.y - 40, 430, self.y + 40