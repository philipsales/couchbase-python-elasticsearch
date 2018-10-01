import sys
import datetime

"""

key_from - key of the json attribute to be mapped to new document
key_to - key of the new document where the value of the 'key_from' will be assigned. (leaves part of the tree)
default_value - default value of the 'key_to' field
type - date type of the value of 'key_to'
parent_key_name - parent of json attribute where it belongs and will create dept (i.e. barangay is under address)
                If you want to create further dept, add the another dept with period(.) delimeter (i.e. blood_pressure.first)
to_compute - a boolean that determines whether the field needs computation
fields_for_computation - if to_compute is True, make sure that you include the fields needed for computation here

"""

dental_health = [
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'cb_id',
        'key_to': 'awh_id',
        'parent_key_name': '',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'organization',
        'key_to': 'org',
        'parent_key_name': '',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'dental_health.do_you_own_toothbrush',
        'key_to': 'do_you_own_toothbrush',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'dental_health.times_clean_teeth_daily',
        'key_to': 'times_clean_teeth_daily',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': "",
        'fields_for_computation': [],
        'key_from': 'dental_health.family_members_d_problems_last_6_months',
        'key_to': 'family_members_d_problems_last_6_months',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': "",
        'fields_for_computation': [],
        'key_from': 'dental_health.what_do_u_use_to_clean_teeth',
        'key_to': 'what_do_u_use_to_clean_teeth',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 1,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'number',
        'parent_key_name': 'version',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date',
        'parent_key_name': 'version',
        'to_compute': False,
        'type': 'string'
    }
]