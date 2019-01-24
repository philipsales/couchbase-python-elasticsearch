import sys
from pipeline.computation import utilities

#TODO: Add new function names here if there are new computations
computations = {
    "bmi" : "bmi",
    "organization" : "organization",
    "poor_risk_score": "poor_risk_score",
    "risk_score_ncd_general": "risk_score_ncd_general",
    "risk_score_child_health": "risk_score_child_health"
}

def compute(params, fn):
    utility = utilities.Computations(params)
    return getattr(utility, computations[fn])()
    