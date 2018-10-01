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

household = [
	{
        "key_from": "cb_id",
        "key_to": "awh_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.no_of_families_in_the_household",
        "key_to": "families_in_household",
        "default_value": 0,
        "type":"integer",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.no_of_people_in_the_household",
        "key_to": "people_in_household",
        "default_value": 0,
        "type":"integer",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.house_ownership",
        "key_to": "type_of_accommodation",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.type_of_house",
        "key_to": "construction",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.neighborhood_description",
        "key_to": "type_of_neighbourhood",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.amenities_present_in_house",
        "key_to": "utilities",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.sanitary_type",
        "key_to": "type_of_sanitation",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "households.sanitary_ownership",
        "key_to": "sanitation_ownerships",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "organization",
        "key_to": "org",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "",
        "key_to": "number",
        "default_value": 1,
        "type":"integer",
        "parent_key_name":"version",
        "to_compute": False,
        "fields_for_computation": []
        },
        {
        "key_from": "",
        "key_to": "date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"version",
        "to_compute": False,
        "fields_for_computation": []
        },
        {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'households.water_sources',
        'key_to': 'water_sources',
        'parent_key_name': '',
        'to_compute': False,
        'type': 'array'
        },
        {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'households.how_ensure_water_safe',
        'key_to': 'how_u_ensure_water_safe',
        'parent_key_name': '',
        'to_compute': False,
        'type': 'array'
        },
        {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'households.what_u_se_to_wash_hands',
        'key_to': 'what_do_u_use_to_wash_hands',
        'parent_key_name': '',
        'to_compute': False,
        'type': 'string'
        }
]