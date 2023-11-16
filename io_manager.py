from sys import argv
from main_handler import MainHandler
from src.utils.logger import setup_logger
import logging
logger = logging.getLogger(__name__)

class IOManager():
    def __init__(self):
        self._main_handler = MainHandler()
        setup_logger()
  
    def read_file(self,file_path):
        with open(file_path, 'r') as file:
            for input_line in file:
                input_line = input_line.replace("\n", '')
                self._main_handler.process_one_line(input_line)