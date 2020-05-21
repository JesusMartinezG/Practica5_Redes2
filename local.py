import os
import shutil

class filemanager:
    currentPath = 'home/'

    def __init__(self):
        currentPath = 'home/'  # inicia en la raiz del sistema de archivos

    def create(self, name, content):
        newfile = open(self.currentPath + name, 'w+')  # write-read
        newfile.write(content)
        newfile.close()
        return 'Archivo creado'

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

    def removefile(self, name):
        try:
            os.remove()
            return 'Archivo eliminado'
        except (OSError, IOError):
            return 'No se encontró "' + self.currentPath + name + '" Revise que el nombre sea correcto'

    def removedir(self, name):
        try:
            shutil.rmtree(self.currentPath + name) # Borra carpeta y sus contenidos
            return 'Carpeta eliminada'
        except (OSError, IOError):
            return 'No se encontró "' + self.currentPath + name + '" Revise que el nombre sea correcto'

    def createdir(self, name):
        try:
            os.makedirs(self.currentPath + name)
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

        if os.path.exists(self.currentPath + name):
            self.currentPath = self.currentPath + name + '/'
            return self.currentPath
        else:
            return self.currentPath


def main():
    print('Para ver la lista de comandos escriba -H')
    manejador = filemanager()

    while True:
        comando = input('>')
        argumentos = comando.split(' ')

        if argumentos[0] == 'ls':
            print(manejador.ls())
        elif argumentos[0] == 'cd':
            print (manejador.cd(argumentos[1]))

main()