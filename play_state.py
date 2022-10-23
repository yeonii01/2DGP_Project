from pico2d import *
import game_framework
from Knight import knight
from Map import map
import game_world

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            Knight.handle_event(event)


# 초기화
def enter():
    global Knight, Map
    Map = map()
    Knight = knight()
    game_world.add_object(Knight, 1)
    game_world.add_object(Map, 0)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        if Map.cur_state == 'start':
            Map.update()
        else:
            game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        if Map.cur_state == 'start':
            Map.draw()
        else:
            game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass



def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
