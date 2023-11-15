import logging

def setup_logger():
    # Configure the logging module
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s]: %(message)s', 
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Create a logger instance
    logger = logging.getLogger(__name__)
    return logger