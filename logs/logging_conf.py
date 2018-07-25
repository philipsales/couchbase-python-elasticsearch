import logging.config
from logging import FileHandler, StreamHandler
import os.path

#LOGS Configuration
default_formatter = logging.Formatter(\
           "%(asctime)s:%(levelname)s:%(message)s")

console_handler = StreamHandler()
console_handler.setFormatter(default_formatter)

error_handler = FileHandler("error.log", "a")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(default_formatter)

root = logging.getLogger()
root.addHandler(console_handler)
root.addHandler(error_handler)
root.setLevel(logging.DEBUG)

def main():
    LOGGING_CONF=os.path.join(os.path.dirname(__file__), "logging.ini")
    logging.config.fileConfig(LOGGING_CONF)

if __name__ == '__main__':
    main()


