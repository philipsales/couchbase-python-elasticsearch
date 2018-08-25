#!/bin/bash

cd /virtual_env/awhdatapipeline

source bin/activate

cd /data-pipeline

python main.py

wait

deactivate