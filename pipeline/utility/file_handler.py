import os 
import sys
import logs
import json
import pprint 

class FileHandler:
    file_type = ".csv"
    file_dir = "data/output/"
        
    @staticmethod
    def fwrite(content, filename=""):
        file_path = FileHandler.file_dir + filename + FileHandler.file_type
        f = open(file_path, 'w')
        f.write(content) 
        f.close()

    @staticmethod
    def fappend(content, filename=""):
        file_path = FileHandler.file_dir + filename + FileHandler.file_type
        f = open(file_path, 'a')
        line = '\n' + str(content) 
        f.write(line) 
        f.close()