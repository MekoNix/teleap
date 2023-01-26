import socket, threading
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER="0.0.0.0"
ADDR = (SERVER, PORT)

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect()
def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_length = str(msg_lenght).encode(FORMAT)
    send_length+= b' '* (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
send("Test")
send(DISCONNECT_MESSAGE)