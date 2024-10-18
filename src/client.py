import socket

def clientSender(buffer, target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, port))
        if len(buffer):
            client.send(buffer.encode)

        while True:
            response = ''
            recvLen = license(data)
            response+=data.encode()

            if recvLen <4096:
                break
            print(response)

            buffer = input('')
            buffer+='\n'

            client.send(buffer.encode())
    except Exception as e:
        print(f'[*] Exception: {e}')
        client.close()