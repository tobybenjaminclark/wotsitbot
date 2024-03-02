from gevent import monkey

monkey.patch_all(thread=False, select=False)


from butterMove import ButterMove
import asyncio

SOCKET = "ws://192.168.243.226:8765/"

async def run():
    bot = ButterMove()
    with connect(SOCKET) as websocket:
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
