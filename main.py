#Prettystick en version pétée by Léa et Asqel
import pygame as py
from pygame.locals import *
from _thread import start_new_thread
from random import *
from uti.textures import *
from uti.sound import play_sound
from time import time, sleep

import key_map
import entities
import world
import events
import modloader
import signals as sig
import saves

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
        if key_map.is_event_key_pressed(i, key_map.t_sprint):
                entities.players[0].speed = 0.85
        elif key_map.is_event_key_pressed(i, key_map.t_use_object):
            if not entities.players[0].guis:
                if entities.players[0].dir == 'u':
                    entities.players[0].world.get_Obj(entities.players[0].pos+(25,-10)).on_interact(entities.players[0].world,entities.players[0])
                    entities.players[0].world.get_dyn_Obj(entities.players[0].pos+(25,-10)).on_interact(entities.players[0].world,entities.players[0])

                if entities.players[0].dir == 'r':
                    entities.players[0].world.get_Obj(entities.players[0].pos+(10+50, 25)).on_interact(entities.players[0].world,entities.players[0])
                    entities.players[0].world.get_dyn_Obj(entities.players[0].pos+(10+50, 25)).on_interact(entities.players[0].world,entities.players[0])

                if entities.players[0].dir == 'd':
                    entities.players[0].world.get_Obj(entities.players[0].pos+(25,50+10)).on_interact(entities.players[0].world,entities.players[0])
                    entities.players[0].world.get_dyn_Obj(entities.players[0].pos+(25,50+10)).on_interact(entities.players[0].world,entities.players[0])

                if entities.players[0].dir == 'l':
                    entities.players[0].world.get_Obj(entities.players[0].pos+(-10,25)).on_interact(entities.players[0].world,entities.players[0])
                    entities.players[0].world.get_dyn_Obj(entities.players[0].pos+(-10,25)).on_interact(entities.players[0].world,entities.players[0])
        elif key_map.is_event_key_pressed(i, key_map.t_open_chat):
            saves.save_player(entities.players[0])
            entities.players[0].open_gui("Exec_command")

        elif key_map.is_event_key_released(i, key_map.t_sprint):
            entities.players[0].speed = 0.5  

        elif i.type == py.KEYDOWN:
            if i.key == K_F3:
                entities.players[0].chunk_border=not entities.players[0].chunk_border
            elif i.key == K_ASTERISK:
                world.toggle_hitbox()


def do_signals() -> None:
    while sig.SIGNALS:
        signal = sig.pop_signal()
        if signal.name == sig.RESTART_SIGNAL:
            running_dict["global"] = False
            running_dict["server"] = False

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
        entities.players[0].day_count = day_count
        entities.players[0].tick_count = tick_count
        
        do_signals()

        for i in events.events[events.Event_before_tick_t]:
            i.function(entities.players, pygame_events)
        
        if entities.players[0].guis:
            result = entities.players[0].guis[-1].tick(pygame_events)
            pygame_events = []
            if result == "end_game":
                running_dict["global"] = False
        for i in pygame_events:
            if i.type == py.QUIT:
                running_dict["global"] = False
        check_keys()
            
        pushed_keys=py.key.get_pressed()
        if not entities.players[0].guis:
            if not entities.players[0].riding:
                if pushed_keys[key_map.key_map[key_map.t_mov_left]] and pushed_keys[key_map.key_map[key_map.t_mov_down]]:
                    entities.players[0].downleft()
                    entities.players[0].world.activate_collision()

                elif pushed_keys[key_map.key_map[key_map.t_mov_left]] and pushed_keys[key_map.key_map[key_map.t_mov_up]]:
                    entities.players[0].upleft()
                    entities.players[0].world.activate_collision()

                elif pushed_keys[key_map.key_map[key_map.t_mov_right]] and pushed_keys[key_map.key_map[key_map.t_mov_up]]:
                    entities.players[0].upright()
                    entities.players[0].world.activate_collision()
    
                elif pushed_keys[key_map.key_map[key_map.t_mov_right]] and pushed_keys[key_map.key_map[key_map.t_mov_down]]:
                    entities.players[0].downright()
                    entities.players[0].world.activate_collision()
    
                elif pushed_keys[key_map.key_map[key_map.t_mov_left]]:
                    entities.players[0].left()
                    entities.players[0].world.activate_collision()

                elif pushed_keys[key_map.key_map[key_map.t_mov_right]]:
                    entities.players[0].right()
                    entities.players[0].world.activate_collision()

                elif pushed_keys[key_map.key_map[key_map.t_mov_up]]:
                    entities.players[0].up()
                    entities.players[0].world.activate_collision()

                elif pushed_keys[key_map.key_map[key_map.t_mov_down]]:
                    entities.players[0].down()
                    entities.players[0].world.activate_collision()
            else:
                if pushed_keys[key_map.key_map[key_map.t_mov_left]] and pushed_keys[key_map.key_map[key_map.t_mov_down]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "dl")
                elif pushed_keys[key_map.key_map[key_map.t_mov_left]] and pushed_keys[key_map.key_map[key_map.t_mov_up]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "ul")
                elif pushed_keys[key_map.key_map[key_map.t_mov_right]] and pushed_keys[key_map.key_map[key_map.t_mov_up]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "ur")
                elif pushed_keys[key_map.key_map[key_map.t_mov_right]] and pushed_keys[key_map.key_map[key_map.t_mov_down]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "dr")
                elif pushed_keys[key_map.key_map[key_map.t_mov_left]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "l")
                elif pushed_keys[key_map.key_map[key_map.t_mov_right]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "r")
                elif pushed_keys[key_map.key_map[key_map.t_mov_up]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "u")
                elif pushed_keys[key_map.key_map[key_map.t_mov_down]]:
                    entities.players[0].riding.mov(entities.players[0].world, entities.players[0], "d")
        if not entities.players[0].guis:
            entities.players[0].world.update()
        for i in events.events[events.Event_after_tick_t]:
            i.function(entities.players, pygame_events)
        pygame_events = []

        t1 = time()
        if TPS_MAX_INVERSE > t1 - t0:
            sleep(TPS_MAX_INVERSE - (t1 - t0))

        if time() - t0:
            g_tps = 1/(time() - t0)

    running_dict["server"] = False


