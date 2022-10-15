from pico2d import *
class Knight:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = True
        self.savey = 0
        self.state = ['idle', 'jump', 'run', 'attack', 'rush', 'up', 'down']
        self.image_r = load_image('knight_sprite.png')
        self.image_l = load_image('knight_sprite_left.png')
    def update(self):
        if self.state == 'idle':
            self.frame = (self.frame+1) % 2
        elif self.state == 'rush':
            self.frame = (self.frame + 1) % 12
            if self.dir == True:
                self.x += 10
            else:
                self.x -= 10
            if self.frame == 0:
                self.frame = 0
                self.state = 'idle'
        elif self.state == 'attack':
            self.frame = (self.frame + 1) % 5
            if self.frame == 0:
                self.frame = 0
                self.state = 'idle'
        elif self.state == 'run':
            self.frame = (self.frame + 1) % 9
            if self.dir == True:
                self.x += 5
            else:
                self.x -= 5
        elif self.state == 'up':
            self.frame = (self.frame + 1) % 3 + 3
        elif self.state == 'down':
            self.frame = (self.frame + 1) % 3 + 7
        elif self.state == 'jump':
            self.frame = (self.frame + 1) % 12
            if self.frame == 0:
                self.frame = 0
                self.y = self.savey
                self.state = 'idle'
            elif self.frame <= 6:
                self.y += 25
            elif self.frame <= 12 and self.frame >= 6:
                self.y -= 25
    def draw(self):
        if self.dir == True:
            if self.state == 'rush' or self.state == 'jump':
                self.image_r.clip_draw(self.frame*80, 223, 80, 80, self.x, self.y)
            elif self.state == 'run':
                self.image_r.clip_draw(self.frame * 80, 942, 80, 80, self.x, self.y)
            elif self.state == 'attack':
                self.image_r.clip_draw(self.frame * 80, 623, 80, 80, self.x, self.y)
            elif self.state == 'idle':
                self.image_r.clip_draw(self.frame * 80, 304, 80, 80, self.x, self.y)
            elif self.state == 'up':
                self.image_r.clip_draw(self.frame * 80, 304, 80, 80, self.x, self.y)
            elif self.state == 'down':
                self.image_r.clip_draw(self.frame * 80, 623, 80, 80, self.x, self.y)
        elif self.dir == False:
            if self.state == 'rush' or self.state == 'jump':
                self.image_l.clip_draw(942 - self.frame * 80, 223, 80, 80, self.x, self.y)
            elif self.state == 'run':
                self.image_l.clip_draw(942 - self.frame * 80, 942, 80, 80, self.x, self.y)
            elif self.state == 'attack':
                self.image_l.clip_draw(942 - self.frame * 80, 623, 80, 80, self.x, self.y)
            elif self.state == 'idle':
                self.image_l.clip_draw(942 - self.frame * 80, 304, 80, 80, self.x, self.y)
            elif self.state == 'up':
                self.image_l.clip_draw(942 - self.frame * 80, 304, 80, 80, self.x, self.y)
            elif self.state == 'down':
                self.image_l.clip_draw(942 - self.frame * 80, 623, 80, 80, self.x, self.y)


class Map:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('bg_1.png')
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                knight.state = 'run'
                knight.dir = False
            elif event.key == SDLK_RIGHT:
                knight.state = 'run'
                knight.dir = True
            elif event.key == SDLK_UP:
                knight.state = 'up'
            elif event.key == SDLK_DOWN:
                knight.state = 'down'
            elif event.key == SDLK_x:
                knight.state = 'attack'
            elif event.key == SDLK_z:
                knight.savey = knight.y
                knight.state = 'jump'
            elif event.key == SDLK_c:
                knight.state = 'rush'
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_UP or event.key == SDLK_DOWN:
                knight.state = 'idle'


open_canvas()

knight = Knight()
map = Map()
running = True
knight.dir = True
knight.state = 'idle'

while running:
    handle_events()

    knight.update()
    clear_canvas()
    map.draw()
    knight.draw()
    update_canvas()

    if knight.state == 'idle':
        delay(0.2)
    elif knight.state == 'rush':
        delay(0.02)
    elif knight.state == 'run' or knight.state == 'attack':
        delay(0.05)
    elif knight.state == 'up' or knight.state == 'down':
        delay(0.4)
    elif knight.state == 'jump':
        delay(0.075)

close_canvas()