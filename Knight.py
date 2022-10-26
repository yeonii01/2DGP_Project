from pico2d import *
from Map import map
RD, LD, RU, LU, UD, DD, UU, DU, Z, X, C = range(11)
event_name = ['RD','LD','RU','LU', 'UD', 'DD','UU','DU', 'Z','X','C']

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
    (SDL_KEYDOWN, SDLK_x): X
}

class IDLE:
    @staticmethod
    def enter(self,event):
        # self.dir = 0
        self.frame = 0
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        delay(0.2)
        self.frame = (self.frame+1) % 2

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(self.frame * 80, 304, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 304, 80, 80, 400, self.y)
class UP:
    @staticmethod
    def enter(self,event):
        # self.dir = self.face_dir
        self.frame = 3
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        delay(0.4)
        self.frame = (self.frame + 1) % 3 + 3

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(self.frame * 80, 304, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 304, 80, 80, 400, self.y)
class DOWN:
    @staticmethod
    def enter(self,event):
        # self.dir = self.face_dir
        self.frame = 7
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        delay(0.4)
        self.frame = (self.frame + 1) % 3 + 7

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(self.frame * 80, 623, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 623, 80, 80, 400, self.y)

class RUN:
    @staticmethod
    def enter(self,event):
        self.frame = 0
        self.dir = 0
        if event == RD:
            self.face_dir = 1
            self.dir += 1
        elif event == LD:
            self.face_dir = -1
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self, event):
        # self.face_dir = self.dir
        # print(self.face_dir)
        pass
    @staticmethod
    def do(self):
        delay(0.05)
        self.frame = (self.frame + 1) % 9
        if self.dir == 1:
            self.x += 7
        else:
            self.x -= 7

    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image_r.clip_draw(self.frame * 80, 942, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 942, 80, 80, 400, self.y)
class ATTACK:
    @staticmethod
    def enter(self, event):
        # self.dir = self.face_dir
        self.frame = 0
        pass

    @staticmethod
    def exit(self, event):
        # self.face_dir = self.dir
        pass
    @staticmethod
    def do(self):
        delay(0.05)
        self.frame = (self.frame + 1) % 5
        if self.frame == 0:
            self.frame = 0
            self.cur_state = IDLE

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(self.frame * 80, 623, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 623, 80, 80, 400, self.y)

class JUMP:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.savey = self.y
        self.pre_state = JUMP
    @staticmethod
    def exit(self, event):
        # self.y = self.savey
        self.frame = 0
        # self.jumpcount = 0
        # self.cur_state = IDLE
        # self.dir = self.face_dir
    @staticmethod
    def do(self):
        delay(0.07)
        self.jumpcount += 1
        self.frame = (self.frame + 1) % 12
        if self.frame == 0:
            self.jumpcount = 0
            self.y = self.savey
            self.cur_state = IDLE
        elif self.jumpcount <= 6:
            self.y += 25
        elif self.jumpcount <= 12 and self.jumpcount >= 6:
            self.y -= 25
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(self.frame * 80, 223, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 223, 80, 80, 400, self.y)

class RUNJUMP:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.savey = self.y
        self.pre_state = RUNJUMP
    @staticmethod
    def exit(self, event):
        # self.y = self.savey
        self.frame = 0
        # self.jumpcount = 0
        # self.cur_state = RUN
        # self.face_dir = self.dir
        pass
    @staticmethod
    def do(self):
        delay(0.07)
        self.jumpcount += 1
        self.frame = (self.frame + 1) % 12
        if self.frame == 0:
            self.jumpcount = 0
            self.y = self.savey
            self.cur_state = RUN
            self.face_dir = self.dir
        elif self.jumpcount <= 6:
            self.y += 25
        elif self.jumpcount <= 12 and self.jumpcount >= 6:
            self.y -= 25
        if self.dir == 1:
            self.x += 7
        else:
            self.x -= 7
    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image_r.clip_draw(self.frame * 80, 223, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 223, 80, 80, 400, self.y)

