from sys import argv
from src.utils.say_my_name import sayMyName
from src.utils.logger import setup_logger

class IOManager():
    logger = setup_logger()
    logger.info("Hi info msg")
    logger.debug("Hi debug msg")
    
    def __init__(self):
        print("IOManager started")
    
    
# if __name__ == "__main__":
#     main()