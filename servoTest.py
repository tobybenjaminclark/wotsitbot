#!/usr/bin/env python3
import math
import time
from trilobot import Trilobot, BUTTON_A, BUTTON_B

SWEEPS = 5  # How many sweeps of the servo to perform
STEPS = 10  # The number of discrete sweep steps
STEPS_INTERVAL = 0.5  # The time in seconds between each step of the sequence

tbot = Trilobot()
tbot.set_servo_angle(0)
ang = 0
while True:
    butA = tbot.read_button(BUTTON_A)
    butB = tbot.read_button(BUTTON_B)
    if butA:
        if ang != 45: 
            ang += 1
            tbot.set_servo_angle(ang)
            time.sleep(0.01)

    if butB:
        if ang != -45: 
            ang -= 1
            tbot.set_servo_angle(ang)
            time.sleep(0.01)
