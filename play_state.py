from pico2d import *
import game_framework
import Knight
from Map import map
import Enemy
from Enemy import geo
import game_world
import random
from ground import Ground
from ground import FGround
from ground import SecondGround
from obstacle import Obstacle
from Npc import NPC
from Npc import NPC2
from ground import Elevator
from boss import KEY
from boss import BOSS
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            knight.handle_event(event)
        if Map.cur_state == 'start' or Map.cur_state == 'die' or Map.cur_state == 'pause':
            if event.type == SDL_MOUSEMOTION:
                Map.cursor_x, Map.cursor_y = event.x, 600 - 1 - event.y
            if Map.cur_state == 'start':
                if event.type == SDL_MOUSEBUTTONDOWN:
                    if event.x <= 573 and event.x >= 170:
                        if 600 - 1 - event.y >= 53 and 600 - 1 - event.y <= 203:
                            Map.cur_state = 'map1'

            elif Map.cur_state == 'die':
                if event.type == SDL_MOUSEBUTTONDOWN:
                    if event.x <= 450 and event.x >= 360:
                        if 600 - 1 - event.y >= 130 and 600 - 1 - event.y <= 170:
                            game_framework.quit()
                    if event.x <= 480 and event.x >= 320:
                        if 600 - 1 - event.y >= 180 and 600 - 1 - event.y <= 220:
                            knight.__init__()
                            GroundMonster.__init__()
                            Map.cur_state = 'map1'
            elif Map.cur_state == 'pause':
                if event.type == SDL_MOUSEBUTTONDOWN:
                    if event.x <= 450 and event.x >= 360:
                        if 600 - 1 - event.y >= 180 and 600 - 1 - event.y <= 220:
                            game_framework.quit()
                    if event.x <= 480 and event.x >= 320:
                        if 600 - 1 - event.y >= 280 and 600 - 1 - event.y <= 320:
                            Map.cur_state = 'map1'
                    if event.x <= 490 and event.x >= 320:
                        if 600 - 1 - event.y >= 380 and 600 - 1 - event.y <= 420:
                            knight.__init__()
                            GroundMonster.__init__()
                            Map.cur_state = 'map1'

        if Map.cur_state == 'map1':
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    Map.cur_state = 'pause'
                if npc.talk == True:
                    if event.key == SDLK_SPACE:
                        npc.dialogue += 1
                        if npc.dialogue == 3:
                            npc.talk = False
                            npc.dialogue = 0
                if npc2.talk == True:
                    if event.key == SDLK_SPACE:
                        npc2.dialogue += 1
                        if npc2.dialogue == 2:
                            if key.keyget == False:
                                npc2.talk = False
                                npc2.dialogue = 0
                        elif npc2.dialogue == 3:
                            npc2.talk = False
                            npc2.dialogue = 0


# 초기화
geonum = random.randint(2,5)
geonum2 = random.randint(2,5)
geonum3 = random.randint(2,5)
tempx,otempx = 0,0

