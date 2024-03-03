from butterMove import ButterMove
import asyncio
from websockets.server import serve

SOCKET = "ws://0.0.0.0:8765/"

bot = ButterMove()

async def do(ws):
    async for let in ws:
        print(let)
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

async def main():
    async with serve(do, "0.0.0.0", 8765):
        await asyncio.Future()
    
asyncio.run(main())
