import os
import hashlib
from pathlib import Path

GIT_DIR = Path('.ugit')
OBJECTS_DIR = GIT_DIR / "objects"
NULL = b'\x00'

def init():
    os.makedirs(GIT_DIR)
    os.makedirs(OBJECTS_DIR)

def hash_object(data, type_='blob'):
    obj = type_.encode() + NULL + data
    oid = hashlib.sha1(obj).hexdigest()

    with open (OBJECTS_DIR / oid, 'wb') as out:
        out.write(obj)

    return oid

def get_object(oid, expected='blob'):
    with open (OBJECTS_DIR / oid, 'rb') as f:
        obj = f.read()
    
    type_, _, content = obj.partition(NULL)
    type_ = type_.decode()

    if expected is not None and type_ != expected:
        raise ValuesError(f'Expected {expected}, got {type_}')

    return content