import sys
import os.path
import datetime

root_url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def write_to_log(string, filename):
    file = open(root_url + "/logs/" + filename + "_log.txt", "a")
    file.write(string)
    file.close()
    
def get_last_batch_log(filename):
    fileHandle = open(root_url+ "/logs/" + filename + "_log.txt", "r")
    lineList = fileHandle.readlines()
    fileHandle.close()

    try:
        theDate = _get_date_from_string(lineList[-1], "<", ">")
        theDate = theDate[:-16]
    except:
        theDate = None

    return theDate

def _get_date_from_string(string, first, last):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except ValueError:
        return ""