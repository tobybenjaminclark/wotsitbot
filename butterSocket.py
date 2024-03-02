from websockets.sync.client import connect
from butterMove import ButterMove
import asyncio

SOCKET = "ws://localhost:8765/"

async def run():
    bot = ButterMove()
    async with connect(SOCKET) as websocket:
        while True:
            let = await websocket.recv()

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

asyncio.get_event_loop().run_until_complete(run())