import itertools
from time import sleep
import random

colors = itertools.cycle(['red','yellow','green'])

def rg_timer():
    return random.randint(3, 7)

def light_rotation(colors):
    for color in colors:
        if color == 'yellow':
            print(f'Caution! The light is {color}')
            sleep(3)
        elif color == 'red':
            print(f'STOP! The light is {color}')
            sleep(rg_timer())
        else:
            print(f'Go! The light is {color}')
            sleep(rg_timer())


if __name__ == '__main__':
    light_rotation(colors)