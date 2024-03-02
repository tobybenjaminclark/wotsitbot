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
                time.sleep(0.1)
            elif 'a' in let:
                tbot.turn_right(1)
                time.sleep(0.1)
            elif 'd' in let:
                tbot.turn_left(1)
                time.sleep(0.1)
            elif 's' in let:
                tbot.backward(-1)
                time.sleep(0.1)


            elif x in let:
                tbot.coast()
                print("stop")