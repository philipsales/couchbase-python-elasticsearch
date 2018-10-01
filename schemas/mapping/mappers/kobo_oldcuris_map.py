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
        "default_value": datetime.datetime.now().isoformat(),
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
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_xt7zz39/Civil_Status',
        'key_to': 'civil_status',
        'parent_key_name': 'profiles',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'profiles',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'education',
        'parent_key_name': 'profiles',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'is_employed',
        'parent_key_name': 'profiles.employment',
        'to_compute': False,
        'type': "boolean"
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'monthly_income',
        'parent_key_name': 'profiles.employment',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'nature',
        'parent_key_name': 'profiles.employment',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'religion',
        'parent_key_name': 'profiles',
        'to_compute': False,
        'type': 'string'
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
        "key_to": "family_members",
        "default_value": "",
        "type":"string",
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
        "key_to": "health_informations",
        "default_value": [],
        "type":"array",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "date_visits",
        "default_value": [datetime.datetime.now().isoformat()],
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
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'group_db3mc77/Do_you_own_a_toothbrush',
        'key_to': 'do_you_own_toothbrush',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_db3mc77/How_many_times_do_yo_ean_your_teeth_dail',
        'key_to': 'times_clean_teeth_daily',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'group_db3mc77/If_yes_what_problems',
        'key_to': 'what_problems',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'are_you_pregnant',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/Are_you_pregnant_or_lready_have_children',
        'key_to': 'is_pregnant_or_have_children',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/How_many_Ante_Natal_visits_have_you_had',
        'key_to': 'ANC_visits',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/Where_are_you_receiv_Ante_Natal_Care_ANC',
        'key_to': 'place_receive_ANC',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/If_you_are_not_recei_alth_Center_Why_not',
        'key_to': 'no_ANC_why_not',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/If_you_do_not_plan_d_alth_center_why_not',
        'key_to': 'why_not_deliver_in_health_center',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/How_many_children_do_you_have',
        'key_to': 'how_many_children_do_you_have',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/How_many_months_are_you_pregnant',
        'key_to': 'how_many_months_are_you_pregnant',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'how_many_parental_visit_did_you_have',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_pl2cz06/Where_do_you_plan_to_deliver_your_baby',
        'key_to': 'where_do_you_plan_to_deliver_baby',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'are_you_taking_ferrous_sulfate_with_folic_acid',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'were_you_vaccinated_with_tetanus_toxoid',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'is_this_your_first_pregnancy',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'did_you_give_birth_less_than_6_weeks_ago',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'did_you_experience_the_following',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'do_you_intend_to_practice_family_planning',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'have_you_been_pregnant_ever_since',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'how_long_has_it_been_since_your_last_delivery',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'when_was_your_last_delivery_date',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'what_type_is_the_place_of_delivery',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'what_childbirth_support_did_you_received',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'did_you_experience_any_of_the_following_after_delivery',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'do_you_have_spouse_right_now',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'are_you_both_using_any_family_method',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'family_planning_methods_you_are_using',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'are_you_willing_to_use_any_family_planning_method',
        'parent_key_name': 'family_planning_and_maternal_healths.not_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'provided_with_the_following',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'exclusive_breast_feeding',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'experience_any',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'mid_upper_arm_circumference',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'exclusive_breast_feeding',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'eating_solid_food',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'following_received',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'following_experience',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'mid_upper_arm_circumference',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'exclusive_breast_feeding',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'eating_solid_food',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'following_received',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'following_experience',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_at2sh96/Have_you_at_any_time_food_for_your_child',
        'key_to': 'times_struggled_to_provide_food_for_child',
        'parent_key_name': 'child_healths.others',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_at2sh96/Has_your_child_received_treatm',
        'key_to': 'treatment_for_malnutrition',
        'parent_key_name': 'child_healths.others',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_at2sh96/what_treatment',
        'key_to': 'if_yes_what_treatment',
        'parent_key_name': 'child_healths.others',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'child_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'group_df4uy18/What_are_the_ameniti_resent_in_your_house',
        'key_to': 'amenities_present_in_house',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'house_ownership',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'neighborhood_description',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'no_of_families_in_the_household',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'no_of_people_in_the_household',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'sanitary_ownership',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'group_df4uy18/What_type_of_sanitation_do_you_have',
        'key_to': 'sanitary_type',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'type_of_house',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_df4uy18/What_do_you_mostly_u_e_to_wash_your_hands',
        'key_to': 'what_u_se_to_wash_hands',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_df4uy18/How_are_the_walls_of_latrine_constructed',
        'key_to': 'latrine_walls_construction',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'group_df4uy18/What_water_sources_d_ehold_have_access_to',
        'key_to': 'water_sources',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'group_df4uy18/How_do_you_ensure_yo_ter_is_safe_to_drink',
        'key_to': 'how_ensure_water_safe',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_sd0ep41/What_is_the_personal_ID_number',
        'key_to': 'identifier',
        'parent_key_name': 'identification.id1',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'group_sd0ep41/Do_you_have_a_person_ty_document_with_you',
        'key_to': 'type',
        'parent_key_name': 'identification.id1',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'identifier',
        'parent_key_name': 'identification.id2',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'type',
        'parent_key_name': 'identification.id2',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'identifier',
        'parent_key_name': 'identification.id3',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'type',
        'parent_key_name': 'identification.id3',
        'to_compute': False,
        'type': 'string'
    }
]