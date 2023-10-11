#Prettystick en version pétée by Léa et Asqel
import pygame as py
from pygame.locals import *

from key_map import *
from uti.textures import *
from uti.sound import play_sound
from entities import *
from time import time, sleep
from interface import *
from world import *
from events import *
from _thread import start_new_thread
from random import *

py.joystick.init()
py.font.init()

FPS_MAX = 60
TPS_MAX = 150
TPS_MAX_INVERSE = 1 / TPS_MAX

MOD_ENABLED = True

VERSION = "001.00.0"

g_tps = 0

tick_count = 0
day_length = 108000
day_count = 0 # day = 108000

running_dict = {
    "global": True,
    "server": True
}

pygame_events=[]

def check_keys():
    global screen
    global pygame_events
    global key_map
    for i in pygame_events:
        if i.type == py.MOUSEBUTTONDOWN:
            if (1,i.button) == key_map[t_sprint]:
                players[0].speed = 0.85
            elif (1,i.button) == key_map[t_slot1]:
                players[0].inventaire_idx = 0
            elif (1,i.button) == key_map[t_slot2]:
                players[0].inventaire_idx = 1
            elif (1,i.button) == key_map[t_slot3]:
                players[0].inventaire_idx = 2
            elif (1,i.button) == key_map[t_slot4]:
                players[0].inventaire_idx = 3
            elif (1,i.button) == key_map[t_slot5]:
                players[0].inventaire_idx = 4
            elif (1,i.button) == key_map[t_slot6]:
                players[0].inventaire_idx = 5
            elif (1,i.button) == key_map[t_slot7]:
                players[0].inventaire_idx = 6
            elif (1,i.button) == key_map[t_slot8]:
                players[0].inventaire_idx = 7
            elif (1,i.button) == key_map[t_slot9]:
                players[0].inventaire_idx = 8
            elif (1,i.button) == key_map[t_slot10]:
                players[0].inventaire_idx = 9
            elif (1,i.button) == key_map[t_drop_item]:
                players[0].drop_item()
            elif (1,i.button) ==key_map[t_use_item]:
                players[0].inventaire[players[0].inventaire_idx].on_use(players[0].world, players[0])
            elif (1,i.button) == K_ESCAPE:
                players[0].gui = guis["Escape_gui"](players[0])
            elif (1,i.button) == key_map[t_use_object]:
                if not players[0].gui:
                    if players[0].dir == 'u':
                        players[0].world.get_Obj(players[0].pos+(25,-10)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(25,-10)).on_interact(players[0].world,players[0])

                    if players[0].dir == 'r':
                        players[0].world.get_Obj(players[0].pos+(10+50, 25)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(10+50, 25)).on_interact(players[0].world,players[0])

                    if players[0].dir == 'd':
                        players[0].world.get_Obj(players[0].pos+(25,50+10)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(25,50+10)).on_interact(players[0].world,players[0])

                    if players[0].dir == 'l':
                        players[0].world.get_Obj(players[0].pos+(-10,25)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(-10,25)).on_interact(players[0].world,players[0])

        elif i.type == py.MOUSEBUTTONUP:
            if (1, i.button) == key_map[t_sprint]:
                players[0].speed = 0.5  
        elif i.type == py.KEYDOWN:
            if i.key == K_F3:
                players[0].chunk_border=not players[0].chunk_border
            elif i.key == K_ASTERISK:
                toggle_hitbox()
            elif i.key == key_map[t_sprint]:
                players[0].speed = 0.85
            elif i.key == key_map[t_slot1]:
                players[0].inventaire_idx = 0
            elif i.key == key_map[t_slot2]:
                players[0].inventaire_idx = 1
            elif i.key == key_map[t_slot3]:
                players[0].inventaire_idx = 2
            elif i.key == key_map[t_slot4]:
                players[0].inventaire_idx = 3
            elif i.key == key_map[t_slot5]:
                players[0].inventaire_idx = 4
            elif i.key == key_map[t_slot6]:
                players[0].inventaire_idx = 5
            elif i.key == key_map[t_slot7]:
                players[0].inventaire_idx = 6
            elif i.key == key_map[t_slot8]:
                players[0].inventaire_idx = 7
            elif i.key == key_map[t_slot9]:
                players[0].inventaire_idx = 8
            elif i.key == key_map[t_slot10]:
                players[0].inventaire_idx = 9
            elif i.key == key_map[t_drop_item]:
                players[0].drop_item()
            elif i.key ==key_map[t_use_item]:
                players[0].inventaire[players[0].inventaire_idx].on_use(players[0].world, players[0])
            elif i.key ==key_map[t_open_chat]:
                players[0].open_gui("Exec_command")
            elif i.key == K_ESCAPE:
                players[0].gui = guis["Escape_gui"](players[0])
            elif i.key == key_map[t_use_object]:
                if not players[0].gui:

                    if players[0].dir == 'u':
                        players[0].world.get_Obj(players[0].pos+(25,-10)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(25,-10)).on_interact(players[0].world,players[0])

                    if players[0].dir == 'r':
                        players[0].world.get_Obj(players[0].pos+(10+50, 25)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(10+50, 25)).on_interact(players[0].world,players[0])

                    if players[0].dir == 'd':
                        players[0].world.get_Obj(players[0].pos+(25,50+10)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(25,50+10)).on_interact(players[0].world,players[0])

                    if players[0].dir == 'l':
                        players[0].world.get_Obj(players[0].pos+(-10,25)).on_interact(players[0].world,players[0])
                        players[0].world.get_dyn_Obj(players[0].pos+(-10,25)).on_interact(players[0].world,players[0])

        elif i.type == py.KEYUP:
            if i.key == key_map[t_sprint]:
                players[0].speed = 0.5  

