from pico2d import *
import game_framework
import Knight
from Map import map
import Enemy
from Enemy import geo
import game_world
import random
from ground import Ground
from obstacle import Obstacle

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
geonum = random.randint(2,5)
tempx,otempx = 0,0

def enter():
    global knight, Map, GroundMonster, Geo, Geos, geonum, blocks1, blocks2, blocks3, tempx, obstacle, obstacles, otempx
    blocks1 = [Ground() for i in range(6)]
    blocks2 = [Ground() for i in range(6)]
    blocks3 = Ground()
    obstacles = [Obstacle()for i in range(3)]
    obstacle = Obstacle()
    Map = map()
    knight = Knight.knight()
    GroundMonster = Enemy.groundmonster()
    Geos = [geo() for i in range(geonum)]
    game_world.add_object(GroundMonster, 1)
    game_world.add_object(knight, 1)
    game_world.add_object(Map, 0)
    for i in blocks1:
        game_world.add_object(i, 0)
        i.x = 140 * tempx
        tempx += 1

    tempx += 1

    for i in blocks2:
        game_world.add_object(i, 0)
        i.x = 140 * tempx
        tempx += 1

    game_world.add_object(blocks3, 0)
    blocks3.x = 1970

    game_world.add_object(obstacle, 0)
    obstacle.x = 1820 + 150 * otempx

    otempx += 2

    for o in obstacles:
        game_world.add_object(o, 0)
        o.x = 1820 + 150 * otempx
        otempx += 1
# 종료
def exit():
    game_world.clear()

timer1 = 0
timer2 = 0

check = False
def update():
    global timer1, timer2, check

    check = False

    for game_object in game_world.all_objects():
        if Map.cur_state == 'start':
            Map.update()
        else:
            game_object.update()
    # 블록 충돌체크
    for i in blocks1:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    for i in blocks2:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    if collide(knight, blocks3):
        knight.y = i.y + 50
        check = True

    if knight.cur_state != Knight.JUMP and knight.cur_state != Knight.JUMPRUSH and knight.cur_state != Knight.RUNJUMP:
        if check == False:
            knight.y -= 1

    # 몬스터 타이머 체크 충돌체크
    if GroundMonster.cur_state != Enemy.DIE:
        if timer1 >= 0:
            timer1 -= 1

        else:
            if math.fabs(GroundMonster.x - knight.x) <= 120:
                if knight.cur_state == Knight.ATTACK:
                    GroundMonster.life -= 1
                    print(GroundMonster.life)
                    GroundMonster.x -= GroundMonster.dir * 75
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

    if knight.life <= 0 or knight.y <= 0:
        Map.cur_state = 'die'

    if GroundMonster.life == 0:
        print(GroundMonster.life)
        GroundMonster.cur_state = Enemy.DIE
        # 아이템 소환
        for Geo in Geos:
            game_world.add_object(Geo, 1)
            Geo.x, Geo.y = random.randint(int(GroundMonster.x - 50),
                                        int(GroundMonster.x + 50)), GroundMonster.y - 20
        GroundMonster.life = -1

    # 아이템 획득
    if GroundMonster.life <= 0:
        for Geo in Geos.copy():
            if collide(knight, Geo):
                knight.itemnum += 1
                Geos.remove(Geo)
                game_world.remove_object(Geo)


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
