import time
from trilobot import *
import math
from curtsies import Input

tbot = Trilobot()

while True:
    with Input(keynames='curses') as input_generator:

        for e in input_generator:
            print(repr(e))
            let = str(repr(e))
            
            print(let)

            if 'w' in let:
                tbot.forward(1)
                tbot.set_underlight(LIGHT_FRONT_RIGHT, 0, 255, 0)  
                tbot.set_underlight(LIGHT_FRONT_LEFT, 0, 255, 0)  
                time.sleep(0.1)
            elif 'a' in let:
                tbot.turn_right(0.4)
                tbot.clear_underlight(LIGHT_FRONT_LEFT)
                tbot.set_underlight(LIGHT_FRONT_RIGHT, 0, 255, 0)
                time.sleep(0.1)
            elif 'd' in let:
                tbot.turn_left(0.4)
                tbot.clear_underlight(LIGHT_FRONT_RIGHT)
                tbot.set_underlight(LIGHT_FRONT_LEFT, 0, 255, 0)
                time.sleep(0.1)
            elif 's' in let:
                tbot.backward(-1)
                time.sleep(0.1)


            elif 'x' in let:
                tbot.coast()
                print("stop")