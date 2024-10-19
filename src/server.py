import socket
import threading
from clientHandler import clientHandler

def serverLoop(target, port):
    if not target:
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    print(f'[*] Listening on {target}:{port}')

    while True:
        clientSocket, addr = server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')

        clientThread = threading.Thread(target=clientHandler, args=(clientThread,))
        clientThread.start()