import os 
import importlib as imp
from importlib.machinery import SourceFileLoader


path = os.path.abspath(".")

mods = []

def load_mods():
    if os.path.isdir(f'{path}/mods'):
        for i in os.listdir(f'{path}/mods'):
            if os.path.isdir(f'{path}/mods/{i}'):
                if os.path.exists(f'{path}/mods/{i}/mod_init.py'):
                    if not os.path.isdir(f'{path}/mods/{i}/mod_init.py'):
                        SourceFileLoader(f"{i}",f"{path}/mods/{i}/mod_init.py").load_module()
                        #imp.import_module(f"mods.{i}.mod_init",package=None)
                        mods.append(i)

                    else:
                        print(f"{path}/mods/{i}/mod_init.py is not a file")
                        continue

                else:
                    print(f"{path}/mods/{i}/mod_init.py doesn' exists")
                    continue

            else:
                print(f'{path}/mods/{i} is not a folder')
                continue

    else:
        print(f'{path}/mods is not a folder')