import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8000/mis_archivos')
currentPath = 'home/'

while True:
    comando = input('>')
    argumentos = comando.split(' ')

    if argumentos[0] == 'create':
        print(s.create(currentPath,argumentos[1], argumentos[2]))
    elif argumentos[0] == 'read':
        print(s.read(currentPath,argumentos[1]))
    elif argumentos[0] == 'write':
        print(s.write(currentPath,argumentos[1]), argumentos[2])
    elif argumentos[0] == 'rename':
        print(s.rename(currentPath,argumentos[1], argumentos[2]))
    elif argumentos[0] == 'rm':
        print(s.remove(currentPath,argumentos[1]))
    elif argumentos[0] == 'mkdir':
        print(s.createdir(currentPath,argumentos[1]))
    elif argumentos[0] == 'rmdir':
        print(s.rmdir(currentPath,argumentos[1]))
    elif argumentos[0] == 'ls':
        print(s.ls(currentPath))
    elif argumentos[0] == 'cd':
        currentPath = s.cd(currentPath,argumentos[1])
        print(currentPath)
    elif argumentos[0] == '-h':
        print(s.help())
    else:
        print('No existe el comando')