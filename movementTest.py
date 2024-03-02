import time
from trilobot import *
import math
import keyboard

tbot = Trilobot()

while True:
    if keyboard.read_key() == 'w':
        tbot.forward(1)
        
        time.sleep(0.1)
    elif keyboard.read_key() == 'a':
        tbot.turn_right(1)
        time.sleep(0.1)
    elif keyboard.read_key() == 'd':
        tbot.turn_left(1)
        time.sleep(0.1)