import socket, threading
def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_length = str(msg_lenght).encode(FORMAT)
    send_length+= b' '* (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER= socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    mesage = input()
    send(mesage)
    if mesage == DISCONNECT_MESSAGE:
        exit("DISCONNECT BY USER")