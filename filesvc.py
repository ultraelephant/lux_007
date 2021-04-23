"""File functions module."""

import os


def createfile(path):
    """Create file."""
    if not os.path.exists(path):
        with open(path, "w"):
            pass
    else:
        raise Exception('File exist')


def deletefile(path):
    """Delete file."""
    if os.path.isfile(path):
        os.remove(path)
    else:
        raise Exception('File not exist')


def readfile(path):
    """Return file content."""
    if os.path.isfile(path):
        f = open(path)
        filer = f.read()
        f.close()
        return (filer)
    else:
        raise Exception('File not exist')


def getfilemeta(path):
    """Return file metadata tuple."""
    if os.path.isfile(path):
        meta = os.stat(path)
        return (meta)
    else:
        raise Exception('File not exist')
