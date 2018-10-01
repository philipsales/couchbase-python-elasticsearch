from schemas.input.kobo import personal_info_522 as personal_info
from schemas.input.old_curis import old_curis as old_curis

input_schemas = {
    'kobo': personal_info.personal_info_schema,
    'old_curis': old_curis.old_curis_schema
}