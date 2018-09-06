import sys
from pipeline.computation import utilities

#TODO: Add new function names here if there are new computations
computations = {
    "bmi" : "bmi",
    "organization" : "organization"
}

def _execute_computation(params, fn):
    utility = utilities.Computations(params)
    return getattr(utility, computations[fn])()
    