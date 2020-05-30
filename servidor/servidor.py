import os
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


def create(currentPath, name):
    try:
        newfile = open(currentPath + name, 'w+')  # write-read
        newfile.close()
        return 'Archivo creado'
    except (OSError, IOError):
        print('No se pudo crear "' + currentPath + name + '" Revise que el nombre sea válido')


def read(currentPath, name):
    try:
        openfile = open(currentPath + name, 'r')  # read
        content = openfile.read()
        return content
    except (OSError, IOError):
        #print(currentPath)
        return 'No se pudo abrir "' + currentPath + name + '" Revise que el nombre sea correcto'


def write(currentPath, name, content):
    try:
        openfile = open(currentPath + name, 'a')  # append
        openfile.write('\n' + content)
        return 'Añadido al archivo'
    except (OSError, IOError):
        return 'No se pudo abrir "' + currentPath + name + '" Revise que el nombre sea correcto'


def rename(currentPath, name, newname):
    try:
        os.rename(currentPath + name, currentPath.append(newname)) # Rename
        return 'Archivo renombrado'
    except (OSError, IOError):
        return 'No se pudo abrir "' + currentPath + name + '" Revise que el nombre sea correcto'


def remove(currentPath, name):
    try:
        os.remove(currentPath + name)
        return 'Archivo eliminado'
    except (OSError, IOError):
        return 'No se encontró "' + currentPath + name + '" Revise que el nombre sea correcto'


def rmdir(currentPath, name):
    try:
        #shutil.rmtree(currentPath + name) # Borra carpeta y sus contenidos
        os.rmdir(currentPath + name)
        return 'Carpeta eliminada'
    except (OSError, IOError):
        return 'No se encontró "' + currentPath + name + '" Revise que el nombre sea correcto y la carpeta esté vacía'


def createdir(currentPath, name):
    try:
        os.makedirs(currentPath + name)
        return currentPath
    except (OSError, IOError):
        return 'No se pudo crear "' + currentPath + name + '" Revise que el nombre de la carpeta no exista'


def ls(currentPath):
    try:
        lista = '\n'.join(i for i in os.listdir(currentPath))
        return lista
    except (OSError, IOError):
        return 'Hubo un error que no debería existir'


def cd(currentPath, name):
    if name == '..':
        dirs = currentPath.split('/')
        if len(dirs) == 2:
            return currentPath
        else:
            dirs.pop()
            dirs.pop()
            currentPath = '/'.join(dirs) + '/'
            return currentPath
    if name[0] == '/':
        currentPath = 'home/'
        return currentPath

    if os.path.exists(currentPath + name):
        currentPath = currentPath + name + '/'
        return currentPath
    else:
        return currentPath

def help():
    return 'ls\ncd <Ruta>\ncreate <Nombre del archivo>\nread <Nombre del archivo>\nwrite <Nombre del archivo> <Texto a escribir>\nrename <Nombre> <Nuevo nombre>\nrm <Nombre>\nmkdir <Nombre>\nrmdir <Nombre>'

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/mis_archivos',)


with SimpleXMLRPCServer(('192.168.1.76', 8000), requestHandler=RequestHandler) as server:
    server.register_function(create)
    server.register_function(read)
    server.register_function(write)
    server.register_function(rename)
    server.register_function(remove)
    server.register_function(rmdir)
    server.register_function(createdir)
    server.register_function(ls)
    server.register_function(cd)
    server.register_function(help)

    server.serve_forever()
