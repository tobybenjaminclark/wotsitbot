import time
from trilobot import *
import math
from curtsies import Input

tbot = Trilobot()

while True:
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            print(repr(e))
            let = repr(e)

            if let == 'w':
                tbot.forward(1)
                
                time.sleep(0.1)
            elif let == 'a':
                tbot.turn_right(1)
                time.sleep(0.1)
            elif let == 'd':
                tbot.turn_left(1)
                time.sleep(0.1)