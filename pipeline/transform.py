import os 
import sys

import json

from collections import namedtuple

from pipeline.schemas import profiles 
from pipeline.schemas import health
from pipeline.schemas import household
from pipeline.schemas import symptoms

from settings import constants

import logs.logging_conf, logging
logger = logging.getLogger("transformer")

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def init_pipeline(data, **kwargs):
    etl_data = []

    demographics_index = constants.ElasticsearchConstants['index']['demographics']
    household_index = constants.ElasticsearchConstants['index']['household']
    health_index = constants.ElasticsearchConstants['index']['health']
    symptoms_index = constants.ElasticsearchConstants['index']['symptoms']

    # Mapping demographics...
    profiles = map_to_schema(data, demographics_index)
    etl_data.extend(categorize_data(profiles, demographics_index))
    
    # Mapping household...
    household = map_to_schema(data, household_index)
    etl_data.extend(categorize_data(household, household_index))

    # Mapping health...
    health = map_to_schema(data, health_index)
    etl_data.extend(categorize_data(health, health_index))

    # Mapping symptoms...
    symptoms = map_to_schema(data, symptoms_index)
    etl_data.extend(categorize_data(symptoms, symptoms_index))

    return etl_data

"""
    MAP_TO_SCHEMA function

    data - raw data
    elastic_schema - name of schema (demographics, health, household, symptoms)
                    recommend that you use the settings.constants under ElasticsearchConstatant['index']

"""
def map_to_schema(data, elastic_schema):
    els_data = []
    raw_data = {}

    if(elastic_schema == constants.ElasticsearchConstants['index']['demographics']):
        raw_data = profiles.Profiles(data)
    elif(elastic_schema == constants.ElasticsearchConstants['index']['household']):
        raw_data = household.Household(data)
    elif(elastic_schema == constants.ElasticsearchConstants['index']['health']):
        raw_data = health.Health(data)
    elif(elastic_schema == constants.ElasticsearchConstants['index']['symptoms']):
        raw_data = symptoms.Symptoms(data)

    els_data = raw_data.map_extracted()
    return els_data

"""
    CATEGORIZE_DATA function
    data - data filtered from map_to_schema function
    elastic_schema - name of schema (demographics, health, household, symptoms)
                    recommend that you use the settings.constants under ElasticsearchConstatant['index']
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
            python_callable=map_to_schema)
