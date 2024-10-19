import sys

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
    print('echo "ABCDEFGHI" | ./socketCat.py 192.168.11.12 -p 135')
    sys.exit(0)