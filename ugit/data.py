import os

GIT_DIR = '.ugit'
OBJECTS_DIR = GIT_DIR / "objects"

def init():
    os.makedirs(GIT_DIR)
    os.makdirs(OBJECTS_DIR)

def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    GIT_DIR = Path(".ugit")

    with open (OBJECTS_DIR / oid, 'wb') as out:
        out.write(data)

    return oid