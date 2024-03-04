import asyncio
import websockets
import cv2
import numpy as np
from time import sleep as zzz

TEST_URI = "ws://192.168.243.38:8765"

async def send_message():
    # Define the message you want to send
    message_to_send = "STOP\n"
    
    async with websockets.connect(TEST_URI) as ws:
        while True:
            await ws.send(message_to_send)
            image = await ws.recv()

            image = cv2.imdecode(np.asarray(bytearray(image), dtype='uint8'), cv2.IMREAD_COLOR)
            cv2.imshow("Hello", image)
            cv2.waitKey(1)
            

if __name__=="__main__":
    asyncio.run(send_message())
