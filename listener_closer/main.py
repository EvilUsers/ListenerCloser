from sys import argv
from time import sleep
from include import banner
import socket
from datetime import datetime

RED ='\033[0;31m'
NFR ='\033[0;0m'

if (argv[0]):
    print('Modo de uso : python3 main.py [IP] [PORTA] [MENSAGEM]')
    print("Exemplo     : python3 main.py 192.168.0.115 40 'Evil Users'")
    print('')

host = str(argv[1])
port = int(argv[2])
msg  = str(argv[3])

banner.showbanner()
print(f'           [--           {RED}Evil Users{NFR}           --]')
print('           [--  Developed by xRev3rse & D0zz  --]')
print('\n','='*60,'\n')

def conectar():
    while True:
        now  = datetime.now()
        hour = now.hour
        min  = now.minute
        sec  = now.second
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = s.connect_ex((host, port))
        if (c == 0):
            s.send(msg.encode("utf-8"))
            print(f' [*] Listener closed : {hour}h:{min}m:{sec}s')
        return c

while True:
    conectar()