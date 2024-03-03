import asyncio
import websockets

# Define the message you want to send
message_to_send = "TURN_R\n"

async def send_message():
    uri = "ws://192.168.243.38:8765"
    
    async with websockets.connect(uri) as ws:
        
        await ws.send(message_to_send)

asyncio.get_event_loop().run_until_complete(send_message())
