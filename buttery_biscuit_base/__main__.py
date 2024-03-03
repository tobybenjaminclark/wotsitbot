from websockets import connect
from buttery_biscuit_base.move import ButterMove
import asyncio

DEFAULT_CONNECTION_STRING = "ws://0.0.0.0:8765/"

async def run(host = DEFAULT_CONNECTION_STRING):
    print(f"Creating Buttery Biscuit Base at {host}")

    bot = ButterMove()
    with connect(host) as websocket:
        print(f"Now listening")
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


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())
