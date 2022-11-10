import sys
import os
import zlib
import hashlib

def md5(filename, chunksize):
    m = hashlib.md5()
    with open(filename, 'rb') as f:
        while chunk := f.read(chunksize):
            m.update(chunk)
    return m.hexdigest()

def cat_file(sha_1):
   
    sub_dir = sha_1[0:2]
    check_sum = sha_1[2:]

    os.chdir(f".git/objects/{sub_dir}")
    blob = open(f'{check_sum}', 'rb')

    bytext = zlib.decompress(blob.read())
    blob_header_ending_index = bytext.find(b'\x00') 
    text = bytext[blob_header_ending_index + 1:].decode('utf-8')
    print(text, end = '')

   
def hash_object(option, to_hash_file):

    blob = open(f'{to_hash_file}', 'rb')
    byte_text = blob.read()
    
    header = f'blob {len(byte_text)}'+'\x00'
    header = header.encode("utf-8")
    
    to_hash = header+byte_text
    hash_object = hashlib.sha1(to_hash)
    pbHash = hash_object.hexdigest()

    os.chdir(".git/objects")
    os.mkdir(f"{pbHash[:2]}")
    
    os.chdir(f"{pbHash[:2]}")
    with open(f"{pbHash[2:]}", "wb") as f:
        
        zipped = bytes(zlib.compress(to_hash))
        f.write(zipped)

    print(pbHash, end='')    

def ls_tree(hashed):
    n = b'\x00'
    s = b' '
    
    blob = open(hashed, 'rb') 
    bytext = zlib.decompress(blob.read())
    hashed = bytext + n 
    
    folder = []
    reg_file = []

    hashed = hashed[hashed.find(n) + 1:]
    while(True):
        d_idx = hashed.find(b'40000')
        if(d_idx != -1):
            n_idx = hashed.find(n)
            folder_name = hashed[d_idx + 6 : n_idx].decode('utf-8')
            hashed = hashed[n_idx + 1]
            folder.append(folder_name)
        else:
            break
    
    while(hashed.find(n) != (len(hahsed) - 1)):
        s_idx = hashed.find(s)
        n_idx = hashed.find(n)
        file_name = hashed[s_idx + 1: n_idx].decode('utf-8')
        reg_file.append(file_name)
        hashed = hashed[n_idx + 1:]
     
    sorted(folder)
    sorted(reg_file)
    
    folder.extend(reg_file)
    for obj in folder:
        print(obj)

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    
    command = sys.argv[1]
    option = sys.argv[2]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")

    elif command == "cat-file":
        cat_file(sys.argv[3])

    elif command == "hash-object":
        hash_object(sys.argv[2], sys.argv[3])    
        
        
        
    elif command == "ls-tree" and option == "--name-only":
        hashed = sys.argv[3]
        ls_tree(hashed):   

if __name__ == "__main__":
    main()
