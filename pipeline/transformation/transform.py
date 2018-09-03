import os 
import sys
import json
import datetime as dt

from pipeline.transformation import extractor

from schemas.mapping import oldcuris2elastic_extractor
from schemas.mapping import kobo2oldcuris_extractor

from settings.base_conf import ELASTICSEARCH_CONSTANTS

import logs.logging_conf, logging
logger = logging.getLogger("transformer")

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def oldcuris2elastic(data, **kwargs):
    etl_data = []

    demographics_index = ELASTICSEARCH_CONSTANTS['index']['demographics']
    household_index = ELASTICSEARCH_CONSTANTS['index']['household']
    health_index = ELASTICSEARCH_CONSTANTS['index']['health']
    symptoms_index = ELASTICSEARCH_CONSTANTS['index']['symptoms']

    # Mapping demographics...
    profiles = extractor.map_to_output(data, oldcuris2elastic_extractor.demographics)
    etl_data.extend(categorize_data(profiles, demographics_index))
    
    # # Mapping household...
    household = extractor.map_to_output(data, oldcuris2elastic_extractor.household)
    etl_data.extend(categorize_data(household, household_index))

    # # Mapping health...
    health = extractor.map_to_output(data, oldcuris2elastic_extractor.health)
    etl_data.extend(categorize_data(health, health_index))

    # # Mapping symptoms...
    symptoms = extractor.map_to_output(data, oldcuris2elastic_extractor.symptoms)
    etl_data.extend(categorize_data(symptoms, symptoms_index))

    return etl_data

def kobo2oldcuris(data, **kwargs):
    couchbase_data = []

    mapped_json = extractor.map_to_output(data, kobo2oldcuris_extractor.personal_informations)
    couchbase_data.extend(mapped_json)

    return couchbase_data

"""
    CATEGORIZE_DATA function
    data - data filtered from map_to_schema function
    elastic_schema - name of schema (demographics, health, household, symptoms)
                    recommend that you use the settings.base_conf under ElasticsearchConstatant['index']
"""
def categorize_data(data,elastic_schema):
    etl_data = []

    for row in data:
        tmp ={}
        tmp[elastic_schema] = json.loads(row)
        etl_data.append(tmp)

    return etl_data

#run as standalone module
if __name__ == "__main__":
    init_pipeline(data)

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
            python_callable=extractor.map_to_output)
