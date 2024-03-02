import asyncio
import websockets

# Define the message you want to send
message_to_send = "TURN_R\n"

async def send_message(websocket, path):
    # When a client connects, send the message and close the connection
    await websocket.send(message_to_send)
    await websocket.close()

start_server = websockets.serve(send_message, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
