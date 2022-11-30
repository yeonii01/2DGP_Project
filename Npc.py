from pico2d import *
import play_state
import math
import game_framework

class NPC:
    def __init__(self):
        self.x, self.y = 3500, 130
        self.talk = False
        self.dialogue = 0
        self.npc_image = load_image('npc.png')
        self.font = load_font('Cafe24Danjunghae.TTF', 20)
        self.talkeffect = load_image('lifeup_effect.png')
    def update(self):
        if math.fabs(self.x - play_state.knight.x) <= 200:
            self.talk = True
            pass

    def draw(self):
        self.npc_image.clip_draw(0,0,187,219,self.x - play_state.knight.x + 400, self.y,95,110)
        if self.talk == True:
            if self.dialogue == 1:
                self.font.draw(self.x- play_state.knight.x + 400, self. y + 75, f'FIND THE KEY',(255,255,255))
                self.talkeffect.clip_draw(0, 0, 91, 83, self.x - play_state.knight.x + 450, self.y + 85, 500, 100)
            elif self.dialogue == 2:
                self.font.draw(self.x- play_state.knight.x + 400, self. y + 75, f'THE HINT IS BELL',(255,255,255))
                self.talkeffect.clip_draw(0,0,91,83,self.x- play_state.knight.x + 450, self. y + 85,500,100)

    def get_bb(self):
        pass
        # return self.x - play_state.knight.x + 400 - 50, self.y - 50, self.x - play_state.knight.x + 400 + 50, self.y + 50