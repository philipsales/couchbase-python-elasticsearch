import os 
import sys
import json

def flattenDict(d, result=None):
    if result is None:
        result = {}
    for key in d:
        value = d[key]
        if isinstance(value, str):
            if "\n" in value:
                print('----------------',value) 
                value = value.replace("\n", ' and ')
                print('----------------',value) 

        if isinstance(value, dict):
        #if d['type'] =='object':
            value1 = {}
            for keyIn in value:
                value1[".".join([key,keyIn])]=value[keyIn]
            flattenDict(value1, result)
        elif isinstance(value, (list, tuple)):   
            for indexB, element in enumerate(value):
                if isinstance(element, dict):
                    value1 = {}
                    index = 0
                    for keyIn in element:
                        newkey = ".".join([key,keyIn])        
                        value1[".".join([key,keyIn])]=value[indexB][keyIn]
                        index += 1
                    for keyA in value1:
                        flattenDict(value1, result)   
        else:
            result[key]=value
    return result
