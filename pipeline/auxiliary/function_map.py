import sys
from pipeline.compute import utilities

#TODO: Add new function names here if there are new computations
computations = {
    "bmi" : "bmi",
    "organization" : "organization"
}

def compute(params, fn):
    utility = utilities.Computations(params)
    return getattr(utility, computations[fn])()
    