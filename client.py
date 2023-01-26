import os
import platform
import socket, threading, time,  sys
from time import sleep
from arts import *

def clear():# Clear the terminal
    if platform.system()=="Windows":
        os.system("cls")
    else:
        os.system("clear")
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
DISCONNECT_MESSAGE="!dis"
SERVER= "192.168.0.11"# Configure it

ADDR = (SERVER, PORT)

client = socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clear()
print(ConnArt)
words = "Connecting..."
for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
clear()
try:

    client.connect(ADDR)

except OSError:
    exit(opus)

while True:
    mesage = input()
    send(mesage)
    if mesage == DISCONNECT_MESSAGE:
        exit("DISCONNECT BY USER")
