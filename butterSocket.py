from websockets.sync.client import connect
from picamera import Picamera
from butterMove import ButterMove


SOCKET = "ws://localhost:8765/"

def listen():
    bot = ButterMove()
    with connect(SOCKET) as websocket:
        msg = websocket.recv()
        let = str(msg)

        if 'FORWARD' in let:
            bot.foward()
        elif 'TURN_R' in let:
            bot.turnRight()
        elif 'TURN_L' in let:
            bot.turnLeft()
        elif 'BACKWARDS' in let:
            bot.backward()
        elif 'TILT_U' in let:
            bot.tiltUp()
        elif 'TILT_D' in let:
            bot.tiltDown()
        elif 'STOP' in let:
            bot.stopAll()