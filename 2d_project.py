from pico2d import *

class Knight:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('knight_sprite.png')
    def update(self):
        self.frame = (self.frame+1) % 7
    def draw(self):
        self.image.clip_draw(self.frame*80, 303, 80, 80, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

knight = Knight()
running = True
while running:
    # handle_events()

    knight.update()
    clear_canvas()
    knight.draw()
    update_canvas()

    delay(0.2)

close_canvas()
