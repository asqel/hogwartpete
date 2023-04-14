"""
event types:
    on_game_tick : called on each game tick
    on_world_tick : called on each game tick when world.name==event.world_name
    on_player_tick : called for each player each game tick
    on_key_pressed 
    on_go_up:
    on_go_down:
    on_go_left:
    on_go_right:
    on_go: joystic vector is passed as arg if no joystic vector of keyboard movement ex: up+left ->(-1,1)
    on_change_world : args->old_world,new_world
    


"""