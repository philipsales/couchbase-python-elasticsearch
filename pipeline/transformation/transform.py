import os 
import sys
import json
import datetime as dt

from pipeline.transformation import extractor

from pipeline.auxiliary import sqlite_checker
from pipeline.auxiliary import getter

from pipeline.connection import sqlite

from schemas.mapping_conf import oldcuris2elastic_extractor
from schemas.mapping_conf import kobo2oldcuris_extractor

from settings.base_conf import ELASTICSEARCH
from settings.base_conf import sqlite_conf

import logs.logging_conf, logging
logger = logging.getLogger("transformer")

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

sqlite_conn = sqlite_conf.SQLiteConfig[sqlite_conf.SQLiteENV]

SQLITE_CONN = sqlite_conn['PATH']
OLD_CURIS = 'old_curis'
KOBO = 'kobo'
DEMOGRAPHICS_INDEX = ELASTICSEARCH['index']['demographics']
HOUSEHOLD_INDEX = ELASTICSEARCH['index']['household']
HEALTH_INDEX = ELASTICSEARCH['index']['health']
SYMPTOMS_INDEX = ELASTICSEARCH['index']['symptoms']
CHILD_HEALTH_INDEX = ELASTICSEARCH['index']['child_health']
FAMILY_PLANNING_MATERNAL_HEALTH_INDEX = ELASTICSEARCH['index']['family_planning_and_maternal_health']
DENTAL_HEALTH = ELASTICSEARCH['index']['dental_health']

def oldcuris2elastic(data, **kwargs):
    etl_data = []

    demographics = _transform(OLD_CURIS, DEMOGRAPHICS_INDEX, 
        data, oldcuris2elastic_extractor.demographics)
    
    household = _transform(OLD_CURIS, HOUSEHOLD_INDEX, 
        data, oldcuris2elastic_extractor.household)
    
    health = _transform(OLD_CURIS, HEALTH_INDEX, 
        data, oldcuris2elastic_extractor.health)

    symptoms = _transform(OLD_CURIS, SYMPTOMS_INDEX, 
        data, oldcuris2elastic_extractor.symptoms)

    child_health = _transform(OLD_CURIS, CHILD_HEALTH_INDEX, 
        data, oldcuris2elastic_extractor.child_health)

    family_planning_maternal_health = _transform(OLD_CURIS, 
        FAMILY_PLANNING_MATERNAL_HEALTH_INDEX, 
        data, oldcuris2elastic_extractor.family_planning_maternal_health)
    
    dental_health = _transform(OLD_CURIS, DENTAL_HEALTH, 
        data, oldcuris2elastic_extractor.dental_health)
    
    child_health_tuple = (child_health, CHILD_HEALTH_INDEX)
    demographics_tuple = (demographics, DEMOGRAPHICS_INDEX)
    household_tuple = (household, HOUSEHOLD_INDEX)
    health_tuple = (health, HEALTH_INDEX)
    symptoms_tuple = (symptoms, SYMPTOMS_INDEX)
    fpmh_tuple = (family_planning_maternal_health, FAMILY_PLANNING_MATERNAL_HEALTH_INDEX)
    dental_health_tuple = (dental_health, DENTAL_HEALTH)

    group_tuple = (demographics_tuple, household_tuple, health_tuple, 
        symptoms_tuple, child_health_tuple,fpmh_tuple, dental_health_tuple)
    

    etl_data.extend(_load_data(group_tuple))

    return etl_data

def kobo2oldcuris(data, **kwargs):
    couchbase_data = []

    mapped_json = _transform(KOBO, OLD_CURIS, 
        data, kobo2oldcuris_extractor.personal_informations)

    couchbase_data.extend(mapped_json)

    conn = sqlite.create_connection(SQLITE_CONN) 
    sqlite.create_table(conn) 
    sqlite_checker.update_rev_ids(conn)
    print(couchbase_data)
    sqlite_data = sqlite_checker.segregate_ids(conn,couchbase_data)

    return sqlite_data

"""
    CATEGORIZE_DATA function
    
    @params
    data - data filtered from map_to_schema function
    elastic_schema - name of schema (demographics, health, household, symptoms)
                    recommend that you use the settings.base_conf 
                    under ElasticsearchConstatant['index']
"""
def _categorize_data(data,elastic_schema):
    etl_data = []

    for row in data:
        tmp ={}
        tmp[elastic_schema] = json.loads(row)
        etl_data.append(tmp)

    return etl_data

def _transform(source_project, specific_schema, raw_data, extract_settings):
    input_schema = getter.get_input_schema(source_project, 
                extract_settings['json_structure'])
    output_schema = getter.get_output_schema(source_project, specific_schema)

    extracted_data = extractor.extract_from_input(raw_data, extract_settings, 
                    input_schema)

    transformed_data = extractor.transform(extracted_data, extract_settings, 
                    output_schema)

    return transformed_data

def _load_data(data_tuple):
	etl_data = []

	for i in data_tuple:
		etl_data.extend(_categorize_data(i[0], i[1]))

	return etl_data

#run as standalone module
if __name__ == "__main__":
    pass

#run as workflow 
default_args = {
    'owner': 'ELKadmin',
    'start_date': dt.datetime(2017, 6, 1)
}

with DAG(dag_id='subdg_transform',
    default_args=default_args,
    schedule_interval='0 1 * * *',
    ) as dag:

    task_map_to_schema = PythonOperator(task_id='task_map_to_schema', 
            python_callable=extractor.transform)
