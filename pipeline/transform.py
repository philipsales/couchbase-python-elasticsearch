import os 
import sys

import json

from collections import namedtuple

from pipeline.schemas import profiles 
from pipeline.schemas import health
from pipeline.schemas import household
from pipeline.schemas import symptoms

import logs.logging_conf, logging
logger = logging.getLogger("transformer")

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def init_pipeline(data, **kwargs):
    etl_data = []

    # profiles = map_profile(data)
    # for row in profiles:
    #     tmp ={}
    #     tmp['demographics'] = json.loads(row)
    #     etl_data.append(tmp)

    # household = map_household(data)
    # for row in household:
    #     tmp ={}
    #     tmp['household'] = json.loads(row)
    #     etl_data.append(tmp)

    # health = map_health(data)
    # for row in health:
    #     tmp ={}
    #     tmp['health'] = json.loads(row)
    #     etl_data.append(tmp)
    
    symptoms = map_symptoms(data)
    for row in symptoms:
        tmp ={}
        tmp['symptoms'] = json.loads(row)
        etl_data.append(tmp)

    return etl_data 

def map_symptoms(data):
    els_data = []
    symptom = {}

    symptom = symptoms.Symptoms(data)
    els_data = symptom.map_extracted()

    return els_data 

def map_health(data):
    els_data = []
    healths = {}

    healths = health.Health(data)
    els_data = healths.map_extracted()
    
    return els_data

def map_profile(data):
    els_data = []
    profile = {}

    profile = profiles.Profiles(data)
    els_data = profile.map_extracted()
    
    return els_data

def map_household(data):
    els_data = []
    households = {}

    households = household.Household(data)
    els_data = households.map_extracted()

    return els_data 

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

    task_map_profile = PythonOperator(task_id='task_map_profile', 
            python_callable=map_profile)

    task_maphealth = PythonOperator(task_id='task_maphealth', 
            python_callable=map_health)

    task_mapsymptoms = PythonOperator(task_id='task_mapsymptoms', 
            python_callable=map_symptoms)
