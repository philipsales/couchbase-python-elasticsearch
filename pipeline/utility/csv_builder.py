import os 
import sys
import json
import pprint 

class CSVBuilder:
        
    @staticmethod
    def set_header(header):
        csv_header = ''

        for v in header:
            csv_header = "|".join(str(x) for x in list(v.keys()))
            break

        return csv_header

    @staticmethod
    def set_body(body):
        csv_body = []

        for v in body:
            csv_body.append("|".join(str(x) for x in list(v.values())))

        return csv_body
