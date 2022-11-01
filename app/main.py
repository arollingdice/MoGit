import sys
import os
import zlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

     #Uncomment this block to pass the first stage
    
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
        print(zlib.decompress(blob.read()), end='') 

if __name__ == "__main__":
    main()
