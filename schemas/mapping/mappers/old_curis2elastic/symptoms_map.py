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

symptoms = [
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
        "key_from": "symptoms_collection.head.head",
        "key_to": "head",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.head.eyes",
        "key_to": "eyes",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.head.nose",
        "key_to": "nose",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.head.mouth",
        "key_to": "mouth",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.head.chin_and_jaw",
        "key_to": "chin_jaw",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.neck.neck",
        "key_to": "neck",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.neck.throat",
        "key_to": "throat",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.neck.upperback",
        "key_to": "upperback",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.neck.lowerback",
        "key_to": "lowerback",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.neck.shoulders",
        "key_to": "shoulder",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.chest.chest",
        "key_to": "chest",
        "default_value": [],
        "type":"array",
        "parent_key_name":"chest",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.chest.lungs_and_breathing",
        "key_to": "lungs",
        "default_value": [],
        "type":"array",
        "parent_key_name":"chest",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.arms.upper_arm",
        "key_to": "upper",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.arms.lower_arm",
        "key_to": "lower",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.arms.wrist",
        "key_to": "wrist",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.arms.hand_and_palm",
        "key_to": "hand",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.arms.fingers",
        "key_to": "fingers",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.abdomen.abdomen",
        "key_to": "abdomen",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.pelvis.hip",
        "key_to": "hip",
        "default_value": [],
        "type":"array",
        "parent_key_name":"pelvis",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.pelvis.pelvis",
        "key_to": "pelvis",
        "default_value": [],
        "type":"array",
        "parent_key_name":"pelvis",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.pelvis.genitals",
        "key_to": "genitals",
        "default_value": [],
        "type":"array",
        "parent_key_name":"pelvis",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.legs.thigh",
        "key_to": "thigh",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.legs.shin",
        "key_to": "shin",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.legs.knee",
        "key_to": "knee",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.legs.foot",
        "key_to": "foot",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.legs.toes",
        "key_to": "toes",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs",
        "to_compute": False,
        "fields_for_computation": []
	},
	{
        "key_from": "symptoms_collection.skin.skin",
        "key_to": "skin",
        "default_value": [],
        "type":"array",
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
    }
]