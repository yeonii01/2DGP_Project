# from Knight import knight
import play_state
from pico2d import *

class map:
    def __init__(self):
        self.x, self.y = 400, 300
        self.cursor_x,self.cursor_y = 0,0
        self.map_ui = load_image('ui_hp.png')
        self.map1_image = load_image('bg_1.png')
        self.map1_floor = load_image('floor.png')
        self.start_image = load_image('start_menu.png')
        self.start_titleimage = load_image('start_title.png')
        self.start_font = load_image('start_font.png')
        self.start_cursor = load_image('cursor.png')
        self.state = ['start', 'map1', 'die']
        self.cur_state = 'start'
        self.font = load_font('Cafe24Danjunghae.TTF', 60)
    def update(self):
        if self.cur_state == 'start':
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEMOTION:
                    self.cursor_x, self.cursor_y = event.x, 600 - 1 - event.y
                if event.type == SDL_MOUSEBUTTONDOWN:
                    if event.x <=573 and event.x >=170:
                        if 600 - 1 - event.y >=53 and 600 - 1 -event.y <=203:
                            self.cur_state = 'map1'

    def draw(self):
        if self.cur_state == 'start':
            self.start_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.start_titleimage.clip_draw(0, 0, 600, 250, 400, 400)
            self.start_font.clip_draw(0, 0, 170, 53, 400, 150)
            self.start_cursor.clip_draw(0,0,37,37,self.cursor_x,self.cursor_y)
        elif self.cur_state == 'map1':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.map_ui.clip_draw(0,0,100,60,60,560)
            for x in range(100):
                self.map1_floor.clip_draw(0, 0, 150, 25, 75 * x - play_state.knight.x, 70)
        elif self.cur_state == 'die':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            play_state.knight.x = 0
            self.font.draw(280, 300, f'(YOU DIE)',(255,255,255))