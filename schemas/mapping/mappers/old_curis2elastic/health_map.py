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

health = [
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
        "key_from": "",
        "key_to": "bmi",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": True,
        "fields_for_computation": ["health_informations.height","health_informations.weight"]
	},
	{
        "key_from": "health_informations.blood_type",
        "key_to": "blood_group",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_sign",
        "key_to": "blood_rhesus",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.allergies",
        "key_to": "allergies",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_pressure.first_reading.systole",
        "key_to": "systole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.first",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_pressure.first_reading.diastole",
        "key_to": "diastole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.first",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_pressure.second_reading.systole",
        "key_to": "systole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.second",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_pressure.second_reading.diastole",
        "key_to": "diastole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.second",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_pressure.third_reading.systole",
        "key_to": "systole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.third",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_pressure.third_reading.diastole",
        "key_to": "diastole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.third",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_sugar",
        "key_to": "blood_sugar",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.smoking_habit",
        "key_to": "smoking_habit",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.blood_sugar",
        "key_to": "blood_sugar",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.fruits_in_a_week",
        "key_to": "fruits_in_a_week",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.vegetables_in_a_week",
        "key_to": "vegetables_in_a_week",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.exercise_in_a_week",
        "key_to": "exercise_in_a_week",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.family_history",
        "key_to": "family_history",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.diagnosed",
        "key_to": "diagnosed",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.medical_equipments",
        "key_to": "medical_equipments",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.high_cost_medicine",
        "key_to": "high_cost_medicine",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "health_informations.maintenance_drugs",
        "key_to": "maintenance_drugs",
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
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.times_exposed_to_smoke',
                'key_to': 'times_exposed_to_smoke',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.times_exposed_to_smoke',
                'key_to': 'how_travel_for_long_term_meds',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.do_u_have_disability',
                'key_to': 'do_u_have_disability',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.alcohol_in_a_week',
                'key_to': 'alcohol_in_a_week',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.traditional_medicine',
                'key_to': 'traditional_medicine',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.taking_long_term_medication',
                'key_to': 'taking_long_term_medication',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.why_take_or_not_prescribed_dose',
                'key_to': 'why_take_or_not_prescribed_dose',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'health_informations.do_u_have_health_insurance_plan',
                'key_to': 'do_u_have_health_insurance_plan',
                'parent_key_name': 'health_informations',
                'to_compute': False,
                'type': 'string'
        }
]