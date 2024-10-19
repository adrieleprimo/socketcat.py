import socket

def clientSender(buffer, target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, port))
        if len(buffer):
            client.send(buffer.encode)

        while True:
            recvLen = 1
            response = ''

            while recvLen:
                data = client.recv(4096)
                recvLen = len(data)
                response+=data.decode()

            if recvLen < 4096:
                break
            print(f'[*] Received response: {response}')

            buffer = input('')
            buffer+='\n'

            client.send(buffer.encode())
    except Exception as e:
        print(f'[*] Exception: {e}')
        client.close()