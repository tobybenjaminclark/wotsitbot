from butterMove import ButterMove
from requests import Session
from signalr import Connection

SOCKET = "ws://192.168.243.226:8765/"

bot = ButterMove()

with Session() as session:
    connection = Connection(SOCKET, session)
    
    chat = connection.register_hub('bot')

    connection.start()

    def acceptMessage(data):
        let = str(data)

        print(let)

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

    chat.client.on('newMessageRecieved', acceptMessage)

    with connection:
        while True:
            connection.wait(0.2)