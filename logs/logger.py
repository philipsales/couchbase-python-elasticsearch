import sys
import datetime

def write_to_log(string, filename):
    file = open("logs/log_files/" + filename + "_log.txt", "a")
    file.write(string)
    file.close()

def get_last_batch_log(filename):
    fileHandle = open("logs/log_files/" + filename + "_log.txt", "r")
    lineList = fileHandle.readlines()
    fileHandle.close()

    theDate = __get_date_from_string(lineList[-1], "<", ">")
    theDate = theDate[:-16]

    return theDate

def __get_date_from_string(string, first, last):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except ValueError:
        return ""