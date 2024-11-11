import sys
import socket
import getopt
import threading
import subprocess
import ssl
import utils.logger as logger
import bcrypt
import getpass

listen = False
command = False
upload = False
execute = ''
target = ''
uploadDestination = ''
port = 0

def usage():
    print('Obtuosa Tool\n')
    print('Usage: socketCat.py -t targetHost -p port\n')
    print('-l --listen                   - listen on [host]:[port] for incoming connections')
    print('-e --execute=fileToRun        - execute the given file upon receiving a connection')
    print('-c --command                  - initialize a command shell')
    print('-u --upload=destination       - upon receiving connection upload a file and write to [destination]')
    print()
    print('Examples:')
    print('socketCat.py -t 192.168.0.1 -p 5555 -l -c')
    print('socketCat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print('socketCat.py -t 192.168.0.1 -p 5555 -l -e="cat /etc/passwd"')
    print('echo "ABCDEFGHI" | socketCat.py 192.168.11.12 -p 135')
    sys.exit(0)

def setPassword():
    password = getpass.getpass('Enter a new password to configure: ')
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open('passwordHash.txt', 'wb') as f:
        f.write(hashed)
    print('Password successfully configured!')



def checkPassword():
    try:
        with open('passwordHash.txt', 'rb') as f:
            storedHash = f.read()
    except FileNotFoundError:
        print("Password hash not found! Let's set a new password")
        setPassword()
        return True
    
    password = getpass.getpass('Enter your password:  ')
    if bcrypt.checkpw(password.encode(), storedHash):
        print('Successful Authentication!.')
        return True
    else:
        print('Incorrect password. Access Denied')
        return False


def clientSender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = ssl.wrap_socket(client, ssl_version=ssl.PROTOCOL_TLSv1_2)
    logger.logConnection(target, port, 'outbound')

    try:
        client.connect((target,port))
        if len(buffer):
            client.send(buffer.encode())
            logger.logMessageSent(buffer)

        while True:
            recvLen = 1
            response = ''
        
            while recvLen:
                data = client.recv(4096)
                recvLen = len(data)
                response+=data.decode()
 
                if recvLen < 4096:
                    break
            print('[*] Received response: ')
            logger.logMessageReceived(response.decode())
            print(response)
            
            buffer = input('')
            buffer+='\n'

            client.send(buffer.encode())
            logger.logMessageSent(buffer)
    except Exception as e:
        logger.logError(f'Exception when connecting: {str(e)}')
        print('[*] Exception! Exiting.')

        client.close()

def serverLoop():
    global target

    if not len(target):
        target = '0.0.0.0'
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)
    logger.logConnection(target, port, 'serverListening')

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='./cert.pem', keyfile='./key.pem')

    print(f'[*] Listening on {target}:{port}')

    while True:
        clientSocket, addr = server.accept()
        logger.logConnection(addr[0], addr[0], 'inbound')
        clientSocket = context.wrap_socket(clientSocket, server_side=True)
        clientThread = threading.Thread(target=clientHandler, args=(clientSocket,))
        clientThread.start()

def runCommand(command):
    command = command.rstrip()
    logger.logCommandExecution(command)
    print(f"[*] Running command: {command}")

    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        logger.logError(f'Error executing command')
        output = f'Failed to execute command.\r\n'
    return output


def clientHandler(clientSocket):
    global upload
    global execute
    global command

    clientAddress = clientSocket.getpeername()
    logger.logConnection(clientAddress[0], clientAddress[1])

    if len(uploadDestination):
        fileBuffer = b''
        logger.logFileUpload(uploadDestination, True)
        print(f'[*] Upload destination set to {uploadDestination}')   
        while True:
            data = clientSocket.recv(1024)

            if not data:
                break
            else:
                fileBuffer+=data

        try:
            fileDescriptor = open(uploadDestination, 'wb')
            fileDescriptor.write(fileBuffer)
            fileDescriptor.close()

            clientSocket.send(f'Successfully saved file to {uploadDestination}\r\n')
            logger.logFileUpload(uploadDestination, True)
        except:
            clientSocket.send(f'Failed to save file to {uploadDestination}\r\n')
            logger.logFileUpload(uploadDestination, False)
    
    if len(execute):
        logger.logCommandExecution(execute)
        print(f'[*] Executing command: {execute}')
        output = runCommand(execute)
        clientSocket.send(output)
    
    if command:
        logger.logCommandExecution('Shell Command Started')
        print(f'[*] Command shell requested')
        while True:
            clientSocket.send(b'socketCat:#> ')
            cmdBuffer = b''
            while b'\n' not in cmdBuffer:
                cmdBuffer += clientSocket.recv(1024)
            response = runCommand(cmdBuffer.decode().strip())
            clientSocket.send(response)
            logger.logMessageSent(response.decode())

    while True:
        request = clientSocket.recv(1024).decode()
        if not request:
            break
        logger.logMessageReceived(request)
        print(f'[*] Received: {request}')
        clientSocket.send(f'Server received: {request}\n'.encode())
        

def main():
    global listen
    global port
    global execute
    global command
    global uploadDestination
    global target

    if not len(sys.argv[1:]):
        usage()
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hle:t:p:cu:',
        ['help', 'listen', 'execute', 'target', 'port', 'command', 'upload'])
    except getopt.GetoptError as err:
        logger.logError(f'Option Error: {str(err)}')
        print(str(err))
        usage()
    
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = a
        elif o in ('-c', '--command'):
            command = True
        elif o in ('-u', '--upload'):
            uploadDestination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, 'Unhandled Option'

    if not checkPassword():
        print('Authentication failed. Closing.')
        sys.exit(1)
    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        clientSender(buffer)

    if listen:
        serverLoop()
main()