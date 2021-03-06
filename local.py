import os
import shutil

class filemanager:
    def __init__(self):
        self.currentPath = 'home/'  # inicia en la raiz del sistema de archivos

    def create(self, name, content):
        try:
            newfile = open(self.currentPath + name, 'w+')  # write-read
            newfile.write(content)
            newfile.close()
            return 'Archivo creado'
        except (OSError, IOError):
            print('No se pudo crear "' + self.currentPath + name + '" Revise que el nombre sea válido')

    def read(self, name):
        try:
            openfile = open(self.currentPath + name, 'r')  # read
            content = openfile.read()
            return content
        except (OSError, IOError):
            print('No se pudo abrir "' + self.currentPath + name + '" Revise que el nombre sea correcto')

    def write(self, name, content):
        try:
            openfile = open(self.currentPath + name, 'a')  # append
            openfile.write(content)
            return 'Añadido al archivo'
        except (OSError, IOError):
            return 'No se pudo abrir "' + self.currentPath + name + '" Revise que el nombre sea correcto'

    def rename(self, name, newname):
        try:
            os.rename(self.currenPath + name, self.currentPath + newname) # Rename
            return 'Archivo renombrado'
        except (OSError, IOError):
            return 'No se pudo abrir "' + self.currentPath + name + '" Revise que el nombre sea correcto'

    def remove(self, name):
        try:
            os.remove()
            return 'Archivo eliminado'
        except (OSError, IOError):
            return 'No se encontró "' + self.currentPath + name + '" Revise que el nombre sea correcto'

    def rmdir(self, name):
        try:
            shutil.rmtree(self.currentPath + name) # Borra carpeta y sus contenidos
            return 'Carpeta eliminada'
        except (OSError, IOError):
            return 'No se encontró "' + self.currentPath + name + '" Revise que el nombre sea correcto'

    def createdir(self, name):
        try:
            os.makedirs(self.currentPath + name)
            return self.currentPath
        except (OSError, IOError):
            return 'No se pudo crear "' + self.currentPath + name + '" Revise que el nombre de la carpeta no exista'

    def ls(self):
        try:
            return os.listdir(self.currentPath)
        except (OSError, IOError):
            return 'Hubo un error que no debería existir'

    def cd(self, name):
        if name == '..':
            dirs = self.currentPath.split('/')
            if len(dirs) == 2:
                return self.currentPath
            else:
                dirs.pop()
                dirs.pop()
                self.currentPath = '/'.join(dirs) + '/'
                return self.currentPath
                ath
        if name[0] == '/':
            self.currentPath = 'home/'
            return self.currentPath

        if os.path.exists(self.currentPath + name):
            self.currentPath = self.currentPath + name + '/'
            return self.currentPath
        else:
            return self.currentPath

    def help(self):
        return 'ls\ncd <Ruta>\ncreate <Nombre del archivo>\nread <Nombre del archivo>\nwrite <Nombre del archivo> <Texto a escribir>\nrename <Nombre> <Nuevo nombre>\nrm <Nombre>\nmkdir <Nombre>\nrmdir <Nombre>'


def main():
    print('Para ver la lista de comandos escriba -H')
    manejador = filemanager()

    while True:
        comando = input('>')
        argumentos = comando.split(' ')

        if argumentos[0] == 'create':
            print(manejador.create(argumentos[1], argumentos[2]))
        elif argumentos[0] == 'read':
            print(manejador.read(argumentos[1]))
        elif argumentos[0] == 'write':
            print(manejador.write(argumentos[1]), argumentos[2])
        elif argumentos[0] == 'rename':
            print(manejador.rename(argumentos[1], argumentos[2]))
        elif argumentos[0] == 'rm':
            print(manejador.remove(argumentos[1]))
        elif argumentos[0] == 'mkdir':
            print (manejador.createdir(argumentos[1]))
        elif argumentos[0] == 'rmdir':
            print(manejador.rmdir(argumentos[1]))
        elif argumentos[0] == 'ls':
            print(manejador.ls())
        elif argumentos[0] == 'cd':
            print (manejador.cd(argumentos[1]))
        elif argumentos[0] == '-h':
            print(manejador.help())
        else:
            print('No existe el comando')

main()