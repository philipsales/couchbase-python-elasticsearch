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

demographics = [
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
        "key_to": "active",
        "default_value": True,
        "type":"boolean",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "gender",
        "key_to": "sex",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "birthdate",
        "key_to": "birth_date",
        "default_value": "unknown",
        "type":"date",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "is_dead",
        "default_value": False,
        "type":"boolean",
        "parent_key_name":"deceased",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "year",
        "default_value": None,
        "type":"date",
        "parent_key_name":"deceased",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "add_date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "address.barangay",
        "key_to": "commnty",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "address.province",
        "key_to": "province",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
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
        "key_from": "profiles.civil_status",
        "key_to": "civil_st",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.religion",
        "key_to": "religion",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.education",
        "key_to": "educ",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.employment.is_employed",
        "key_to": "is_empl",
        "default_value": "",
        "type":"string",
        "parent_key_name":"employed",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.employment.monthly_income",
        "key_to": "m_income",
        "default_value": 0.0,
        "type":"string",
        "parent_key_name":"employed",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.employment.nature",
        "key_to": "nature",
        "default_value": "",
        "type":"string",
        "parent_key_name":"employed",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.employment.currency",
        "key_to": "currency",
        "default_value": "",
        "type":"string",
        "parent_key_name":"employed",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.are_you_currently_earning",
        "key_to": "are_you_currently_earning",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "profiles.where_income_from",
        "key_to": "where_income_from",
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
    }
]