from pico2d import *
class Knight:
    def __init__(self):
        self.x, self.y = 400, 110
        self.frame = 0
        self.dashframe = 0
        self.jumpcount = 0
        self.dir = True
        self.savey = 0
        self.state = ['idle', 'jump', 'run', 'attack', 'rush', 'up', 'down', 'jumpdash']
        self.pre_state = 'idle'
        self.move = False
        self.hp_num = 5
        self.image_r = load_image('knight_sprite.png')
        self.image_l = load_image('knight_sprite_left.png')
        self.dash_image_left = load_image('dash_left.png')
        self.dash_image_right = load_image('dash_right.png')
        self.hp_image = load_image('hp.png')
    def update(self):
        if self.state == 'idle':
            self.frame = (self.frame+1) % 2
        elif self.state == 'rush'or self.state == 'jumpdash':
            self.frame = (self.frame + 1) % 12
            self.dashframe = (self.frame + 1) % 5
            if self.dir == True:
                self.x += 10
            else:
                self.x -= 10
            if self.frame == 0:
                self.frame = 0
                if self.pre_state == 'jump':
                    self.state = 'jump'
                    self.pre_state = 'idle'
                    if self.jumpcount < 6:
                        self.jumpcount = 12 - self.jumpcount
                        self.frame = self.jumpcount
                    else:
                        self.frame = self.jumpcount
                else:
                    self.state = 'idle'
        elif self.state == 'attack':
            self.frame = (self.frame + 1) % 5
            if self.frame == 0:
                self.frame = 0
                self.state = 'idle'
        elif self.state == 'jump':
            self.jumpcount += 1
            self.frame = (self.frame + 1) % 12
            if self.frame == 0:
                self.frame = 0
                self.jumpcount = 0
                self.y = self.savey
                if self.move == False:
                    self.state = 'idle'
                else:
                    self.state = 'run'
            elif self.jumpcount <= 6:
                self.y += 25
            elif self.jumpcount <= 12 and self.jumpcount >= 6:
                self.y -= 25
            if self.move == True:
                if self.dir == True:
                    self.x += 5
                else:
                    self.x -= 5
        elif self.state == 'run':
            self.frame = (self.frame + 1) % 9
            if self.dir == True:
                self.x += 7
            else:
                self.x -= 7
        elif self.state == 'up':
            self.frame = (self.frame + 1) % 3 + 3
        elif self.state == 'down':
            self.frame = (self.frame + 1) % 3 + 7

    def draw(self):
        if map.state != 'start':
            if self.dir == True:
                if self.state == 'rush' or self.state == 'jump'or self.state == 'jumpdash':
                    self.image_r.clip_draw(self.frame*80, 223, 80, 80, 400, self.y)
                    if self.state == 'rush'or self.state == 'jumpdash':
                        self.dash_image_right.clip_draw(self.dashframe*80,0,80,80,400,self.y)
                elif self.state == 'run':
                    self.image_r.clip_draw(self.frame * 80, 942, 80, 80, 400, self.y)
                elif self.state == 'attack':
                    self.image_r.clip_draw(self.frame * 80, 623, 80, 80, 400, self.y)
                elif self.state == 'idle':
                    self.image_r.clip_draw(self.frame * 80, 304, 80, 80, 400, self.y)
                elif self.state == 'up':
                    self.image_r.clip_draw(self.frame * 80, 304, 80, 80, 400, self.y)
                elif self.state == 'down':
                    self.image_r.clip_draw(self.frame * 80, 623, 80, 80, 400, self.y)
            elif self.dir == False:
                if self.state == 'rush' or self.state == 'jump'or self.state == 'jumpdash':
                    self.image_l.clip_draw(942 - self.frame * 80, 223, 80, 80, 400, self.y)
                    if self.state == 'rush'or self.state == 'jumpdash':
                        self.dash_image_left.clip_draw(self.dashframe*80,0,80,80,400,self.y)
                elif self.state == 'run':
                    self.image_l.clip_draw(942 - self.frame * 80, 942, 80, 80, 400, self.y)
                elif self.state == 'attack':
                    self.image_l.clip_draw(942 - self.frame * 80, 623, 80, 80, 400, self.y)
                elif self.state == 'idle':
                    self.image_l.clip_draw(942 - self.frame * 80, 304, 80, 80, 400, self.y)
                elif self.state == 'up':
                    self.image_l.clip_draw(942 - self.frame * 80, 304, 80, 80, 400, self.y)
                elif self.state == 'down':
                    self.image_l.clip_draw(942 - self.frame * 80, 623, 80, 80, 400, self.y)
            for x in range(0, knight.hp_num):
                self.hp_image.clip_draw(0, 0, 40, 50, 100 + x * 40, 550)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_z:
                knight.savey = knight.y
                knight.state = 'jump'
                knight.frame = 0
            elif event.key == SDLK_UP:
                if knight.state != 'jump':
                    knight.state = 'up'
            elif event.key == SDLK_DOWN:
                if knight.state != 'jump':
                    knight.state = 'down'
            elif event.key == SDLK_x:
                knight.state = 'attack'
            elif event.key == SDLK_c:
                if knight.state == 'jump':
                    knight.pre_state = 'jump'
                    knight.state = 'jumpdash'
                knight.state = 'rush'
            if knight.state != 'jump':
                if event.key == SDLK_LEFT:
                    knight.state = 'run'
                    knight.dir = False
                    knight.move = True
                elif event.key == SDLK_RIGHT:
                    knight.state = 'run'
                    knight.dir = True
                    knight.move = True
                if event.key == SDLK_c:
                    knight.state = 'rush'
            elif knight.state == 'jump':
                if event.key == SDLK_LEFT:
                    knight.dir = False
                    knight.move = True
                elif event.key == SDLK_RIGHT:
                    knight.dir = True
                    knight.move = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_UP or event.key == SDLK_DOWN:
                if knight.state != 'jump' and knight.state != 'attack':
                    knight.state = 'idle'
                    knight.move = False
        elif event.type == SDL_MOUSEMOTION:
            if map.state == 'start':
                map.cursor_x, map.cursor_y = event.x, 600 -1 - event.y
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                if map.state == 'start':
                    if event.x >=315 and event.x <=485 and 600 -1 - event.y >= 124 and 600 -1 - event.y <=176:
                        map.state = 'map1'


open_canvas()

knight = Knight()

running = True
knight.dir = True
knight.state = 'idle'
map.state = 'start'
hide_cursor()

while running:
    handle_events()

    knight.update()
    clear_canvas()
    map.draw()
    knight.draw()
    update_canvas()

    if map.state != 'start':
        if knight.state == 'idle':
            delay(0.2)
        elif knight.state == 'rush':
            delay(0.02)
        elif knight.state == 'run' or knight.state == 'attack':
            delay(0.05)
        elif knight.state == 'up' or knight.state == 'down':
            delay(0.4)
        elif knight.state == 'jump':
            delay(0.07)

close_canvas()