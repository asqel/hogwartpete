# example mod

## mod init
create a folder example_mod in the mods folder \
create a mod_init.py file in example_mod folder \
(the game will try to execute this file when starting) \
(you can replace example_mod with the name of your mod)

## add textures
create a assets folder in example_mod \
create a folder with name of the texture category in it \
(the category of textures is not checked by the game so
you can put anything in them or create another)
add your image in the folder \
create a file with the same name as your image ending in .tx \
(this file tell the game how to cut / resize / name your textures) \
in this file you have to register the texture like this :  
    x y w h new_w new_h $ texture_name \
    x y are the coordinate of the top left corner of the texture in the image \
    w h is the width and height of the textrue in pixel in the image \
    new_w new_h are the width and heiht resized in the game in pixel  \
    simple objects are generaly resized with 50 50 \
           items with 30 30

to replace a texture do everythin like when adding a texture \
but when place it in the same category as the one that you  \
want to replace and name it the same 

### example : 
    to add a simple texture here it will be a a red square of 16x16 pixel \
    place a the top left corner of the image the image will be called red.png .\
    you have to create the folder Obj then place the image in it \
    create red.tx and write in it 0 0 16 16 50 50 $ red_square
    (this will register a texture called red_square at 0 0 with a width and \
    height of 16 16 in the .png and resize it with 50 50 of width and height)

## add Object
to add an object you have to import the texture and the object(Obj) class with \
(from uti import * \
from objs import *) \
create a class with the name of your object that inherite from Obj \
the \_\_init\_\_ have to take only x and y as parameters \
in the super.\_\_init\_\_ \
you have to pass: \
id (the id of your obj generally the same as class (self.\_\_class\_\_.\_\_name\_\_)) \
x (x position) \
y (y position) \
istop (True if the texture is above the player False otherwise) \
texture (you can access texture with Textures[category][texture_name]) \
hitbox (you can either use pre-made hitboxes like HITBOX_50X50 or HITBOX_0X0 or create yours)
data (optional dictionary for the object it can only contains int, float, str, boolean, dictionary or lists)

### example :
we will create an object called Square with a texture red_square in Obj
#### add the imports :
    from uti import * 
    from objs import *
### create the class : 
    class Square(Obj):
        def __init__(x, y) -> None:
            super.__init__(self.__class_.__name__, x, y, False, Textures["Obj"]["red_square"], HITBOX_50X50)
    
### registering the Object :
    registerObj(Square)
