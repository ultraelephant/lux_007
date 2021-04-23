import os
import pytest

from config import basepath
from filesvc import createfile
from filesvc import deletefile
from filesvc import readfile
from filesvc import getfilemeta

filename = 'testfile'
filenamepath = basepath + filename

def test_createfile():
    createfile(filenamepath)
    with open(filenamepath, 'r') as fp:
        assert fp.read() == ''

def test_readfile():
    assert readfile(filenamepath) == ''

def test_getfilemeta():
    attrs = ['st_mode', 'st_ino', 'st_dev', 'st_nlink', 'st_uid', 'st_gid', 'st_size', 'st_atime', 'st_mtime', 'st_ctime']
    for attr in attrs:
        if attr in dir(getfilemeta(filenamepath)):
            pass
        else:
            pytest.fail('Missing {}'.format(attr))

def test_deletefile():
    deletefile(filenamepath)
    assert os.path.isfile(filenamepath) == False