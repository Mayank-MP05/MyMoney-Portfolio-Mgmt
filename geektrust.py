from sys import argv
from src.utils.say_my_name import sayMyName

def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    sayMyName()
    
if __name__ == "__main__":
    main()