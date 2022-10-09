from pico2d import *

class Knight:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('knight_sprite.png')
    def update(self):
        self.frame = (self.frame+1) % 12
    def draw(self):
        self.image.clip_draw(self.frame*80, 303, 80, 80, self.x, self.y)

open_canvas()
knight = Knight()
running = True
while running:
    # handle_events()

    knight.update()
    clear_canvas()
    knight.draw()
    update_canvas()

    delay(0.1)

close_canvas()



