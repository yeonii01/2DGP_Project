from pico2d import *
import game_framework
import Knight
from Map import map
import Enemy
import game_world

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            knight.handle_event(event)


# 초기화
def enter():
    global knight, Map, GroundMonster
    Map = map()
    knight = Knight.knight()
    GroundMonster = Enemy.groundmonster()
    game_world.add_object(knight, 1)
    game_world.add_object(GroundMonster, 1)
    game_world.add_object(Map, 0)

# 종료
def exit():
    game_world.clear()


timer1 = 0
timer2 = 0
def update():
    global timer1, timer2

    for game_object in game_world.all_objects():
        if Map.cur_state == 'start':
            Map.update()
        else:
            game_object.update()

    if GroundMonster.cur_state != Enemy.DIE:
        if timer1 >= 0:
            timer1 -= 1

        else:
            if math.fabs(knight.x - GroundMonster.x <= 150):
                if knight.cur_state == Knight.ATTACK:
                    GroundMonster.life -= 1
                    GroundMonster.x -= GroundMonster.dir * 150
                    timer1 = 500

        if timer2 >= 0:
            if timer2 >= 1900:
                knight.x = knight.x + GroundMonster.dir * 1
            timer2 -= 1

        else:
            if collide(knight, GroundMonster):
                if knight.cur_state != Knight.ATTACK:
                    if knight. life > 0:
                        knight.life -= 1
                        timer2 = 2000

    if knight.life <= 0:
        Map.cur_state = 'die'
        pass

    if GroundMonster.life <= 0:
        GroundMonster.cur_state = Enemy.DIE

def draw_world():
    for game_object in game_world.all_objects():
        if Map.cur_state == 'start' or Map.cur_state == 'die':
            Map.draw()
        else:
            game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

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
