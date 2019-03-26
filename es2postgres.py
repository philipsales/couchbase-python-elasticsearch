import os 
import sys
import logs
import json
import pprint
import datetime as dt

from settings.base_conf import ELASTICSEARCH, COUCHBASE
from settings.base_conf import elastic_config, couchbase_config 

from pipeline.extract import couchbase_n1ql, couchbase_sync, elastic, kobo, sqlite

from pipeline.transform import transformer, flattener
from lib.utility.file_handler import FileHandler
from lib.utility.csv_builder import CSVBuilder 

PHILIPPINES = 'philippines'
CAMBODIA = 'cambodia'


def get_input_schema():
    pass

def get_output_schema():
    pass

def map_input2output_schema():
    pass

def clean_data():
    pass

def dump_data():
    pass

def flatten_elastic_properties(es_data):
    properties = []
    
    for k, v in es_data.items():
        if k == 'hits':
            for key in v['hits']:
                item = {}
                item = flattener.flattenDict(key['_source'])
                properties.append(item)

    return properties 

def transform_data(es_data):
    return flatten_elastic_properties(es_data)

def export_csv(es_data, index):
    flatten_data = transform_data(es_data)

    fH = FileHandler()

    header = CSVBuilder.set_header(flatten_data)
    fH.fwrite(header, index)

    body = CSVBuilder.set_body(flatten_data)
    for item in body:
        fH.fappend(item, index)

def get_source_data(index):
    return elastic.get_data(index)

def transform(indeces):
    #TODO: optimize if 1M records transposition
    for es_index in indeces:
        es_data = get_source_data(es_index)
        trans_data = export_csv(es_data, es_index)

def init_index(country):
    new_index = []
    old_indeces = ELASTICSEARCH['index']

    for index in old_indeces:
        new_index.append(country + '_' + index)
    
    return new_index

def elastic_to_postgres():
    indeces = init_index(CAMBODIA)
    transform(indeces)

#run as standalone package
if __name__ == '__main__':
    elastic_to_postgres()
