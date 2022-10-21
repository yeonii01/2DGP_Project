import Knight
from pico2d import *

class Map:
    def __init__(self):
        self.x, self.y = 400, 300
        self.cursor_x,self.cursor_y = 0,0
        self.map_ui = load_image('ui_hp_left.png')
        self.map1_image = load_image('bg_1.png')
        self.map1_floor = load_image('floor.png')
        self.start_image = load_image('start_menu.png')
        self.start_titleimage = load_image('start_title.png')
        self.start_font = load_image('start_font.png')
        self.start_cursor = load_image('cursor.png')
        self.state = ['start', 'map1']
    def draw(self):
        if self.state == 'start':
            self.start_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.start_titleimage.clip_draw(0, 0, 600, 250, 400, 400)
            self.start_font.clip_draw(0, 0, 170, 53, 400, 150)
            self.start_cursor.clip_draw(0,0,37,37,self.cursor_x,self.cursor_y)
        elif self.state == 'map1':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.map_ui.clip_draw(0,0,100,60,60,560)
            for x in range(100):
                self.map1_floor.clip_draw(0, 0, 150, 25, 75 * x - Knight.knight.x, 70)