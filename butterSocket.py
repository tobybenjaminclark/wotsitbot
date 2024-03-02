from websockets.sync.client import connect
from picamera import Picamera

SOCKET = ' '

def handshake():
    with connect(SOCKET) as websocket:
        msg = websocket.recv()
        