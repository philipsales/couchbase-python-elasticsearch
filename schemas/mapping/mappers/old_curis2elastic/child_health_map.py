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

child_health = [
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
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.provided_with_the_following',
                'key_to': 'provided_with_the_following',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.exclusive_breast_feeding',
                'key_to': 'exclusive_breast_feeding',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.experience_any',
                'key_to': 'experience_any',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.mid_upper_arm_circumference',
                'key_to': 'mid_upper_arm_circumference',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.exclusive_breast_feeding',
                'key_to': 'exclusive_breast_feeding',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.eating_solid_food',
                'key_to': 'eating_solid_food',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.following_received',
                'key_to': 'following_received',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.following_experience',
                'key_to': 'following_experience',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.child.mid_upper_arm_circumference',
                'key_to': 'mid_upper_arm_circumference',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'child_healths.child.exclusive_breast_feeding',
                'key_to': 'exclusive_breast_feeding',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': False,
                'fields_for_computation': [],
                'key_from': 'child_healths.child.eating_solid_food',
                'key_to': 'eating_solid_food',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'boolean'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.child.following_received',
                'key_to': 'following_received',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': [],
                'fields_for_computation': [],
                'key_from': 'child_healths.child.following_experience',
                'key_to': 'following_experience',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'array'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.child.times_struggled_to_provide_food_for_child',
                'key_to': 'times_struggled_to_provide_food_for_child',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.child.treatment_for_malnutrition',
                'key_to': 'treatment_for_malnutrition',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.child.if_yes_what_treatment',
                'key_to': 'if_yes_what_treatment',
                'parent_key_name': 'child',
                'to_compute': False,
                'type': 'string'
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
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.where_was_baby_delivered',
                'key_to': 'where_was_baby_delivered',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.how_soon_colostrum_br_milk_after_delivery',
                'key_to': 'how_soon_colostrum_br_milk_after_delivery',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.where_was_baby_delivered',
                'key_to': 'where_was_baby_delivered',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.why_not_deliver_in_health_center',
                'key_to': 'why_not_deliver_in_health_center',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.place_receive_ANC',
                'key_to': 'place_receive_ANC',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.why_not_deliver_in_health_center',
                'key_to': 'why_not_deliver_in_health_center',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.months_of_exclusive_breast_feeding',
                'key_to': 'months_of_exclusive_breast_feeding',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.kind_of_solid_food',
                'key_to': 'kind_of_solid_food',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.provided_first_breast_milk',
                'key_to': 'provided_first_breast_milk',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.provide_colostrum_or_breast_milk_after_delivery',
                'key_to': 'provide_colostrum_or_breast_milk_after_delivery',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': 0,
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.ANC_visits',
                'key_to': 'ANC_visits',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'integer'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.provided_first_breast_milk',
                'key_to': 'provided_first_breast_milk',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.place_receive_ANC',
                'key_to': 'place_receive_ANC',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'string'
        },
        {
                'default_value': 0,
                'fields_for_computation': [],
                'key_from': 'child_healths.infant.ANC_visits',
                'key_to': 'ANC_visits',
                'parent_key_name': 'infant',
                'to_compute': False,
                'type': 'integer'
        },
        {
                'default_value': '',
                'fields_for_computation': [],
                'key_from': 'child_healths.newborn.how_soon_colostrum_br_milk_after_delivery',
                'key_to': 'how_soon_colostrum_br_milk_after_delivery',
                'parent_key_name': 'newborn',
                'to_compute': False,
                'type': 'string'
        }
]