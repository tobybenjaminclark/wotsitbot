import time
from trilobot import *
import math
from curtsies import Input
from picamera import PiCamera

class ButterMove:
    def __init__(self):
        self.tbot = Trilobot()


        self.tbot.set_servo_angle(0)
        self.ang = 0

    def foward(self, speed=1):
        self.tbot.forward(speed)
        self.tbot.clear_underlighting()
        self.tbot.set_underlight(LIGHT_FRONT_RIGHT, 200, 0, 255)  
        self.tbot.set_underlight(LIGHT_FRONT_LEFT, 200, 0, 255)  
        time.sleep(0.1)
    
    def backward(self, speed=1):
        self.tbot.backward(speed)
        self.tbot.clear_underlighting()
        self.tbot.set_underlight(LIGHT_REAR_RIGHT, 255, 0, 0)  
        self.tbot.set_underlight(LIGHT_REAR_LEFT, 255, 0, 0)  
        time.sleep(0.1)

    def turnRight(self, speed=0.8):
        self.tbot.turn_right(speed)
        self.tbot.clear_underlighting()
        self.tbot.set_underlight(LIGHT_FRONT_RIGHT, 0, 255, 0)
        self.tbot.set_underlight(LIGHT_MIDDLE_RIGHT, 0, 255, 0)
        time.sleep(0.1)
    
    def turnLeft(self, speed=0.8):
        self.tbot.turn_left(speed)
        self.tbot.clear_underlighting()
        self.tbot.set_underlight(LIGHT_FRONT_LEFT, 0, 255, 0)
        self.tbot.set_underlight(LIGHT_MIDDLE_LEFT, 0, 255, 0)
        time.sleep(0.1)
    
    def tiltUp(self, degSpeed=2):
        self.stopAll()
        if self.ang < 40: 
            self.ang += degSpeed
            self.tbot.set_servo_angle(self.ang)
            time.sleep(0.01)
    
    def tiltDown(self, degSpeed=2):
        self.stopAll()
        if self.ang > -40: 
            self.ang -= degSpeed
            self.tbot.set_servo_angle(self.ang)
            time.sleep(0.01)

    def stopAll(self):
        self.tbot.coast()
        self.tbot.clear_underlighting()


if __name__ == "__main__":
    bot = ButterMove()
    while True:
        with Input(keynames='curses') as input_generator:

            for e in input_generator:
                print(repr(e))
                let = str(repr(e))
                
                print(let)

                if 'w' in let:
                    bot.foward()
                elif 'd' in let:
                    bot.turnRight()
                elif 'a' in let:
                    bot.turnLeft()
                elif 's' in let:
                    bot.backward()
                elif 'q' in let:
                    bot.tiltUp()
                elif 'e' in let:
                    bot.tiltDown()
                elif 'x' in let:
                    bot.stopAll()
