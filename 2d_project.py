from pico2d import *

class Knight:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.frame_count = 0
        self.dir = True
        self.state = ['idle', 'jump', 'run', 'attack', 'rush']
        self.image_r = load_image('knight_sprite.png')
        self.image_l = load_image('knight_sprite_left.png')

    def update(self):
        if self.state == 'idle':
            self.frame = (self.frame+1) % 7
        elif self.state == 'rush':
            knight.frame_count += 1
            if self.frame_count <= 12:
                self.frame = (self.frame + 1) %12
                self.x += 10
            else:
                self.frame_count = 0
                self.frame = 0
                self.state = 'idle'
    def draw(self):
        if self.state == 'rush' and self.dir == True:
            self.image_r.clip_draw(self.frame*80, 223, 80, 80, self.x, self.y)
        if self.state == 'attack' and self.dir == True:
            self.image_r.clip_draw(self.frame * 80, 223, 80, 80, self.x, self.y)
        elif self.state == 'idle' and self.dir == True:
            self.image_r.clip_draw(self.frame*80, 303, 80, 80, self.x, self.y)
        elif self.state == 'idle' and self.dir == False:
            self.image_l.clip_draw(800 - self.frame * 80, 303, 80, 80, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        if event.key == SDLK_LEFT:
            knight.state = 'run'
            knight.dir = False
            knight.x -= 5
        elif event.key == SDLK_RIGHT:
            knight.state = 'run'
            knight.dir = True
        elif event.key == SDLK_x:
            knight.state = 'attack'
            knight.frame = 0
        elif event.key == SDLK_c:
            knight.state = 'rush'
            knight.frame = 0
        else:
            knight.state = 'idle'
            knight.frame = 0


open_canvas()

knight = Knight()
running = True
knight.dir = True
knight.state = 'idle'

while running:
    handle_events()

    knight.update()
    clear_canvas()
    knight.draw()
    update_canvas()

    if knight.state == 'idle':
        delay(0.2)
    elif knight.state == 'rush':
        delay(0.03)

close_canvas()