def server_thread():
    global running_dict, g_tps, pygame_events, show_hitbox ,tick_count, day_count
    joystick_count = py.joystick.get_count()
    if joystick_count:
        joysticks = []
        for i in range(joystick_count):
            joystick = py.joystick.Joystick(i)
            joystick.init()
            joysticks.append(joystick)
    while running_dict["global"]:
        t0 = time()
        
        tick_count += 1
        while tick_count >= day_length:
            tick_count -= day_length
            day_count += 1
        players[0].day_count = day_count
        players[0].tick_count = tick_count

        for i in events[Event_before_tick_t]:
            i.function(players, pygame_events)
        
        if players[0].gui is not None:
            result = players[0].gui.tick(pygame_events)
            pygame_events = []
            if result == "end_game":
                running_dict["global"] = False
        for i in pygame_events:
            if i.type == py.QUIT:
                running_dict["global"] = False
        check_keys()
            
        pushed_keys=py.key.get_pressed()
        if not players[0].gui:
            if not players[0].riding:
                if pushed_keys[key_map[t_mov_left]] and pushed_keys[key_map[t_mov_down]]:
                    players[0].downleft()
                    players[0].world.activate_collision()

                elif pushed_keys[key_map[t_mov_left]] and pushed_keys[key_map[t_mov_up]]:
                    players[0].upleft()
                    players[0].world.activate_collision()

                elif pushed_keys[key_map[t_mov_right]] and pushed_keys[key_map[t_mov_up]]:
                    players[0].upright()
                    players[0].world.activate_collision()
    
                elif pushed_keys[key_map[t_mov_right]] and pushed_keys[key_map[t_mov_down]]:
                    players[0].downright()
                    players[0].world.activate_collision()
    
                elif pushed_keys[key_map[t_mov_left]]:
                    players[0].left()
                    players[0].world.activate_collision()

                elif pushed_keys[key_map[t_mov_right]]:
                    players[0].right()
                    players[0].world.activate_collision()

                elif pushed_keys[key_map[t_mov_up]]:
                    players[0].up()
                    players[0].world.activate_collision()

                elif pushed_keys[key_map[t_mov_down]]:
                    players[0].down()
                    players[0].world.activate_collision()
            else:
                if pushed_keys[key_map[t_mov_left]] and pushed_keys[key_map[t_mov_down]]:
                    players[0].riding.mov(players[0].world, players[0], "dl")
                elif pushed_keys[key_map[t_mov_left]] and pushed_keys[key_map[t_mov_up]]:
                    players[0].riding.mov(players[0].world, players[0], "ul")
                elif pushed_keys[key_map[t_mov_right]] and pushed_keys[key_map[t_mov_up]]:
                    players[0].riding.mov(players[0].world, players[0], "ur")
                elif pushed_keys[key_map[t_mov_right]] and pushed_keys[key_map[t_mov_down]]:
                    players[0].riding.mov(players[0].world, players[0], "dr")
                elif pushed_keys[key_map[t_mov_left]]:
                    players[0].riding.mov(players[0].world, players[0], "l")
                elif pushed_keys[key_map[t_mov_right]]:
                    players[0].riding.mov(players[0].world, players[0], "r")
                elif pushed_keys[key_map[t_mov_up]]:
                    players[0].riding.mov(players[0].world, players[0], "u")
                elif pushed_keys[key_map[t_mov_down]]:
                    players[0].riding.mov(players[0].world, players[0], "d")
        if not players[0].gui:
            players[0].world.update()
        for i in events[Event_after_tick_t]:
            i.function(players, pygame_events)
        pygame_events = []

        t1 = time()
        if TPS_MAX_INVERSE > t1 - t0:
            sleep(TPS_MAX_INVERSE - (t1 - t0))

        if time() - t0:
            g_tps = 1/(time() - t0)

    running_dict["server"] = False

