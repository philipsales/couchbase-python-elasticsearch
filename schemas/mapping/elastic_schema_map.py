import sys
import datetime

"""

key_from - key of the json attribute to be mapped to new document
key_to - key of the new document where the value of the 'key_from' will be assigned. (leaves part of the tree)
default_value - default value of the 'key_to' field
type - date type of the value of 'key_to'
parent_key_name - parent of json attribute where it belongs and will create dept (i.e. barangay is under address)
                If you want to create further dept, add the another dept with period(.) delimeter (i.e. blood_pressure.first)

"""

demographics = [
    {
        "key_from": "cb_id",
        "key_to": "awh_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
    },
    {
        "key_from": "",
        "key_to": "active",
        "default_value": True,
        "type":"boolean",
        "parent_key_name":""
    },
    {
        "key_from": "gender",
        "key_to": "sex",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":""
    },
    {
        "key_from": "year_of_birth",
        "key_to": "birth_date",
        "default_value": "unknown",
        "type":"date",
        "parent_key_name":""
    },
    {
        "key_from": "",
        "key_to": "is_dead",
        "default_value": False,
        "type":"boolean",
        "parent_key_name":"deceased"
    },
    {
        "key_from": "",
        "key_to": "year",
        "default_value": None,
        "type":"date",
        "parent_key_name":"deceased"
    },
    {
        "key_from": "",
        "key_to": "add_date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"address"
    },
    {
        "key_from": "barangay",
        "key_to": "commnty",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address"
    },
    {
        "key_from": "province",
        "key_to": "province",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address"
    },
    {
        "key_from": "organization",
        "key_to": "org",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
    },
    {
        "key_from": "civil_status",
        "key_to": "civil_st",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":""
    },
    {
        "key_from": "religion",
        "key_to": "religion",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":""
    },
    {
        "key_from": "education",
        "key_to": "educ",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":""
    },
    {
        "key_from": "employment.is_employed",
        "key_to": "is_empl",
        "default_value": "",
        "type":"string",
        "parent_key_name":"employed"
    },
    {
        "key_from": "employment.monthly_income",
        "key_to": "m_income",
        "default_value": 0.0,
        "type":"string",
        "parent_key_name":"employed"
    },
    {
        "key_from": "employment.nature",
        "key_to": "nature",
        "default_value": "",
        "type":"string",
        "parent_key_name":"employed"
    },
    {
        "key_from": "",
        "key_to": "number",
        "default_value": 1,
        "type":"integer",
        "parent_key_name":"version"
    },
    {
        "key_from": "",
        "key_to": "date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"version"
    }
]

household = [
	{
        "key_from": "cb_id",
        "key_to": "awh_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "no_of_families_in_the_household",
        "key_to": "families_in_household",
        "default_value": 0,
        "type":"integer",
        "parent_key_name":""
	},
	{
        "key_from": "no_of_people_in_the_household",
        "key_to": "people_in_household",
        "default_value": 0,
        "type":"integer",
        "parent_key_name":""
	},
	{
        "key_from": "house_ownership",
        "key_to": "type_of_accommodation",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "type_of_house",
        "key_to": "construction",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "neighborhood_description",
        "key_to": "type_of_neighbourhood",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "amenities_present_in_house",
        "key_to": "utilities",
        "default_value": [],
        "type":"array",
        "parent_key_name":""
	},
	{
        "key_from": "sanitary_type",
        "key_to": "type_of_sanitation",
        "default_value": [],
        "type":"array",
        "parent_key_name":""
	},
	{
        "key_from": "sanitary_ownership",
        "key_to": "sanitation_ownerships",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "organization",
        "key_to": "org",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "",
        "key_to": "number",
        "default_value": 1,
        "type":"integer",
        "parent_key_name":"version"
    },
    {
        "key_from": "",
        "key_to": "date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"version"
    }
]

