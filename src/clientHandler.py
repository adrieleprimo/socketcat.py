import subprocess

def runCommand(command):
    command = command.rstrip()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = 'Failed to execute command.\r\n'

    return output

def clientHandler(clientSocket, uploadDestination=None, execute=None, command=False):
    if uploadDestination:
        fileBuffer = b''

        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            else:
                fileBuffer+=data

        try:
            with open(uploadDestination, 'wb') as f:
                f.write(fileBuffer)
            clientSocket.send(f'Successfully saved file to {uploadDestination}\r\n'.encode())
        except:
            clientSocket.send(f'Failed to save file to {uploadDestination}\r\n'.encode())
        
    if execute:
        output = runCommand(execute)
        clientSocket.send(output.encode())

    if command:
        while True:
            clientSocket.send(b'socketCat:#> ')
            cmdBuffer = b''
            while b'\n' not in cmdBuffer:
                cmdBuffer +=clientSocket.recv(1024)

    response = runCommand(cmdBuffer.decode())   
    clientSocket.send(response.encode())