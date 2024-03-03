import asyncio
import websockets

TEST_URI = "ws://192.168.243.38:8765"

async def send_message():
    # Define the message you want to send
    message_to_send = "TURN_R\n"
    
    async with websockets.connect(TEST_URI) as ws:
        
        await ws.send(message_to_send)

if __name__=="__main__":
    asyncio.get_event_loop().run_until_complete(send_message())
