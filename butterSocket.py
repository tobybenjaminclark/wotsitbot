from butterMove import ButterMove
from requests import Session
from signalr import Connection

SOCKET = "https://192.168.243.215:7078/"

bot = ButterMove()

with Session() as session:
    connection = Connection(SOCKET, session)
    
    chat = connection.register_hub('RobotControlHub')

    connection.start()
    

    global_name = None

    def setName(new_name):
        global global_name

        global_name = new_name

    def acceptMessage(name, data):
        if name != global_name:
            return
        
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

    chat.client.on('SetRobotName', setName)
    chat.client.on('RecieveRobotCommand', acceptMessage)

    with connection:
        while True:
            connection.wait(0.2)