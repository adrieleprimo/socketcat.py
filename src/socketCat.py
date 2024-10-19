import sys
import getopt
from server import serverLoop
from client import clientSender
from utils import usage

listen = False
command = False
upload = False
execute = ''
target = ''
uploadDestination = ''
port = 0


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
    
    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        clientSender(buffer, target, port)

    if listen:
        serverLoop(target, port)

if __name__ == '__main__':
    main()