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

family_planning_and_maternal_health = [
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
                'key_from': 'family_planning_and_maternal_healths.are_you_pregnant',
                'key_to': 'are_you_pregnant',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant_or_have_children',
                'key_to': 'is_pregnant_or_have_children',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': 0,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.ANC_visits',
                'key_to': 'ANC_visits',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'integer'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.place_receive_ANC',
                'key_to': 'place_receive_ANC',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.no_ANC_why_not',
                'key_to': 'no_ANC_why_not',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': 0,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.how_many_children_do_you_have',
                'key_to': 'how_many_children_do_you_have',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'integer'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.why_not_deliver_in_health_center',
                'key_to': 'why_not_deliver_in_health_center',
                'parent_key_name': '',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.how_many_months_are_you_pregnant',
                'key_to': 'how_many_months_are_you_pregnant',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.how_many_parental_visit_did_you_have',
                'key_to': 'how_many_parental_visit_did_you_have',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.where_do_you_plan_to_deliver_baby',
                'key_to': 'where_do_you_plan_to_deliver_baby',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.are_you_taking_ferrous_sulfate_with_folic_acid',
                'key_to': 'are_you_taking_ferrous_sulfate_with_folic_acid',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.were_you_vaccinated_with_tetanus_toxoid',
                'key_to': 'were_you_vaccinated_with_tetanus_toxoid',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.is_this_your_first_pregnancy',
                'key_to': 'is_this_your_first_pregnancy',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.did_you_give_birth_less_than_6_weeks_ago',
                'key_to': 'did_you_give_birth_less_than_6_weeks_ago',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.did_you_experience_the_following',
                'key_to': 'did_you_experience_the_following',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.is_pregnant.do_you_intend_to_practice_family_planning',
                'key_to': 'do_you_intend_to_practice_family_planning',
                'parent_key_name': 'is_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.have_you_been_pregnant_ever_since',
                'key_to': 'have_you_been_pregnant_ever_since',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.how_long_has_it_been_since_your_last_delivery',
                'key_to': 'how_long_has_it_been_since_your_last_delivery',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.when_was_your_last_delivery_date',
                'key_to': 'when_was_your_last_delivery_date',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.what_type_is_the_place_of_delivery',
                'key_to': 'what_type_is_the_place_of_delivery',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.what_childbirth_support_did_you_received',
                'key_to': 'what_childbirth_support_did_you_received',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.did_you_experience_any_of_the_following_after_delivery',
                'key_to': 'did_you_experience_any_of_the_following_after_delivery',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.do_you_have_spouse_right_now',
                'key_to': 'do_you_have_spouse_right_now',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.are_you_both_using_any_family_method',
                'key_to': 'are_you_both_using_any_family_method',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.family_planning_methods_you_are_using',
                'key_to': 'family_planning_methods_you_are_using',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'family_planning_and_maternal_healths.not_pregnant.are_you_willing_to_use_any_family_planning_method',
                'key_to': 'are_you_willing_to_use_any_family_planning_method',
                'parent_key_name': 'not_pregnant',
                'to_compute': False,
                'type': 'boolean'
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