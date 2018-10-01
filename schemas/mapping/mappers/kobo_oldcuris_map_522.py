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

old_curis =[
    {
        "parent_key_name": "identification.id1",
        "key_to": "type",
        "key_from": "identity_consent/identity_document",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "identification.id1",
        "key_to": "identifier",
        "key_from": "identity_consent/personal_id_no",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "",
        "key_from": "identity_consent/questions_to_be_asked",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "user-cam",
        "key_to": "id",
        "key_from": "identity_consent/cam_account",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "user-cam",
        "key_to": "owner",
        "key_from": "identity_consent/cam_account",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "address",
        "key_to": "province",
        "key_from": "identity_consent/town",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "address",
        "key_to": "country",
        "key_from": "identity_consent/country",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "",
        "key_from": "identity_consent/region",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "organization",
        "key_from": "identity_consent/organization",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles.employment",
        "key_to": "currency",
        "key_from": "personal_info/currency",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles",
        "key_to": "where_income_from",
        "key_from": "personal_info/source_of_income",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles.employment",
        "key_to": "monthly_income",
        "key_from": "personal_info/household_monthly_income",
        "default_value": "0.0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "address",
        "key_to": "lot_or_house_number",
        "key_from": "personal_info/address_line_1",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "birthdate",
        "key_from": "personal_info/date_of_birth",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "address",
        "key_to": "postal_code",
        "key_from": "personal_info/postal_code",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "last_name",
        "key_from": "personal_info/last_name",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "",
        "key_from": "personal_info/type_of_registration",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles.employment",
        "key_to": "nature",
        "key_from": "personal_info/work_nature",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "gender",
        "key_from": "personal_info/gender",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles",
        "key_to": "are_you_currently_earning",
        "key_from": "personal_info/is_earning_currently",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "",
        "key_to": "first_name",
        "key_from": "personal_info/first_name",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles",
        "key_to": "civil_status",
        "key_from": "personal_info/civil_status",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "sanitary_type",
        "key_from": "household/type_of_sanitation",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "households",
        "key_to": "how_ensure_water_safe",
        "key_from": "household/ensuring_water_is_safe",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "households",
        "key_to": "type_of_house",
        "key_from": "household/house_construction",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "amenities_present_in_house",
        "key_from": "household/amenities",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "households",
        "key_to": "water_sources",
        "key_from": "household/water_sources",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "households",
        "key_to": "what_u_se_to_wash_hands",
        "key_from": "household/mostly_used_to_wash_hands",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "sanitary_ownership",
        "key_from": "household/sanitation_ownership",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "no_of_people_in_the_household",
        "key_from": "household/no_of_people_household",
        "default_value": "0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations.blood_pressure.second_reading",
        "key_to": "diastole",
        "key_from": "health_information/blood_pressure_2nd_diastole",
        "default_value": "0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "do_u_have_disability",
        "key_from": "health_information/considering_self_with_disabili",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "weight",
        "key_from": "health_information/weight",
        "default_value": "0.0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "taking_long_term_medication",
        "key_from": "health_information/taking_long_term_meds",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "vegetables_in_a_week",
        "key_from": "health_information/vegetable_within_week",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "do_u_have_health_insurance_plan",
        "key_from": "health_information/has_health_insurance_plan",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "why_take_or_not_prescribed_dose",
        "key_from": "health_information/how_taking_prescribed_dose",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "smoking_habit",
        "key_from": "health_information/smoking_habit",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations.blood_pressure.first_reading",
        "key_to": "systole",
        "key_from": "health_information/blood_pressure_1st_systole",
        "default_value": "0.0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "exercise_in_a_week",
        "key_from": "health_information/exercise_within_week",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "how_travel_for_long_term_meds",
        "key_from": "health_information/travel_for_medicine",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "times_exposed_to_smoke",
        "key_from": "health_information/times_exposed_to_t_smoke",
        "default_value": "0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations.blood_pressure.first_reading",
        "key_to": "diastole",
        "key_from": "health_information/blood_pressure_1st_diastole",
        "default_value": "0.0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "alcohol_in_a_week",
        "key_from": "health_information/alcohol_within_week",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "waist_circumference",
        "key_from": "health_information/waist_circumference",
        "default_value": "0.0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "traditional_medicine",
        "key_from": "health_information/traditional_medicine",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "family_history",
        "key_from": "health_information/family_history",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "fruits_in_a_week",
        "key_from": "health_information/fruits_within_week",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations.blood_pressure.second_reading",
        "key_to": "systole",
        "key_from": "health_information/blood_pressure_2nd_systole",
        "default_value": "0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "height",
        "key_from": "health_information/height",
        "default_value": "0.0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "diagnosed",
        "key_from": "health_information/diagnosed",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "dental_health",
        "key_to": "what_problems",
        "key_from": "dental_health/family_dental_problems",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "dental_health",
        "key_to": "times_clean_teeth_daily",
        "key_from": "dental_health/times_brush_teeth_daily",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "dental_health",
        "key_to": "what_do_u_use_to_clean_teeth",
        "key_from": "dental_health/used_for_cleaning_teeth",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "dental_health",
        "key_to": "family_members_d_problems_last_6_months",
        "key_from": "dental_health/last_6_months_dental_fam_probl",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "dental_health",
        "key_to": "do_you_own_toothbrush",
        "key_from": "dental_health/owning_toothbrush",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "disability",
        "key_to": "do_you_have_types_disability",
        "key_from": "disability/types_of_disability",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "how_many_months_are_you_pregnant",
        "key_from": "pregnancy/months_pregnant",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "where_do_you_plan_to_deliver_baby",
        "key_from": "pregnancy/where_to_deliver_baby",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "is_pregnant_or_have_children",
        "key_from": "pregnancy/is_pregnant_or_have_children",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "ANC_visits",
        "key_from": "pregnancy/ANC_visits",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "how_many_children_do_you_have",
        "key_from": "pregnancy/female_no_of_children",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "are_you_taking_ferrous_sulfate_with_folic_acid",
        "key_from": "pregnancy/Are_you_taking_ferro_hate_with_folic_acid",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "is_this_your_first_pregnancy",
        "key_from": "pregnancy/is_first_pregnancy",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "were_you_vaccinated_with_tetanus_toxoid",
        "key_from": "pregnancy/vaccinated_tetanus_toxoid",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "place_receive_ANC",
        "key_from": "pregnancy/place_receive_ANC",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "why_not_deliver_in_health_center",
        "key_from": "pregnancy/why_not_delivr_health_centr",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": "",
        "to_compute": "",
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "how_soon_colostrum_br_milk_after_delivery",
        "key_from": "new_born/how_soon_provided_colostrum",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "place_receive_ANC",
        "key_from": "new_born/place_receive_ANC_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "where_was_baby_delivered",
        "key_from": "new_born/where_baby_delivered",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "ANC_visits",
        "key_from": "new_born/ANC_visits_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "why_not_deliver_in_health_center",
        "key_from": "new_born/why_not_delivr_health_centr_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "provided_first_breast_milk",
        "key_from": "new_born/did_u_provide_1st_breastfeed",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "kind_of_solid_food",
        "key_from": "infant/What_kind_of_solid_f_providing_your_baby",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "why_not_deliver_in_health_center",
        "key_from": "infant/why_not_delivr_health_centr_002",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "exclusive_breast_feeding",
        "key_from": "infant/exclusive_breastfeeding",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "eating_solid_food",
        "key_from": "infant/is_eating_solid_food",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "place_receive_ANC",
        "key_from": "infant/place_receive_ANC_002",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "where_was_baby_delivered",
        "key_from": "infant/where_baby_delivered_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "how_soon_colostrum_br_milk_after_delivery",
        "key_from": "infant/how_soon_provided_colostrum_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "provided_first_breast_milk",
        "key_from": "infant/did_u_provide_1st_breastfeed_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "months_of_exclusive_breast_feeding",
        "key_from": "infant/months_of_exclusive_breastfeed",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "following_received",
        "key_from": "infant/following_received_last_6_mont",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "ANC_visits",
        "key_from": "infant/ANC_visits_002",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "if_yes_what_treatment",
        "key_from": "child_1_5/has_malnutrition_treatmnt",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "following_received",
        "key_from": "child_1_5/following_received_last_6_mont_001",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "times_struggled_to_provide_food_for_child",
        "key_from": "child_1_5/frequency_providing_n_food_chi",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "treatment_for_malnutrition",
        "key_from": "child_1_5/malnutrition_treatment",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "cb_id",
        "key_from": "_uuid",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "kobo_id",
        "key_from": "_uuid",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "registered_at",
        "key_from": "_submission_time",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": ""
    },
    {
        "parent_key_name": "address",
        "key_to": "barangay",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "contact_number",
        "key_to": "country_code",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "contact_number",
        "key_to": "number",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "date_visits",
        "key_from": "",
        "default_value": [datetime.datetime.now().isoformat()],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "",
        "key_to": "email_address",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "family_members",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "allergies",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "blood_sign",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "blood_sugar",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "blood_type",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "high_cost_medicine",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "maintenance_drugs",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "medical_equipments",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "health_informations",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "house_ownership",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "neighborhood_description",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "households",
        "key_to": "no_of_families_in_the_household",
        "key_from": "",
        "default_value": "0",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "integer"
    },
    {
        "parent_key_name": "identification.id2",
        "key_to": "identifier",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "identification.id2",
        "key_to": "type",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "identification.id3",
        "key_to": "identifier",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "identification.id3",
        "key_to": "type",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "last_name_suffix",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "middle_name",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profile_picture",
        "key_to": "name",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profile_picture",
        "key_to": "path",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles",
        "key_to": "education",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "profiles.employment",
        "key_to": "is_employed",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "profiles",
        "key_to": "religion",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "symptoms_collection.abdomen",
        "key_to": "abdomen",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.arms",
        "key_to": "elbow",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.arms",
        "key_to": "fingers",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.arms",
        "key_to": "hand_and_palm",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.arms",
        "key_to": "lower_arm",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.arms",
        "key_to": "upper_arm",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.arms",
        "key_to": "wrist",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.chest",
        "key_to": "chest",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.chest",
        "key_to": "lungs_and_breathing",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "symptoms_collection.head",
        "key_to": "chin_and_jaw",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.head",
        "key_to": "ears",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.head",
        "key_to": "eyes",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.head",
        "key_to": "head",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.head",
        "key_to": "mouth",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.head",
        "key_to": "nose",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.legs",
        "key_to": "foot",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.legs",
        "key_to": "knee",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.legs",
        "key_to": "shin",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.legs",
        "key_to": "thigh",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.legs",
        "key_to": "toes",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.neck",
        "key_to": "lowerback",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.neck",
        "key_to": "neck",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.neck",
        "key_to": "shoulders",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.neck",
        "key_to": "throat",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.neck",
        "key_to": "upperback",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.pelvis",
        "key_to": "genitals",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.pelvis",
        "key_to": "hip",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.pelvis",
        "key_to": "pelvis",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "symptoms_collection.skin",
        "key_to": "skin",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "provided_with_the_following",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths.newborn",
        "key_to": "experience_any",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "mid_upper_arm_circumference",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths.infant",
        "key_to": "following_experience",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "mid_upper_arm_circumference",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "exclusive_breast_feeding",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "eating_solid_food",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "child_healths.child",
        "key_to": "following_experience",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "child_healths",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "are_you_pregnant",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "how_many_parental_visit_did_you_have",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "did_you_give_birth_less_than_6_weeks_ago",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "did_you_experience_the_following",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.is_pregnant",
        "key_to": "do_you_intend_to_practice_family_planning",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "have_you_been_pregnant_ever_since",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "how_long_has_it_been_since_your_last_delivery",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "when_was_your_last_delivery_date",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "what_type_is_the_place_of_delivery",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "what_childbirth_support_did_you_received",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "did_you_experience_any_of_the_following_after_delivery",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "do_you_have_spouse_right_now",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "are_you_both_using_any_family_method",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "family_planning_methods_you_are_using",
        "key_from": "",
        "default_value": [],
        "fields_for_computation": [],
        "to_compute": False,
        "type": "array"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths.not_pregnant",
        "key_to": "are_you_willing_to_use_any_family_planning_method",
        "key_from": "",
        "default_value": False,
        "fields_for_computation": [],
        "to_compute": False,
        "type": "boolean"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "dental_health",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "disability",
        "key_to": "date_updated",
        "key_from": "",
        "default_value": datetime.datetime.now().isoformat(),
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "type",
        "key_from": "",
        "default_value": "user-resident",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "",
        "key_to": "date_completed",
        "key_from": "",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    },
    {
        "parent_key_name": "family_planning_and_maternal_healths",
        "key_to": "no_ANC_why_not",
        "key_from": "pregnancy/not_rec_ANC_local_health_cente",
        "default_value": "",
        "fields_for_computation": [],
        "to_compute": False,
        "type": "string"
    }
]