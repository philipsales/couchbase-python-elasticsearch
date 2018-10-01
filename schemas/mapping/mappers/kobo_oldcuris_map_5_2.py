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
        "key_from": "personal_info/What_is_your_gender",
        "key_to": "gender",
        "default_value": "unknown",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "personal_info/What_is_your_Post_Zip_Code",
        "key_to": "postal_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "identity_consent/What_is_this_town",
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
        "key_from": "personal_info/What_is_your_Post_Zip_Code",
        "key_to": "postal_code",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "personal_info/What_is_Line_1_of_your_address",
        "key_to": "lot_or_house_number",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "identity_consent/What_is_this_country",
        "key_to": "country",
        "default_value": "",
        "type":"string",
        "parent_key_name":"address",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "personal_info/What_is_your_First_Name",
        "key_to": "first_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "",
        "key_to": "middle_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "personal_info/What_is_your_Family_Name",
        "key_to": "last_name",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "personal_info/What_is_your_date_of_birth",
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
        'key_from': 'personal_info/Civil_Status',
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
        'key_from': 'personal_info/What_is_your_househo_income_approximately',
        'key_to': 'monthly_income',
        'parent_key_name': 'profiles.employment',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'personal_info/What_is_the_nature_of_your_work',
        'key_to': 'nature',
        'parent_key_name': 'profiles.employment',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'personal_info/What_currency_are_you_paid_in',
        'key_to': 'currency',
        'parent_key_name': 'profiles.employment',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'personal_info/Are_you_currently_earning',
        'key_to': 'are_you_currently_earning',
        'parent_key_name': 'profiles',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'personal_info/Where_does_your_income_come_from',
        'key_to': 'where_income_from',
        'parent_key_name': 'profiles',
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
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'allergies',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'health_information/Blood_Pressure_1st_Reading_Diastolic',
        'key_to': 'diastole',
        'parent_key_name': 'health_informations.blood_pressure.first_reading',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'health_information/Blood_Pressure_1st_Reading_Systolic',
        'key_to': 'systole',
        'parent_key_name': 'health_informations.blood_pressure.first_reading',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'health_information/Blood_Pressure_2nd_Reading_Diastolic',
        'key_to': 'diastole',
        'parent_key_name': 'health_informations.blood_pressure.second_reading',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'health_information/Blood_Pressure_2nd_Reading_Systolic',
        'key_to': 'systole',
        'parent_key_name': 'health_informations.blood_pressure.second_reading',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'diastole',
        'parent_key_name': 'health_informations.blood_pressure.third_reading',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'systole',
        'parent_key_name': 'health_informations.blood_pressure.third_reading',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'blood_sign',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'blood_sugar',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'blood_type',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'health_information/Have_you_ever_been_d_any_of_the_following',
        'key_to': 'diagnosed',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/Added_together_how_rate_within_a_week',
        'key_to': 'exercise_in_a_week',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'health_information/Does_your_family_hav_any_of_the_following',
        'key_to': 'family_history',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/How_many_75g_fruits_serving',
        'key_to': 'fruits_in_a_week',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0.0,
        'fields_for_computation': [],
        'key_from': 'health_information/What_is_you_height_in_cm',
        'key_to': 'height',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'float'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'high_cost_medicine',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'maintenance_drugs',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'medical_equipments',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/Do_you_directly_smoke_cigarett',
        'key_to': 'smoking_habit',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/How_many_75g_vegetables_servin',
        'key_to': 'vegetables_in_a_week',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0.0,
        'fields_for_computation': [],
        'key_from': 'health_information/What_is_your_waist_circumference_in_cm',
        'key_to': 'waist_circumference',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'float'
    },
    {
        'default_value': 0.0,
        'fields_for_computation': [],
        'key_from': 'health_information/What_is_your_weight_in_kg',
        'key_to': 'weight',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'float'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/Do_you_take_or_need_to_take_th',
        'key_to': 'taking_long_term_medication',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/Regarding_your_long_the_prescribed_dose',
        'key_to': 'why_take_or_not_prescribed_dose',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/How_many_units_of_al_ll_measure_of_spirit',
        'key_to': 'alcohol_in_a_week',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/How_do_or_would_you_long_term_medicines',
        'key_to': 'how_travel_for_long_term_meds',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/How_many_times_do_yo_in_a_day_on_average',
        'key_to': 'times_exposed_to_smoke',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/Do_you_consider_yourself_to_ha',
        'key_to': 'do_u_have_disability',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/Do_you_currently_hav_ealth_insurance_plan',
        'key_to': 'do_u_have_health_insurance_plan',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'health_information/What_phrase_best_des_raditional_medicines',
        'key_to': 'traditional_medicine',
        'parent_key_name': 'health_informations',
        'to_compute': False,
        'type': 'string'
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
        "key_from": "identity_consent/What_AWH_organisatio_his_registered_under",
        "key_to": "organization",
        "default_value": "",
        "type":"string",
        "parent_key_name":"",
        "to_compute": True,
        "fields_for_computation": ["identity_consent/What_AWH_organisatio_his_registered_under"]
    },
    {
        "key_from": "identity_consent/What_is_the_name_of_resident_is_assigned",
        "key_to": "id",
        "default_value": "",
        "type":"string",
        "parent_key_name":"user-cam",
        "to_compute": False,
        "fields_for_computation": []
    },
    {
        "key_from": "identity_consent/What_is_the_name_of_resident_is_assigned",
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
        'key_from': 'dental_health/Do_you_own_a_toothbrush',
        'key_to': 'do_you_own_toothbrush',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'dental_health/What_do_you_use_to_clean_your_teeth',
        'key_to': 'what_do_u_use_to_clean_teeth',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'dental_health/How_many_times_do_yo_ean_your_teeth_daily',
        'key_to': 'times_clean_teeth_daily',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'dental_health/If_yes_what_problems',
        'key_to': 'what_problems',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'dental_health/Have_any_members_of_your_famil',
        'key_to': 'family_members_d_problems_last_6_months',
        'parent_key_name': 'dental_health',
        'to_compute': False,
        'type': 'string'
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
        'key_from': 'pregnancy/Are_you_pregnant_or_lready_have_children',
        'key_to': 'is_pregnant_or_have_children',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'pregnancy/P_How_many_Ante_Natal_visits',
        'key_to': 'ANC_visits',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'pregnancy/Where_are_you_receiv_Ante_Natal_Care_ANC',
        'key_to': 'place_receive_ANC',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'pregnancy/If_you_are_not_recei_alth_Center_Why_not',
        'key_to': 'no_ANC_why_not',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'pregnancy/If_you_do_not_plan_d_alth_center_why_not',
        'key_to': 'why_not_deliver_in_health_center',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'pregnancy/How_many_children_do_you_have',
        'key_to': 'how_many_children_do_you_have',
        'parent_key_name': 'family_planning_and_maternal_healths',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'pregnancy/How_many_months_are_you_pregnant',
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
        'key_from': 'pregnancy/Where_do_you_plan_to_deliver_your_baby',
        'key_to': 'where_do_you_plan_to_deliver_baby',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'pregnancy/Are_you_taking_ferro_hate_with_folic_acid',
        'key_to': 'are_you_taking_ferrous_sulfate_with_folic_acid',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'pregnancy/Were_you_vaccinated_with_Tetanus_Toxoid',
        'key_to': 'were_you_vaccinated_with_tetanus_toxoid',
        'parent_key_name': 'family_planning_and_maternal_healths.is_pregnant',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'pregnancy/Is_this_your_first_pregnancy',
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
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'new_born/birth_sm_Where_was_baby_dlv',
        'key_to': 'where_was_baby_delivered',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'string'
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
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'new_born/birth_sm_how_soon_after_d_col',
        'key_to': 'how_soon_colostrum_br_milk_after_delivery',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'new_born/birth_sm_Did_u_pvd_the_1st_col',
        'key_to': 'provided_first_breast_milk',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'provide_colostrum_or_breast_milk_after_delivery',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'new_born/birth_sm_why_did_not_dlv_com',
        'key_to': 'why_not_deliver_in_health_center',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'new_born/birth_sm_How_many_Ante_Natal_v',
        'key_to': 'ANC_visits',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'new_born/birth_sm_Where_did_you_rcv_anc',
        'key_to': 'place_receive_ANC',
        'parent_key_name': 'child_healths.newborn',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'infant/fst_year_how_soon_after_d_col',
        'key_to': 'how_soon_colostrum_br_milk_after_delivery',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'infant/fst_year_Where_did_you_rcv_anc',
        'key_to': 'place_receive_ANC',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'infant/fst_year_Where_was_baby_dlv',
        'key_to': 'where_was_baby_delivered',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'infant/first_year_why_did_not_dlv_com',
        'key_to': 'why_not_deliver_in_health_center',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'infant/How_many_months_did_lusively_breast_feed',
        'key_to': 'months_of_exclusive_breast_feeding',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': 0,
        'fields_for_computation': [],
        'key_from': 'infant/fst_year_How_many_Ante_Natal_v',
        'key_to': 'ANC_visits',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'integer'
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
         'default_value': '',
        'fields_for_computation': [],
        'key_from': 'infant/fst_year_Did_u_pvd_the_1st_col',
        'key_to': 'provided_first_breast_milk',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'infant/Is_baby_exclusively_breast_feeding',
        'key_to': 'exclusive_breast_feeding',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'infant/What_kind_of_solid_f_providing_your_baby',
        'key_to': 'kind_of_solid_food',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': False,
        'fields_for_computation': [],
        'key_from': 'infant/Is_baby_eating_solid_food',
        'key_to': 'eating_solid_food',
        'parent_key_name': 'child_healths.infant',
        'to_compute': False,
        'type': 'boolean'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'infant/fst_year_child_rcvd_six_mnts',
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
        'key_from': 'child_1_5/old_year_child_rcvd_six_mnts',
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
        'key_from': 'child_1_5/Have_you_at_any_time_food_for_your_child',
        'key_to': 'times_struggled_to_provide_food_for_child',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'child_1_5/Has_your_child_received_treatm',
        'key_to': 'treatment_for_malnutrition',
        'parent_key_name': 'child_healths.child',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'child_1_5/what_treatment',
        'key_to': 'if_yes_what_treatment',
        'parent_key_name': 'child_healths.child',
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
        'key_from': 'household/What_are_the_ameniti_resent_in_your_house',
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
        'key_from': 'household/How_many_people_are_ing_in_the_household',
        'key_to': 'no_of_people_in_the_household',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'integer'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'household/Is_your_sanitation_owned_or_shared',
        'key_to': 'sanitary_ownership',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'household/What_type_of_sanitation_do_you_have',
        'key_to': 'sanitary_type',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'household/What_best_describes_house_do_you_live_in',
        'key_to': 'type_of_house',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'household/What_do_you_mostly_u_e_to_wash_your_hands',
        'key_to': 'what_u_se_to_wash_hands',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'household/What_water_sources_d_ehold_have_access_to',
        'key_to': 'water_sources',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': [],
        'fields_for_computation': [],
        'key_from': 'household/How_do_you_ensure_yo_ter_is_safe_to_drink',
        'key_to': 'how_ensure_water_safe',
        'parent_key_name': 'households',
        'to_compute': False,
        'type': 'array'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'identity_consent/What_is_the_personal_ID_number',
        'key_to': 'identifier',
        'parent_key_name': 'identification.id1',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'identity_consent/Do_you_have_a_person_ty_document_with_you',
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
    },
    {
        'default_value': '',
        'fields_for_computation': [],
        'key_from': 'disability/Do_you_consider_your_types_of_disability',
        'key_to': 'do_you_have_types_disability',
        'parent_key_name': 'disability',
        'to_compute': False,
        'type': 'string'
    },
    {
        'default_value': datetime.datetime.now().isoformat(),
        'fields_for_computation': [],
        'key_from': '',
        'key_to': 'date_updated',
        'parent_key_name': 'disability',
        'to_compute': False,
        'type': 'string'
    }
]