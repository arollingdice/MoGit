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

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized git directory")
    elif command == "cat-file":

        option = sys.argv[2]
        sha_1 = sys.argv[3]
        sub_dir = sha_1[0:2]
        check_sum = sha_1[2:]
    
        os.chdir(f".git/objects/{sub_dir}")
        blob = open(f'{check_sum}', 'rb')
        #print( end='') 
        bytext = zlib.decompress(blob.read())
        blob_header_ending_index = bytext.find(b'\x00') 
        text = bytext[blob_header_ending_index + 1:].decode('utf-8')
        print(text, end = '')

    elif command == "hash-object":
        
        option = sys.argv[2]
        to_hash_file = sys.argv[3]
        
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
        
if __name__ == "__main__":
    main()
