import os 
import importlib as imp

path = os.path.dirname(os.path.abspath(__file__))

mods = []

def load_mods():
    if os.path.isdir(f'{path}/mods'):
        for i in os.listdir(f'{path}/mods'):
            if os.path.isdir(f'{path}/mods/{i}'):
                if os.path.exists(f'{path}/mods/{i}/mod_init.py'):
                    if not os.path.isdir(f'{path}/mods/{i}/mod_init.py'):
                        imp.import_module(f"mods.{i}.mod_init",__package__)
                        mods.append(i)

                    else:
                        print(f"{path}/mods/{i}/mod_init.py is not a file")
                        exit(1)

                else:
                    print(f"{path}/mods/{i}/mod_init.py doesn' exists")
                    exit(1)

            else:
                print(f'{path}/mods/{i} is not a folder')
                exit(1)

    else:
        print(f'{path}/mods is not a folder')
        exit(1)