def enter():
    global knight, Map, GroundMonster, GroundMonster2, Geos, Geos2, Geos3, geonum, geonum2, geonum3, blocks1, blocks2, blocks3, blocks4, blocks5, tempx, obstacle, obstacles, otempx, npc, elev
    global secblocks1, secblocks2, secblocks3, twelev, twelev2, twblockdown, twblockup, key, npc2, bosselev, GroundMonster3,boss
    blocks1 = [Ground() for i in range(6)]
    blocks2 = [Ground() for i in range(6)]
    blocks3 = Ground()
    blocks4 = [FGround() for i in range(3)]
    blocks5 = [Ground() for i in range(11)]
    secblocks1 = [SecondGround() for i in range(6)]
    twblockdown = [SecondGround() for i in range(6)]
    twblockup = [SecondGround() for i in range(6)]
    secblocks2 = [SecondGround() for i in range(6)]
    secblocks3 = [SecondGround() for i in range(8)]
    obstacles = [Obstacle()for i in range(3)]
    obstacle = Obstacle()
    Map = map()
    knight = Knight.knight()
    GroundMonster = Enemy.groundmonster()
    GroundMonster2 = Enemy.groundmonster()
    GroundMonster3 = Enemy.groundmonster()
    boss = BOSS()
    npc = NPC()
    npc2 = NPC2()
    elev = Elevator()
    twelev = Elevator()
    twelev2 = Elevator()
    bosselev = Elevator()
    key = KEY()
    GroundMonster2.type = 2
    GroundMonster2.x = 3000
    GroundMonster3.x = 5000
    Geos = [geo() for i in range(geonum)]
    Geos2 = [geo() for i in range(geonum2)]
    Geos3 = [geo() for i in range(geonum3)]
    game_world.add_object(GroundMonster, 1)
    game_world.add_object(GroundMonster2, 1)
    game_world.add_object(GroundMonster3, 1)
    game_world.add_object(boss, 1)
    game_world.add_object(knight, 1)
    game_world.add_object(Map, 0)
    game_world.add_object(npc, 0)
    game_world.add_object(elev, 1)
    game_world.add_object(twelev, 1)
    game_world.add_object(twelev2, 1)
    game_world.add_object(key, 1)
    game_world.add_object(npc2, 0)
    game_world.add_object(bosselev, 1)

    # 블록 그리기
    for i in blocks1:
        game_world.add_object(i, 0)
        i.x = 140 * tempx
        tempx += 1

    tempx += 1

    for i in blocks2:
        game_world.add_object(i, 0)
        i.x = 140 * tempx
        tempx += 1

    tempx += 1
    game_world.add_object(blocks3, 0)
    blocks3.x = 140 * tempx

    # 장애물 시작
    game_world.add_object(obstacle, 0)
    obstacle.x = 1820 + 150 * otempx

    otempx += 2

    for i in blocks4:
        game_world.add_object(i, 0)
        i.x = 20 + 150 * tempx
        tempx += 1

    for o in obstacles:
        game_world.add_object(o, 0)
        o.x = 1820 + 150 * otempx
        otempx += 1

    for i in blocks5:
        game_world.add_object(i, 0)
        i.x = 20 + 150 * tempx
        tempx += 1

    knight.x = 3500 #확인용
    twelev.x = 5300
    # twblockup.y += 200

    twcount = 0
    for i in twblockup:
        game_world.add_object(i, 0)
        i.x = 5480 + 150 * twcount
        i.y += 300
        twcount += 1

    twcount = 0
    for i in twblockdown:
        game_world.add_object(i, 0)
        i.x = 5480 + 150 * twcount
        twcount += 1

    twelev2.x = 6400

    for i in secblocks2:
        game_world.add_object(i, 0)
        i.x = 5680 + 150 * twcount
        twcount += 1

    bosselev.x = 7510
    bosselev.savex = 7510
    twcount = 0
    for i in secblocks3:
        game_world.add_object(i, 0)
        i.x = 8110 + 150 * twcount
        twcount += 1

# 종료
def exit():
    game_world.clear()

timer1 = 0
timer2 = 0

