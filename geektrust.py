from sys import argv
from io_manager import IOManager

def lineProcessorFn(singleLine):
    pass

def main():
    ioObj = IOManager()
    ioObj.read_file(argv[1],lineProcessorFn)
    pass
    
if __name__ == "__main__":
    main()