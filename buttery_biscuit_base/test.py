import asyncio
import websockets
import cv2

TEST_URI = "ws://192.168.243.38:8765"

async def send_message():
    # Define the message you want to send
    message_to_send = "TURN_R\n"
    
    async with websockets.connect(TEST_URI) as ws:
        await ws.send(message_to_send)
        image = await ws.recv()

        image = cv2.imdecode(image)
        cv2.imshow("Hello", image)

if __name__=="__main__":
    asyncio.run(send_message())
