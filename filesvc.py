import os

def createfile(path):
    if not os.path.exists(path):
        with open (path, "w"):
            pass
    else:
        raise Exception('File exist')

def deletefile(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        raise Exception('File not exist')

def readfile(path):
    if os.path.isfile(path):
        f = open(path)
        filer = f.read()
        f.close()
        return (filer)
    else:
        raise Exception('File not exist')

def getfilemeta(path):
    if os.path.isfile(path):
        meta = os.stat(path)
        return (meta)
    else:
        raise Exception('File not exist')