def draw_inventory():
    x, y = screen.get_width()/2 - Textures["other"]["slot_x_10"].get_width()/2, 10
    screen.blit(Textures["other"]["slot_x_10"], (x,y))
    for i in range(10):
        screen.blit(players[0].inventaire[i].texture, (x+46*(i+1)-40, y+6))
        if players[0].inventaire[i].quantity > 1:
            screen.blit(main_font.render(str(players[0].inventaire[i].quantity),False,(0,0,0)), (x+46*(i+1)-25, y+27))
        if players[0].inventaire_idx == i:
            py.draw.rect(screen, (255,0,0), py.Rect(x+46*(i+1)-46, y+45,40,5))
    if players[0].inventaire[players[0].inventaire_idx].id != "Air":
        text = players[0].inventaire[players[0].inventaire_idx].display_name
        if not text:
            text = players[0].inventaire[players[0].inventaire_idx].id
        text_name = main_font.render(str(text), False, (0,0,0))
        screen.blit(text_name, (-text_name.get_width()//2+ screen.get_width()//2,60))


fullscreen = False
old_w=0
old_h=0
py.display.set_allow_screensaver(0)
will_end = False
def main():
    global day_count
    global tick_count
    global running_dict
    global players
    global will_end
    global key_map
    while 1:
        global pygame_events
        global display_screen
        global old_w, old_h 
        global fullscreen
        #start_new_thread(play_sound, ("nymphe-echo-demo1.flac",))
        if MOD_ENABLED:
            import modloader as md
            md.load_mods()
        load_keys()
        for i in events[Event_on_textures_load_t]:
            i.function(Textures)

        starting_world = World("bed room",(125, 125, 125))
        players.append(Character("Jean", "Magie", "pouffsoufle", None, None, POUFSOUFFLE_TEXTURES_0, None, 100, 0, starting_world))
        players[0].gui = guis["Choose_name"](players[0])
        players[0].pv = 100




        players[0].zoom_out = 1
        players[0].render_distance = 3

        start_new_thread(server_thread, ())

        arial = py.font.SysFont("Arial", 25, False, False)
        fps = 0
        while running_dict["global"] and running_dict["server"]:
            start_time = time()
            pygame_events = py.event.get()
            for i in pygame_events:
                if i.type == py.QUIT:
                    running_dict["global"] = False
                    running_dict["server"] = False
                    will_end = True
                elif i.type == pygame.KEYDOWN and i.key == py.K_F9:
                    running_dict["global"] = False
                    running_dict["server"] = False
                elif i.type == pygame.KEYDOWN and i.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        old_h = display_screen.get_height()
                        old_w = display_screen.get_width()
                        display_screen = pygame.display.set_mode((screen_width, screen_height),py.FULLSCREEN)
                    else:
                        display_screen = pygame.display.set_mode((old_w, old_h),py.RESIZABLE)


            players[0].world : World = players[0].world
            players[0].world.show(screen, players[0].zoom_out)

            for i in events[Event_on_draw_t]:
                i.function(players, screen)

            screen.blit(arial.render(f"fps: {int(fps)}", False, (255, 0, 0)), (0, 0))
            screen.blit(arial.render(f"mid tps: {int(g_tps)}", False, (255, 0, 0)), (0, 30))
            screen.blit(arial.render(str(players[0].pos.floor()), False, (255, 0, 0)), (0, 60))
            screen.blit(arial.render(str(players[0].world.get_Chunk_from_pos(players[0].pos).pos), False, (255, 0, 0)), (0, 90))
            screen.blit(arial.render(str(players[0].money)+" €", False, (255, 0, 0)), (0, 120))
            screen.blit(arial.render(str(players[0].pv) + " Pv", False, (255, 0, 0)), (0, 150))
            screen.blit(arial.render("day: "+str(day_count), False, (255, 0, 0)), (0, 180))
            screen.blit(arial.render("tick: "+str(tick_count), False, (255, 0, 0)), (0, 210))

            draw_inventory()
            if players[0].gui:
                players[0].gui.draw(screen)

            display_screen.fill((0,0,0))
            display_screen_width, display_screen_height = display_screen.get_size()

            # Calculer les dimensions ajustées de l'affichage de screen
            scale_factor_width = display_screen_width / screen.get_width()
            scale_factor_height = display_screen_height / screen.get_height()
            scale_factor = min(scale_factor_width, scale_factor_height)

            adjusted_width = int(screen.get_width() * scale_factor)
            adjusted_height = int(screen.get_height() * scale_factor)

            x_offset = (display_screen_width - adjusted_width) // 2
            y_offset = (display_screen_height - adjusted_height) // 2

            # Redimensionner l'écran en conservant le rapport de hauteur/largeur
            scaled_screen = pygame.transform.scale(screen, (adjusted_width, adjusted_height))

            # Dessiner le contenu de scaled_screen sur display_screen
            display_screen.fill((0, 0, 0))  # Remplir display_screen avec du noir
            display_screen.blit(scaled_screen, (x_offset, y_offset))
            py.display.update()
            t = time()
            if  t - start_time < 1 / 60:
                sleep(1 / 60 - t + start_time)
            fps = 1 / (time() - start_time)
        day_count = 0
        tick_count = 0
        players.pop()
        running_dict["global"] =False
        running_dict["server"] =False
        if will_end:
            break
        sleep(2)
        running_dict["global"] =True
        running_dict["server"] =True



main()

