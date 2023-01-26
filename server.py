import threading
import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT_MESSAGE = '!DISCONECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length.decode(FORMAT))
        if msg == DISCONECT_MESSAGE:
            connected = False

        print(f'[{addr}] {msg}')
    conn.close()

def start():
    server.listen()
    while True:
        addr, conn = server.accept()
        print(addr, conn)
        thread = threading.Thread(target=handle_client, args=(addr, conn))
        thread.start()
        print(f'[ACTIVE CONNECTING] {threading.active_count() - 1}')

print('[STARTING] server is starting...')
start()