check = False
def update():
    global timer1, timer2, check, tempx

    check = False

    for game_object in game_world.all_objects():
        if Map.cur_state == 'start' or Map.cur_state == 'die':
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
        knight.y = blocks3.y + 50
        check = True

    for i in blocks4:
        if collide(knight, i):
            knight.y = i.y + 60
            check = True

    for i in blocks5:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    for i in secblocks1:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    for i in twblockup:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    for i in twblockdown:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    for i in secblocks2:
        if collide(knight, i):
            knight.y = i.y + 50
            check = True

    for i in secblocks3:
        if collide(knight, i):
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

    if GroundMonster2.cur_state != Enemy.DIE:
        if timer1 >= 0:
            timer1 -= 1
        else:
            if math.fabs(GroundMonster2.x - knight.x) <= 120:
                if knight.cur_state == Knight.ATTACK:
                    GroundMonster2.life -= 1
                    GroundMonster2.x -= GroundMonster2.dir * 75
                    timer1 = 500

        if timer2 >= 0:
            if timer2 >= 1900:
                knight.x = knight.x + GroundMonster2.dir * 1
            timer2 -= 1
        else:
            if collide(knight, GroundMonster2):
                if knight.cur_state != Knight.ATTACK:
                    if knight. life > 0:
                        knight.life -= 1
                        timer2 = 2000

    if GroundMonster3.cur_state != Enemy.DIE:
        if timer1 >= 0:
            timer1 -= 1

        else:
            if math.fabs(GroundMonster3.x - knight.x) <= 120:
                if knight.cur_state == Knight.ATTACK:
                    GroundMonster3.life -= 1
                    GroundMonster3.x -= GroundMonster3.dir * 75
                    timer1 = 500

        if timer2 >= 0:
            if timer2 >= 1900:
                knight.x = knight.x + GroundMonster3.dir * 1
            timer2 -= 1

        else:
            if collide(knight, GroundMonster3):
                if knight.cur_state != Knight.ATTACK:
                    if knight. life > 0:
                        knight.life -= 1
                        timer2 = 2000

    if GroundMonster.life == 0:
        GroundMonster.cur_state = Enemy.DIE
        # 아이템 소환
        for Geo in Geos:
            game_world.add_object(Geo, 1)
            Geo.x, Geo.y = random.randint(int(GroundMonster.x - 50),
                                        int(GroundMonster.x + 50)), GroundMonster.y - 20
        GroundMonster.life = -1

    if GroundMonster2.life == 0:
        GroundMonster2.cur_state = Enemy.DIE
        # 아이템 소환
        for Geo in Geos2:
            game_world.add_object(Geo, 1)
            Geo.x, Geo.y = random.randint(int(GroundMonster2.x - 50),
                                        int(GroundMonster2.x + 50)), GroundMonster2.y - 20
        GroundMonster2.life = -1

    if GroundMonster3.life == 0:
        GroundMonster3.cur_state = Enemy.DIE
        # 아이템 소환
        for Geo in Geos3:
            game_world.add_object(Geo, 1)
            Geo.x, Geo.y = random.randint(int(GroundMonster3.x - 50),
                                          int(GroundMonster3.x + 50)), GroundMonster3.y - 20
        GroundMonster3.life = -1
    # 아이템 획득
    if GroundMonster.life <= 0:
        for Geo in Geos.copy():
            if collide(knight, Geo):
                knight.itemnum += 1
                Geos.remove(Geo)
                game_world.remove_object(Geo)

    if GroundMonster2.life <= 0:
        for Geo in Geos2.copy():
            if collide(knight, Geo):
                knight.itemnum += 1
                Geos2.remove(Geo)
                game_world.remove_object(Geo)

    if GroundMonster3.life <= 0:
        for Geo in Geos3.copy():
            if collide(knight, Geo):
                knight.itemnum += 1
                Geos3.remove(Geo)
                game_world.remove_object(Geo)

    #승강기 사용
    if collide(elev, knight):
        if elev.sFloor == False:
            if elev.plusy <= 600:
                elev.plusy += 0.25
                elev.savey = elev.plusy
            else:
                if elev.sFloor == False:
                    elev.sFloor = True
                    elev.plusy = 0
                for i in secblocks1:
                    game_world.add_object(i, 0)
                    i.x = 180 + 150 * tempx
                    tempx += 1
        knight.y = elev.y + elev.plusy + 50

    # 두개의 길 선택 승강기
    if twelev.plusy >= 300:
        twelev.dir = -1
    elif twelev.plusy <=0:
        twelev.dir = 1
    twelev.plusy += 0.25* twelev.dir
    if collide(twelev, knight):
        knight.y = twelev.y + twelev.plusy + 50

    if twelev2.plusy >= 300:
        twelev2.dir = -1
    elif twelev2.plusy <= 0:
        twelev2.dir = 1
    twelev2.plusy += 0.25* twelev2.dir
    if collide(twelev2, knight):
        knight.y = twelev2.y + twelev2.plusy + 50

    if key.keyget == False:
        if collide(key, knight):
            key.keyget = True
    if key.onoff == True:
        if knight.x >=7100:
            knight.x = 7100
    # 수정중
    if collide(bosselev, knight):
        if bosselev.sFloor == False:
            if math.fabs(bosselev.savex - bosselev.x) <= 400:
                bosselev.x += 0.5
                knight.x += 0.5
            else:
                bosselev.sFloor = True
        knight.y = bosselev.y + 50


def draw_world():
    for game_object in game_world.all_objects():
        if Map.cur_state == 'start' or Map.cur_state == 'die'or Map.cur_state == 'pause':
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