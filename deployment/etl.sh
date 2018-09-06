#!/bin/bash

cd /virtualenv/awhdatapipeline

source bin/activate

cd ~/data-pipeline

python main.py

wait

deactivate