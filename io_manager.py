from sys import argv
from src.utils.logger import setup_logger
import logging

class IOManager():
    def __init__(self):
        setup_logger()
    
    def read_file(self,file_path, lineProcessorFn):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                logging.info("File content:")
                logging.info(content)
                lineProcessorFn(content)
        except FileNotFoundError:
            logging.error(f"Error: File '{file_path}' not found.")
        except Exception as e:
            logging.error(f"Error: {e}")
        