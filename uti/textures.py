import pygame as py
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folders = list(os.listdir(f"{path}/src"))

Textures:dict[str,dict[str,py.Surface]]={i:{} for i in folders}

py.display.init()
screen=py.display.set_mode((1080,720),py.RESIZABLE)


"""
animation for animated tiles are store in directories that are in tiles_animation
they are stored in differents png called frame_0 to frame_n where n is ther number of frame +1
and there must be a file called delay containing delay between a frame 

ex :
    tiles_animation/grass_tile/-- frame_0
                               |- frame_1
                               |- frame_2
                               |- delay (contains : 0)
"""

def cut_image(image, x, y, width, height):
    sous_image = py.Surface((width, height), py.SRCALPHA)
    sous_image.blit(image, (0, 0), py.Rect(x, y, width, height))
    return sous_image

def make_texture(folder:str,tx_file:str):
    global Textures
    png_file=tx_file[:-3]+".png"
    
    if not os.path.exists(f"{path}/src/{folder}/{png_file}"):
        print(f"ERROR {path}/src/{folder}/{tx_file} doesent have a matching .png file")
        exit(1)
    if not os.path.isfile(f"{path}/src/{folder}/{png_file}"):
        print(f"ERROR {path}/src/{folder}/{tx_file} doesent have a matching .png file")
        exit(1)
        
    images:list[list[str|int]]=[] #name x y w h resize_w resize_h
    with open(f"{path}/src/{folder}/{tx_file}","r") as f:
        lines=f.read().split('\n')
        for i in range(len(lines)):
            lines[i]=lines[i].rstrip('\n')
        while "" in lines:
            lines.remove("")
        for i in lines:
            if not i.startswith("-"):
                if " $ " not in i:
                    print(f"ERROR in {path}/src/{folder}/{tx_file} missing separator ' $ '")
                    exit(1)
                name=i.split(" $ ")[1].rstrip()
                numbers=i.split(' $ ')[0].split(" ")
                while "" in numbers:
                    numbers.remove("")
                for i in range(6):
                    numbers[i]=numbers[i].rstrip()
                for i in range(6):
                    if not numbers[i].isdigit():
                        print(f"ERROR in {path}/src/{folder}/{tx_file} values not number")
                        exit(1)
                images.append([name,
                    int(numbers[0]),
                    int(numbers[1]),
                    int(numbers[2]),
                    int(numbers[3]),
                    int(numbers[4]),
                    int(numbers[5])
                ])
    for i in images:
        if folder!="":
            if i[0] in Textures[folder].keys():    
                print(f"ERROR in textures redefinition of texture in {path}/src/{folder}/{tx_file}")
                exit(1)
            to_cut=py.image.load(f'{path}/src/{folder}/{png_file}')
            Textures[folder][i[0]]=py.transform.scale(cut_image(to_cut,i[1],i[2],i[3],i[4]),(i[5],i[6]))
            continue
        to_cut=py.image.load(f'{path}/src/{folder}/{png_file}')
        Textures[folder][i[0]]=py.transform.scale(cut_image(to_cut,i[1],i[2],i[3],i[4]),(i[5],i[6]))

for i in folders:
    if os.path.isdir(f"{path}/src/{i}"):
        if i not in ["tiles_animation","not_texture"]:
            for k in os.listdir(f"{path}/src/{i}"):
                if k.endswith(".tx"):
                    make_texture(i,k)
        else:...
            #TODO : implement support for animations
    elif i.endswith(".tx"):
        make_texture("",i)


#to acces a texture , Textures[FOLDER_NAME][TEXTURE_NAME]
#if texture not in folder , Textures[TEXTURE_NAME]

"""
creation of textures:
    create a file .png and a .tx file that has the same name
    .tx should look like this
    
    (you can start a line by a - and it will be treated as a comment)
    
        posX posY width height in-game_width in-game_height $ name
        -this is a comment
        posX posY width height in-game_width in-game_height $ name
        ...
    
    exemple:
        text.png
        text.tx :
            0 0 16 16 50 50 $ texture1
            0 16 16 32  50 100 $ texture2
    that means that text.png contains a texture called textures1 at (0,0) with a
    width of 16 and a height of 16 and which will be resized to (50,50) and
    a texture called textures1 at (0,16) with a
    width of 16 and a height of 32 and which will be resized to (50,100)
"""
#player_0
POUFSOUFFLE_TEXTURES_0=[
    Textures["player"]["mc_up_0"],
    Textures["player"]["mc_right_0_pf"],
    Textures["player"]["mc_down_pf"],
    Textures["player"]["mc_left_0_pf"],
]

GRIFFONDOR_TEXTURES_0=[
    Textures["player"]["mc_up_0"],
    Textures["player"]["mc_right_0_gf"],
    Textures["player"]["mc_down_gf"],
    Textures["player"]["mc_left_0_gf"],
]

SERDAIGLE_TEXTURES_0=[
    Textures["player"]["mc_up_0"],
    Textures["player"]["mc_right_0_sd"],
    Textures["player"]["mc_down_sd"],
    Textures["player"]["mc_left_0_sd"],
]

SERPENTARD_TEXTURES_0=[
    Textures["player"]["mc_up_0"],
    Textures["player"]["mc_right_0_sp"],
    Textures["player"]["mc_down_sp"],
    Textures["player"]["mc_left_0_sp"],
]

#player_1
POUFSOUFFLE_TEXTURES_1=[
    Textures["player"]["mc_up_1"],
    Textures["player"]["mc_right_1_pf"],
    Textures["player"]["mc_down_pf"],
    Textures["player"]["mc_left_1_pf"],
]

GRIFFONDOR_TEXTURES_1=[
    Textures["player"]["mc_up_1"],
    Textures["player"]["mc_right_1_gf"],
    Textures["player"]["mc_down_gf"],
    Textures["player"]["mc_left_1_gf"],
]

SERDAIGLE_TEXTURES_1=[
    Textures["player"]["mc_up_1"],
    Textures["player"]["mc_right_1_sd"],
    Textures["player"]["mc_down_sd"],
    Textures["player"]["mc_left_1_sd"],
]

SERPENTARD_TEXTURES_1=[
    Textures["player"]["mc_up_1"],
    Textures["player"]["mc_right_1_sp"],
    Textures["player"]["mc_down_sp"],
    Textures["player"]["mc_left_1_sp"],
]


FARINE_TEXTURE=[
    Textures["player"]["farine_up"],
    Textures["player"]["farine_right"],
    Textures["player"]["farine_down"],
    Textures["player"]["farine_left"],

]

NOTHING_TEXTURE=py.Surface((50,50)).convert_alpha()
NOTHING_TEXTURE.fill(py.Color(0,0,0,0))

texture_ptr=0
def next_texture():
    global texture_ptr
    texture_ptr+=1
    if texture_ptr >=9:
        texture_ptr=0
    return[
        POUFSOUFFLE_TEXTURES_0,
        POUFSOUFFLE_TEXTURES_1,
        GRIFFONDOR_TEXTURES_0,
        GRIFFONDOR_TEXTURES_1,
        SERDAIGLE_TEXTURES_0,
        SERDAIGLE_TEXTURES_1,
        SERPENTARD_TEXTURES_0,
        SERPENTARD_TEXTURES_1,
        FARINE_TEXTURE
    ][texture_ptr]
        