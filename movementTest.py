import time
from trilobot import *
import math
from curtsies import Input

tbot = Trilobot()

while True:
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print(repr(e))

    # if keyboard.read_key() == 'w':
    #     tbot.forward(1)
        
    #     time.sleep(0.1)
    # elif keyboard.read_key() == 'a':
    #     tbot.turn_right(1)
    #     time.sleep(0.1)
    # elif keyboard.read_key() == 'd':
    #     tbot.turn_left(1)
    #     time.sleep(0.1)