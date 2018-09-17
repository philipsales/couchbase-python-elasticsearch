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

old_curis = [
    {
        "key_from": "What_is_your_gender",
        "key_to": "gender",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_Post_Zip_Code",
        "key_to": "postal_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_town",
        "key_to": "province",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "barangay",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "postal_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "lot_or_house_number",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_country",
        "key_to": "country",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_First_Name",
        "key_to": "first_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_Middle_Name",
        "key_to": "middle_initial",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_Last_Name",
        "key_to": "last_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "What_is_your_date_of_birth",
        "key_to": "birthdate",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "_submission_time",
        "key_to": "registered_at",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "_uuid",
        "key_to": "kobo_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "profiles",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "health_informations",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "households",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "last_name_suffix",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"profile_picture",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "path",
        "default_value": "",
        "type":"string",
        "parent_key_name":"profile_picture",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "country_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"contact_number",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "number",
        "default_value": "",
        "type":"string",
        "parent_key_name":"contact_number",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "email_address",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "child_healths",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "family_members",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "symptoms_collection",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "date_visits",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "Organization",
        "key_to": "organization",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": True,
        "fields_for_computation": ["Organization"]
    },
    {
        "key_from": "CAM",
        "key_to": "id",
        "default_value": "",
        "type":"string",
        "parent_key_name":"user-cam",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "CAM",
        "key_to": "owner",
        "default_value": "",
        "type":"string",
        "parent_key_name":"user-cam",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "type",
        "default_value": "user-resident",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    }

]

old_curis_v1 = [
    {
        "key_from": "group_xt7zz39/What_is_your_gender",
        "key_to": "gender",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/What_is_your_Post_Zip_Code",
        "key_to": "postal_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_sd0ep41/What_is_this_town",
        "key_to": "province",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "barangay",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/What_is_your_Post_Zip_Code",
        "key_to": "postal_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/What_is_Line_1_of_your_address",
        "key_to": "lot_or_house_number",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_sd0ep41/What_is_this_country",
        "key_to": "country",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/What_is_your_First_Name",
        "key_to": "first_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/Do_you_have_an_Alias",
        "key_to": "middle_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/What_is_your_Family_Name",
        "key_to": "last_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_xt7zz39/What_is_your_date_of_birth",
        "key_to": "birthdate",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "_submission_time",
        "key_to": "registered_at",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "_uuid",
        "key_to": "kobo_id",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "profiles",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "health_informations",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "households",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "last_name_suffix",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"profile_picture",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "path",
        "default_value": "",
        "type":"string",
        "parent_key_name":"profile_picture",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "country_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"contact_number",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "number",
        "default_value": "",
        "type":"string",
        "parent_key_name":"contact_number",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "email_address",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "child_healths",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "family_members",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "symptoms_collection",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "date_visits",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_sd0ep41/What_AWH_organisatio_his_registered_under",
        "key_to": "organization",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": True,
        "fields_for_computation": ["group_sd0ep41/What_AWH_organisatio_his_registered_under"]
    },
    {
        "key_from": "group_sd0ep41/What_is_the_name_of_resident_is_assigned",
        "key_to": "id",
        "default_value": "",
        "type":"string",
        "parent_key_name":"user-cam",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "group_sd0ep41/What_is_the_name_of_resident_is_assigned",
        "key_to": "owner",
        "default_value": "",
        "type":"string",
        "parent_key_name":"user-cam",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "type",
        "default_value": "user-resident",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    }
]