class RUSH:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        # self.dir = self.face_dir
        pass

    @staticmethod
    def exit(self, event):
        # self.face_dir = self.dir
        pass
    @staticmethod
    def do(self):
        delay(0.02)
        self.frame = (self.frame + 1) % 12
        self.dashframe = (self.frame + 1) % 5
        if self.face_dir == 1:
            self.x += 10
        else:
            self.x -= 10
        if self.frame == 0:
            self.frame = 0
            self.cur_state = IDLE
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image_r.clip_draw(self.frame * 80, 223, 80, 80, 400, self.y)
            self.dash_image_right.clip_draw(self.dashframe * 80, 0, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 223, 80, 80, 400, self.y)
            self.dash_image_left.clip_draw(self.dashframe*80,0,80,80,400,self.y)

class JUMPRUSH:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        # self.dir = self.face_dir
        pass

    @staticmethod
    def exit(self, event):
        self.dir = self.face_dir
        pass
    @staticmethod
    def do(self):
        delay(0.02)
        self.frame = (self.frame + 1) % 12
        self.dashframe = (self.frame + 1) % 5
        if self.face_dir == 1:
            self.x += 10
        else:
            self.x -= 10
        if self.frame == 0:
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
            self.image_r.clip_draw(self.frame * 80, 223, 80, 80, 400, self.y)
            self.dash_image_right.clip_draw(self.dashframe * 80, 0, 80, 80, 400, self.y)
        else:
            self.image_l.clip_draw(942 - self.frame * 80, 223, 80, 80, 400, self.y)
            self.dash_image_left.clip_draw(self.dashframe*80,0,80,80,400,self.y)



next_state = {
    IDLE:   {RU: IDLE,  LU: IDLE,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK },
    UP:     {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:IDLE, UU: IDLE,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK },
    DOWN:   {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:UP, UU: UP, DU: IDLE, DD: IDLE, C: RUSH, Z: JUMP, X:ATTACK  },
    RUSH:   {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP, X:ATTACK },
    JUMP:   {RU: RUNJUMP,  LU: RUNJUMP,  RD: RUNJUMP, UD: RUNJUMP, UU: IDLE, DU: IDLE, DD:IDLE, C:JUMPRUSH, Z:IDLE, X:IDLE},
    RUNJUMP: {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD: IDLE, UU: IDLE, DU:IDLE, DD:IDLE, C:JUMPRUSH, Z:IDLE, X:IDLE},
    JUMPRUSH: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UD: UP, UU: UP, DU: DOWN, DD: DOWN, C: RUSH, Z: JUMP, X: ATTACK},
    RUN:    {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE,UD: IDLE, UU: IDLE, DU: IDLE, DD: IDLE, X: ATTACK, Z: RUNJUMP, C: RUSH},
    ATTACK: {RU: RUN,  LU: RUN,  RD: RUN, LD: RUN, UD:UP, UU: UP,DU:DOWN, DD:DOWN, C:RUSH, Z:JUMP,X:ATTACK }
}
class knight:
    def __init__(self):
        self.x, self.y = 400, 110
        self.frame = 0
        self.dashframe = 0
        self.jumpcount = 0
        self.dir, self.face_dir = 0, 1
        self.savey = 0

        self.hp_num = 5

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.pre_state = IDLE

        self.image_r = load_image('knight_sprite.png')
        self.image_l = load_image('knight_sprite_left.png')
        self.dash_image_left = load_image('dash_left.png')
        self.dash_image_right = load_image('dash_right.png')
        self.hp_image = load_image('hp.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            pre_state= event
            if self.frame !=0 and (self.cur_state == JUMP or self.cur_state == JUMPRUSH or self.cur_state == RUNJUMP or self.cur_state == RUSH):
                self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if self.cur_state != JUMPRUSH:
                self.add_event(key_event)