from websockets.sync.client import connect
from butterMove import ButterMove
import asyncio

SOCKET = "ws://localhost:8765/"

async def getmsg():
    async with connect(SOCKET) as websocket:
        return await websocket.recv()

while True:
    bot = ButterMove()
    
    let = getmsg()

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

