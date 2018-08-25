import sys
import datetime

# from pipeline import couchbase_n1ql

def write_to_log(string, filename):
    file = open("logs/log_files/" + filename + "_log.txt", "a")
    file.write(string)
    file.close()

def _get_last_batch_log(filename):
    try:
        fileHandle = open("logs/log_files/" + filename + "_log.txt", "r")
        lineList = fileHandle.readlines()
        fileHandle.close()

        theDate = get_date_from_string(lineList[-1], "<", ">")
        theDate = theDate[:-16]
    
    except FileNotFoundError:
        theDate = _get_date_yesterday()

    return theDate

def get_date_from_string(string, first, last):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except ValueError:
        return ""

def _get_date_yesterday():
    d = datetime.datetime.utcnow()
    month = '{:02d}'.format(d.month)
    day = '{:02d}'.format(d.day)
    year = '{:02d}'.format(d.year)

    day = int(day) - 1

    return year + "-" + month + "-" + str(day)