#!/bin/bash

source /virtual_env/awhdatapipeline_env/bin/activate

cd ~/src/data-pipeline

python main.py

wait

deactivate