fullscreen = False
old_w=0
old_h=0
py.display.set_allow_screensaver(0)
will_end = False
def main():
    global day_count
    global tick_count
    global running_dict
    global will_end
    global key_map
    while 1:
        global pygame_events
        global display_screen
        global old_w, old_h 
        global fullscreen
        #start_new_thread(play_sound, ("nymphe-echo-demo1.flac",))
        if MOD_ENABLED:
            modloader.load_mods()
        key_map.load_keys()
        for i in events.events[events.Event_on_textures_load_t]:
            i.function(Textures)

        starting_world = world.World("bed room",(125, 125, 125))
        entities.players.append(entities.Character(POUFSOUFFLE_TEXTURES_0, 100, 0, starting_world, "NULL"))
        entities.players[0].open_gui("Main_menu")
        entities.players[0].pv = 100

        entities.players[0].zoom_out = 1
        entities.players[0].render_distance = 3

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
                elif i.type == py.KEYDOWN and i.key == py.K_F9:
                    sig.send_signal(sig.signal(sig.RESTART_SIGNAL))
                elif i.type == py.KEYDOWN and i.key == py.K_F11:
                    fullscreen = not fullscreen
                    if fullscreen:
                        old_h = display_screen.get_height()
                        old_w = display_screen.get_width()
                        display_screen = py.display.set_mode((screen_width, screen_height),py.FULLSCREEN)
                    else:
                        display_screen = py.display.set_mode((old_w, old_h),py.RESIZABLE)


            entities.players[0].world.show(screen, entities.players[0].zoom_out)

            for i in events.events[events.Event_on_draw_t]:
                i.function(entities.players, screen)

            screen.blit(arial.render(f"fps: {int(fps)}", False, (255, 0, 0)), (0, 0))
            screen.blit(arial.render(f"mid tps: {int(g_tps)}", False, (255, 0, 0)), (0, 30))
            screen.blit(arial.render(str(entities.players[0].pos.floor()), False, (255, 0, 0)), (0, 60))
            screen.blit(arial.render(str(entities.players[0].world.get_Chunk_from_pos(entities.players[0].pos).pos), False, (255, 0, 0)), (0, 90))
            screen.blit(arial.render(str(entities.players[0].pv) + " Pv", False, (255, 0, 0)), (0, 150))
            screen.blit(arial.render("day: "+str(day_count), False, (255, 0, 0)), (0, 180))
            screen.blit(arial.render("tick: "+str(tick_count), False, (255, 0, 0)), (0, 210))

            if entities.players[0].guis:
                entities.players[0].guis[-1].draw(screen)

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
            scaled_screen = py.transform.scale(screen, (adjusted_width, adjusted_height))

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
        entities.players.pop()
        running_dict["global"] =False
        running_dict["server"] =False
        if will_end:
            break
        sleep(2)
        running_dict["global"] =True
        running_dict["server"] =True


print(entities.players)
main()