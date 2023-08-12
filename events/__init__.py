import os
import importlib as imp
__event_count = 0
def __next_event():
    global __event_count
    __event_count += 1
    return __event_count - 1
    


Event_before_tick_t = __next_event()
Event_after_tick_t = __next_event()
Event_on_draw_t = __next_event()
Event_on_textures_load_t = __next_event()
Event_on_chunk_generate = __next_event()
Event_on_world_chunk = __next_event()

Event_max_t = __next_event()

Key_event_mouse = 0
Key_event_key = 0




Event_type = int
Key_event_type = int

"""
type of event :
    Event_before_tick_t : called before everything on the server
        function : (players : list[Character], pygame_events : pygame.event.Event)
        
    Event_after_tick_t : called after everything on the server
        function : (players : list[Character], pygame_events : pygame.event.Event)
        
    Event_on_draw_t : called after everything has been drawn to the screen
        function : (players : list[Character], screen : pygame.Surface)
        
    Event_on_textures_load_t:
        function : (Texture : dict[str,dict[str,py.Surface]])

    Event_on_chunk_generate:
        function : (players : list[Character], chunk : Chunk)

    Event_on_world_load:
        function : (players : list[Character], world)
"""
class Event:
    def __init__(self, type : Event_type, function : 'function'):
        self.type = type
        self.function = function


events :dict[int,list[Event]] ={i : [] for i in range(Event_max_t)} # {type:[events]}


def registerEvent(event : Event):
    global events
    if event.type >= Event_max_t:
        print("Error when registering event incorrect type")
        exit(1)
    events[event.type].append(event)
    
#import every spells
module_names=os.listdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(len(module_names)):
    if module_names[i]=="__init__.py":
        module_names.pop(i)
        break
for i in range(len(module_names)):
    if module_names[i].endswith(".py"):
        module_names[i]=module_names[i][:-3]

for i in module_names:
    imp.import_module(f".{i}", __package__)