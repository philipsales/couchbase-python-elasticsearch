import os 
import sys
import logs
import json
import pprint 

import lib.logs.logging_conf, logging
logger = logging.getLogger("file_handler.py")

class FileHandler:
    FILE_TYPE = ".csv"
    FILE_DIR = "data/output/"

    @staticmethod
    def fwrite_encode(content, **kwargs):
        logger.info('--------')
        logger.info(content)

        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))  

        file_path = "data/tmp/" + 'kobo' + '.avro'
        f = open(file_path, 'w')
        f.write(str(content))
        f.close()

    @staticmethod
    def fwrite_encode_avro(content, **kwargs):
        logger.info('--------')
        logger.info(content)

        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))  

        file_path = "data/tmp/" + 'kobo' + '.avro'
        f = open(file_path, 'w')
        f.write(str(content))
        f.close()
        
    @staticmethod
    def fwrite(content, filename=""):
        
        file_path = FileHandler.FILE_DIR + filename + FileHandler.FILE_TYPE
        f = open(file_path, 'w')
        f.write(content) 
        f.close()

    @staticmethod
    def fappend(content, filename=""):
        file_path = FileHandler.FILE_DIR + filename + FileHandler.FILE_TYPE
        f = open(file_path, 'a')
        line = '\n' + str(content) 
        f.write(line) 
        f.close()