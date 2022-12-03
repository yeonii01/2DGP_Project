# from Knight import knight
import play_state
from pico2d import *

class map:
    def __init__(self):
        self.x, self.y = 400, 300
        self.cursor_x,self.cursor_y = 0,0
        self.map_ui = load_image('ui_hp.png')
        self.map1_image = load_image('bg_1.png')
        self.start_image = load_image('start_menu.png')
        self.start_titleimage = load_image('start_title.png')
        self.start_font = load_image('start_font.png')
        self.start_cursor = load_image('cursor.png')
        self.state = ['start', 'map1', 'die', 'pause', 'finish']
        self.cur_state = 'start'
        self.font = load_font('Cafe24Danjunghae.TTF', 70)
        self.smallfont = load_font('Cafe24Danjunghae.TTF', 40)
        self.geo_image = load_image('geo_item.png')
        self.start_bench = load_image('spider_town_bench.png')
        self.bell = load_image('chain_bell.png')
        self.success = load_image('Finishimage.png')
    def update(self):
        pass

    def draw(self):
        if self.cur_state == 'start':
            self.start_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.start_titleimage.clip_draw(0, 0, 600, 250, 400, 400)
            self.start_font.clip_draw(0, 0, 170, 53, 400, 150)
            self.start_cursor.clip_draw(0,0,37,37,self.cursor_x,self.cursor_y)
        elif self.cur_state == 'map1':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.start_bench.clip_draw(0, 0, 255, 124, 400- play_state.knight.x + 400, 105,210,100)
            self.map_ui.clip_draw(0,0,100,60,60,560)
            self.geo_image.clip_draw(0, 0, 58, 61, 40, 500, 40, 40)
            self.smallfont.draw(80, 495, f'{play_state.knight.itemnum}',(255,255,255))
            self.bell.clip_draw(0,0,52,469, 5450 - play_state.knight.x + 400, 550, 30,220)
        elif self.cur_state == 'die':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.font.draw(280, 400, f'YOU DIE',(255,255,255))
            self.smallfont.draw(320, 200, f'RESTART',(255,255,255))
            # draw_rectangle(320,180,480,220)
            self.smallfont.draw(360, 150, f'QUIT',(255,255,255))
            # draw_rectangle(360,130,450,170)
            self.start_cursor.clip_draw(0,0,37,37,self.cursor_x,self.cursor_y)
        elif self.cur_state == 'pause':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.smallfont.draw(320, 400, f'RESTART', (255, 255, 255))
            # draw_rectangle(320,380,490,420)
            self.smallfont.draw(320, 300, f'RESUME', (255, 255, 255))
            # draw_rectangle(320,280,480,320)
            self.smallfont.draw(360, 200, f'QUIT', (255, 255, 255))
            # draw_rectangle(360,180,450,220)
            self.start_cursor.clip_draw(0,0,37,37,self.cursor_x,self.cursor_y)
        elif self.cur_state == 'finish':
            self.map1_image.clip_draw(0, 0, 800, 600, self.x, self.y)
            self.success.clip_draw(0,0,578,1016,400,250,284,500)
            self.smallfont.draw(300, 550, f'GAME FINISH', (255, 255, 255))