health = [
	{
        "key_from": "cb_id",
        "key_to": "awh_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "bmi",
        "key_to": "bmi",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "blood_type",
        "key_to": "blood_group",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "blood_sign",
        "key_to": "blood_rhesus",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "allergies",
        "key_to": "allergies",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "blood_pressure.first_reading.systole",
        "key_to": "systole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.first"
	},
	{
        "key_from": "blood_pressure.first_reading.diastole",
        "key_to": "diastole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.first"
	},
	{
        "key_from": "blood_pressure.second_reading.systole",
        "key_to": "systole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.second"
	},
	{
        "key_from": "blood_pressure.second_reading.diastole",
        "key_to": "diastole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.second"
	},
	{
        "key_from": "blood_pressure.third_reading.systole",
        "key_to": "systole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.third"
	},
	{
        "key_from": "blood_pressure.third_reading.diastole",
        "key_to": "diastole",
        "default_value": 0.0,
        "type":"float",
        "parent_key_name":"bp.third"
	},
	{
        "key_from": "blood_sugar",
        "key_to": "blood_sugar",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "smoking_habit",
        "key_to": "smoking_habit",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "blood_sugar",
        "key_to": "blood_sugar",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "fruits_in_a_week",
        "key_to": "fruits_in_a_week",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "vegetables_in_a_week",
        "key_to": "vegetables_in_a_week",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "exercise_in_a_week",
        "key_to": "exercise_in_a_week",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "family_history",
        "key_to": "family_history",
        "default_value": [],
        "type":"array",
        "parent_key_name":""
	},
	{
        "key_from": "diagnosed",
        "key_to": "diagnosed",
        "default_value": [],
        "type":"array",
        "parent_key_name":""
	},
	{
        "key_from": "medical_equipments",
        "key_to": "medical_equipments",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "high_cost_medicine",
        "key_to": "high_cost_medicine",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "maintenance_drugs",
        "key_to": "maintenance_drugs",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "organization",
        "key_to": "org",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "",
        "key_to": "number",
        "default_value": 1,
        "type":"integer",
        "parent_key_name":"version"
    },
    {
        "key_from": "",
        "key_to": "date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"version"
    }
]

symptoms = [
	{
        "key_from": "cb_id",
        "key_to": "awh_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "head.head",
        "key_to": "head",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head"
	},
	{
        "key_from": "head.eyes",
        "key_to": "eyes",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head"
	},
	{
        "key_from": "head.nose",
        "key_to": "nose",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head"
	},
	{
        "key_from": "head.mouth",
        "key_to": "mouth",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head"
	},
	{
        "key_from": "head.chin_and_jaw",
        "key_to": "chin_jaw",
        "default_value": [],
        "type":"array",
        "parent_key_name":"head"
	},
	{
        "key_from": "neck.neck",
        "key_to": "neck",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck"
	},
	{
        "key_from": "neck.throat",
        "key_to": "throat",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck"
	},
	{
        "key_from": "neck.upperback",
        "key_to": "upperback",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck"
	},
	{
        "key_from": "neck.lowerback",
        "key_to": "lowerback",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck"
	},
	{
        "key_from": "neck.shoulders",
        "key_to": "shoulders",
        "default_value": [],
        "type":"array",
        "parent_key_name":"neck"
	},
	{
        "key_from": "chest.chest",
        "key_to": "chest",
        "default_value": [],
        "type":"array",
        "parent_key_name":"chest"
	},
	{
        "key_from": "chest.lungs_and_breathing",
        "key_to": "lungs",
        "default_value": [],
        "type":"array",
        "parent_key_name":"chest"
	},
	{
        "key_from": "arms.upper_arm",
        "key_to": "upper",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms"
	},
	{
        "key_from": "arms.lower_arm",
        "key_to": "lower",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms"
	},
	{
        "key_from": "arms.wrist",
        "key_to": "wrist",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms"
	},
	{
        "key_from": "arms.hand_and_palm",
        "key_to": "hand",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms"
	},
	{
        "key_from": "arms.fingers",
        "key_to": "fingers",
        "default_value": [],
        "type":"array",
        "parent_key_name":"arms"
	},
	{
        "key_from": "abdomen.abdomen",
        "key_to": "abdomen",
        "default_value": [],
        "type":"array",
        "parent_key_name":""
	},
	{
        "key_from": "pelvis.hip",
        "key_to": "hip",
        "default_value": [],
        "type":"array",
        "parent_key_name":"pelvis"
	},
	{
        "key_from": "pelvis.pelvis",
        "key_to": "pelvis",
        "default_value": [],
        "type":"array",
        "parent_key_name":"pelvis"
	},
	{
        "key_from": "pelvis.genitals",
        "key_to": "genitals",
        "default_value": [],
        "type":"array",
        "parent_key_name":"pelvis"
	},
	{
        "key_from": "legs.thigh",
        "key_to": "thigh",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs"
	},
	{
        "key_from": "legs.shin",
        "key_to": "shin",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs"
	},
	{
        "key_from": "legs.knee",
        "key_to": "knee",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs"
	},
	{
        "key_from": "legs.foot",
        "key_to": "foot",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs"
	},
	{
        "key_from": "legs.toes",
        "key_to": "toes",
        "default_value": [],
        "type":"array",
        "parent_key_name":"legs"
	},
	{
        "key_from": "skin.skin",
        "key_to": "skin",
        "default_value": [],
        "type":"array",
        "parent_key_name":""
	},
	{
        "key_from": "organization",
        "key_to": "org",
        "default_value": "",
        "type":"string",
        "parent_key_name":""
	},
	{
        "key_from": "",
        "key_to": "number",
        "default_value": 1,
        "type":"integer",
        "parent_key_name":"version"
    },
    {
        "key_from": "",
        "key_to": "date",
        "default_value": datetime.datetime.now().isoformat(),
        "type":"date",
        "parent_key_name":"version"
    }
]