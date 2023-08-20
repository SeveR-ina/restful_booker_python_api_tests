import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to INFO or DEBUG as needed
        format='%(asctime)s [%(levelname)s] - %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
