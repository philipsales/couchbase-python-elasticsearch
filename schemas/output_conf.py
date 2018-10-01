from schemas.output.elastic import demographics as demographics
from schemas.output.elastic import health as health
from schemas.output.elastic import household as household
from schemas.output.elastic import symptoms as symptoms
from schemas.output.elastic import child_health as child_health
from schemas.output.elastic import fam_planning_maternal as fam_planning_maternal
from schemas.output.elastic import dental_health as dental_health

from schemas.output.old_curis import old_curis_522 as old_curis

output_schemas = {
    'old_curis': {
        'demographics': demographics.demographics_schema,
        'household': household.household_schema,
        'health': health.health_schema,
        'symptoms': symptoms.symptoms_schema,
        'child_health': child_health.child_health_schema,
        'family_planning_and_maternal_health' : fam_planning_maternal.family_planning_schema,
        'dental_health': dental_health.dental_health_schema
    },
    'kobo': {
        'old_curis': old_curis.old_curis_schema
    }
}