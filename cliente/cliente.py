import os
import xmlrpc.client
from colorama import Fore
s = xmlrpc.client.ServerProxy('http://192.168.1.76:8000/mis_archivos')
currentPath = 'home/'

while True:
    comando = input(Fore.MAGENTA + ('{}>'.format(currentPath,color='green')))
    argumentos = comando.split(' ')

    try:
        if argumentos[0] == 'create':
            print(Fore.LIGHTRED_EX + s.create(currentPath,argumentos[1]))
        elif argumentos[0] == 'read':
            print(Fore.LIGHTBLACK_EX + s.read(currentPath,argumentos[1]))
        elif argumentos[0] == 'write':
            if len(argumentos) > 3:
                argumentos[2] = ' '.join(argumentos[2:(len(argumentos))])
            print(Fore.LIGHTRED_EX + s.write(currentPath, argumentos[1], argumentos[2]))
        elif argumentos[0] == 'rename':
            print(Fore.LIGHTRED_EX + s.rename(currentPath,argumentos[1], argumentos[2]))
        elif argumentos[0] == 'rm':
            print(Fore.LIGHTRED_EX + s.remove(currentPath,argumentos[1]))
        elif argumentos[0] == 'mkdir':
            print(Fore.LIGHTRED_EX + s.createdir(currentPath,argumentos[1]))
        elif argumentos[0] == 'rmdir':
            print(Fore.LIGHTRED_EX + s.rmdir(currentPath,argumentos[1]))
        elif argumentos[0] == 'ls':
            print(Fore.LIGHTBLUE_EX + s.ls(currentPath))
        elif argumentos[0] == 'cd':
            currentPath = s.cd(currentPath,argumentos[1])
        elif argumentos[0] == '-h':
            print(Fore.LIGHTBLACK_EX + s.help())
        elif argumentos[0] == 'exit':
            exit(0)
        elif argumentos[0] == 'upload':
            if os.path.isfile(argumentos[1]):
                name = os.path.basename(argumentos[1])
                f = open(argumentos[1], 'rb')
                send = xmlrpc.client.Binary(f.read())
                print(s.upload(currentPath, name, send))
            else:
                print('No se encontó el archivo ' + argumentos[1])
        else:
            print(Fore.RED + 'No existe el comando')
    except (IndexError):
        print(Fore.RED + 'Argumentos faltantes (-h para ver todos los comandos disponibles)')