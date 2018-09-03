import sys
from pipeline.computation import bmi

computations = {
    "bmi" : "bmi.BMI"
}

def _execute_computation(params, fn):
    getattr(computations[fn](), "_do_computations")
    