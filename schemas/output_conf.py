from schemas.output.elastic import demographics as demographics
from schemas.output.elastic import health as health
from schemas.output.elastic import household as household
from schemas.output.elastic import symptoms as symptoms

from schemas.output.old_curis import old_curis as old_curis

output_schemas = {
    'old_curis': {
        'demographics': demographics.demographics_schema,
        'household': household.household_schema,
        'health': health.health_schema,
        'symptoms': symptoms.symptoms_schema
    },
    'kobo': {
        'old_curis': old_curis.old_curis_schema
    }
}