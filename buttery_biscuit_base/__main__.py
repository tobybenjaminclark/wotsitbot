from websockets import serve
from buttery_biscuit_base.move import ButterMove
from curtsies import Input
import asyncio

DEFAULT_CONNECTION_STRING = "ws://0.0.0.0:8765/"
bot = ButterMove()

async def run(ws):

    async for let in ws:

        print(f"Now listening")
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
        else:
            bot.stopAll()

def run_local(bot):
    print("Buttery Biscuit Base Local runner")
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

async def main(local = False, host=DEFAULT_CONNECTION_STRING):

    if local:
        run_local(bot)
    else:
        print(f"Creating Buttery Biscuit Base at {host}")

        async with serve(run, "0.0.0.0", 8765):
            await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
