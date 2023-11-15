from sys import argv
from io_manager import IOManager

def main():
    ioObj = IOManager()
    ioObj.read_file(argv[1])
    
if __name__ == "__main__":
    main()