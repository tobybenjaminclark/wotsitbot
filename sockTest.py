import asyncio
import websockets

# Define the message you want to send
message_to_send = "TURN_R\n"

async def send_message():
    server = await websockets.serve(message_to_send, 'localhost', 8765)
    await server.wait_closed()

asyncio.run(send_message())
