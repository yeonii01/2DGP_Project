import game_framework
import pico2d

import play_state

pico2d.open_canvas(800, 600)
pico2d.hide_cursor()
game_framework.run(play_state)
pico2d.close_canvas()