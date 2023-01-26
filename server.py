import socket
import threading
from arts import *
HEADER = 64
PORT = 5050
SERVER = "192.168.0.11"# Configure it
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!dis"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    firstcn=1
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == "!help":
                conn.send(str(helpmenu).encode(FORMAT)) # Не работает надо проврить

            elif firstcn ==1:
                conn.send(WelcumArt.encode(FORMAT))
                firstcn+=1
            else:
                pass
            print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()