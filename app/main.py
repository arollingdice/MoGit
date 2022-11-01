import sys
import os
import zlib

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

if __name__ == "__main__":
    main()
