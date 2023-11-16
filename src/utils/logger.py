import logging

def setup_logger():
    logging.basicConfig(
        # level=logging.DEBUG,
        level=logging.CRITICAL,
        format='%(asctime)s [%(levelname)s]: %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S'
    )