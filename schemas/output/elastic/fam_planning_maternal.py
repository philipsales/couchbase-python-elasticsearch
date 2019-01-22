family_planning_mapping = {
	"family_planning_and_maternal_health":{  
        "_source":{  
            "enabled": True
        },
        "properties":{
			"awh_id": {"type": "keyword"},
			"org": {"type": "keyword"},
			"are_you_pregnant": {"type": "boolean"},
			"is_pregnant_or_have_children": {"type": "keyword"},
			"ANC_visits": {"type": "integer"},
			"place_receive_ANC": {"type": "keyword"},
			"no_ANC_why_not": {"type": "keyword"},
			"how_many_children_do_you_have": {"type": "integer"},
			"why_not_deliver_in_health_center": {"type": "keyword"},
			"is_pregnant": {
				"type": "object",
				"properties": {
					"how_many_months_are_you_pregnant": {"type": "keyword"},
					"how_many_parental_visit_did_you_have": {"type": "keyword"},
					"where_do_you_plan_to_deliver_baby": {"type": "keyword"},
					"are_you_taking_ferrous_sulfate_with_folic_acid": {"type": "boolean"},
					"were_you_vaccinated_with_tetanus_toxoid": {"type": "keyword"},
					"is_this_your_first_pregnancy": {"type": "boolean"},
					"did_you_give_birth_less_than_6_weeks_ago": {"type": "boolean"},
					"did_you_experience_the_following": {"type": "keyword"},
					"do_you_intend_to_practice_family_planning": {"type": "boolean"}
				}
			},
			"not_pregnant": {
				"type": "object",
				"properties": {
					"have_you_been_pregnant_ever_since": {"type": "boolean"},
					"how_long_has_it_been_since_your_last_delivery": {"type": "keyword"},
					"when_was_your_last_delivery_date": {"type": "keyword"},
					"what_type_is_the_place_of_delivery": {"type": "keyword"},
					"what_childbirth_support_did_you_received": {"type": "keyword"},
					"did_you_experience_any_of_the_following_after_delivery": {"type": "keyword"},
					"do_you_have_spouse_right_now": {"type": "boolean"},
					"are_you_both_using_any_family_method": {"type": "boolean"},
					"family_planning_methods_you_are_using": {"type": "keyword"},
					"are_you_willing_to_use_any_family_planning_method": {"type": "boolean"}
				}
			},
			"cam_account": {"type": "keyword"},
			"version": {
				"type": "object",
				"properties": {
					"number": {"type": "integer"},
					"date": {"type": "date"}
				}
			}
		}
	}
}

family_planning_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "org",
    "cam_account",
    "are_you_pregnant",
    "is_pregnant_or_have_children",
    "ANC_visits",
    "place_receive_ANC",
    "no_ANC_why_not",
    "how_many_children_do_you_have",
    "why_not_deliver_in_health_center",
    "is_pregnant",
    "not_pregnant",
    "version"
  ],
  "properties": {
    "awh_id": {
      "$id": "#/properties/awh_id",
      "type": "string",
      "title": "The Awh_id Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "org": {
      "$id": "#/properties/org",
      "type": "string",
      "title": "The Org Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "cam_account": {
      "$id": "#/properties/cam_account",
      "type": "string",
      "title": "The Cam_account Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "are_you_pregnant": {
      "$id": "#/properties/are_you_pregnant",
      "type": "boolean",
      "title": "The Are_you_pregnant Schema",
      "default": False,
      "examples": [
        False
      ]
    },
    "is_pregnant_or_have_children": {
      "$id": "#/properties/is_pregnant_or_have_children",
      "type": "string",
      "title": "The Is_pregnant_or_have_children Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "ANC_visits": {
      "$id": "#/properties/ANC_visits",
      "type": "integer",
      "title": "The Anc_visits Schema",
      "default": 0,
      "examples": [
        1
      ]
    },
    "place_receive_ANC": {
      "$id": "#/properties/place_receive_ANC",
      "type": "string",
      "title": "The Place_receive_anc Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "no_ANC_why_not": {
      "$id": "#/properties/no_ANC_why_not",
      "type": "string",
      "title": "The No_anc_why_not Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "how_many_children_do_you_have": {
      "$id": "#/properties/how_many_children_do_you_have",
      "type": "integer",
      "title": "The How_many_children_do_you_have Schema",
      "default": 0,
      "examples": [
        1
      ]
    },
    "why_not_deliver_in_health_center": {
      "$id": "#/properties/why_not_deliver_in_health_center",
      "type": "string",
      "title": "The Why_not_deliver_in_health_center Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "is_pregnant": {
      "$id": "#/properties/is_pregnant",
      "type": "object",
      "title": "The Is_pregnant Schema",
      "required": [
        "how_many_months_are_you_pregnant",
        "how_many_parental_visit_did_you_have",
        "where_do_you_plan_to_deliver_baby",
        "are_you_taking_ferrous_sulfate_with_folic_acid",
        "were_you_vaccinated_with_tetanus_toxoid",
        "is_this_your_first_pregnancy",
        "did_you_give_birth_less_than_6_weeks_ago",
        "did_you_experience_the_following",
        "do_you_intend_to_practice_family_planning"
      ],
      "properties": {
        "how_many_months_are_you_pregnant": {
          "$id": "#/properties/is_pregnant/properties/how_many_months_are_you_pregnant",
          "type": "string",
          "title": "The How_many_months_are_you_pregnant Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "how_many_parental_visit_did_you_have": {
          "$id": "#/properties/is_pregnant/properties/how_many_parental_visit_did_you_have",
          "type": "string",
          "title": "The How_many_parental_visit_did_you_have Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "where_do_you_plan_to_deliver_baby": {
          "$id": "#/properties/is_pregnant/properties/where_do_you_plan_to_deliver_baby",
          "type": "string",
          "title": "The Where_do_you_plan_to_deliver_baby Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "are_you_taking_ferrous_sulfate_with_folic_acid": {
          "$id": "#/properties/is_pregnant/properties/are_you_taking_ferrous_sulfate_with_folic_acid",
          "type": "boolean",
          "title": "The Are_you_taking_ferrous_sulfate_with_folic_acid Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "were_you_vaccinated_with_tetanus_toxoid": {
          "$id": "#/properties/is_pregnant/properties/were_you_vaccinated_with_tetanus_toxoid",
          "type": "array",
          "title": "The Were_you_vaccinated_with_tetanus_toxoid Schema"
        },
        "is_this_your_first_pregnancy": {
          "$id": "#/properties/is_pregnant/properties/is_this_your_first_pregnancy",
          "type": "boolean",
          "title": "The Is_this_your_first_pregnancy Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "did_you_give_birth_less_than_6_weeks_ago": {
          "$id": "#/properties/is_pregnant/properties/did_you_give_birth_less_than_6_weeks_ago",
          "type": "boolean",
          "title": "The Did_you_give_birth_less_than_6_weeks_ago Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "did_you_experience_the_following": {
          "$id": "#/properties/is_pregnant/properties/did_you_experience_the_following",
          "type": "array",
          "title": "The Did_you_experience_the_following Schema"
        },
        "do_you_intend_to_practice_family_planning": {
          "$id": "#/properties/is_pregnant/properties/do_you_intend_to_practice_family_planning",
          "type": "boolean",
          "title": "The Do_you_intend_to_practice_family_planning Schema",
          "default": False,
          "examples": [
            False
          ]
        }
      }
    },
    "not_pregnant": {
      "$id": "#/properties/not_pregnant",
      "type": "object",
      "title": "The Not_pregnant Schema",
      "required": [
        "have_you_been_pregnant_ever_since",
        "how_long_has_it_been_since_your_last_delivery",
        "when_was_your_last_delivery_date",
        "what_type_is_the_place_of_delivery",
        "what_childbirth_support_did_you_received",
        "did_you_experience_any_of_the_following_after_delivery",
        "do_you_have_spouse_right_now",
        "are_you_both_using_any_family_method",
        "family_planning_methods_you_are_using",
        "are_you_willing_to_use_any_family_planning_method"
      ],
      "properties": {
        "have_you_been_pregnant_ever_since": {
          "$id": "#/properties/not_pregnant/properties/have_you_been_pregnant_ever_since",
          "type": "boolean",
          "title": "The Have_you_been_pregnant_ever_since Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "how_long_has_it_been_since_your_last_delivery": {
          "$id": "#/properties/not_pregnant/properties/how_long_has_it_been_since_your_last_delivery",
          "type": "string",
          "title": "The How_long_has_it_been_since_your_last_delivery Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "when_was_your_last_delivery_date": {
          "$id": "#/properties/not_pregnant/properties/when_was_your_last_delivery_date",
          "type": "string",
          "title": "The When_was_your_last_delivery_date Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "what_type_is_the_place_of_delivery": {
          "$id": "#/properties/not_pregnant/properties/what_type_is_the_place_of_delivery",
          "type": "string",
          "title": "The What_type_is_the_place_of_delivery Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "what_childbirth_support_did_you_received": {
          "$id": "#/properties/not_pregnant/properties/what_childbirth_support_did_you_received",
          "type": "string",
          "title": "The What_childbirth_support_did_you_received Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "did_you_experience_any_of_the_following_after_delivery": {
          "$id": "#/properties/not_pregnant/properties/did_you_experience_any_of_the_following_after_delivery",
          "type": "array",
          "title": "The Did_you_experience_any_of_the_following_after_delivery Schema"
        },
        "do_you_have_spouse_right_now": {
          "$id": "#/properties/not_pregnant/properties/do_you_have_spouse_right_now",
          "type": "boolean",
          "title": "The Do_you_have_spouse_right_now Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "are_you_both_using_any_family_method": {
          "$id": "#/properties/not_pregnant/properties/are_you_both_using_any_family_method",
          "type": "boolean",
          "title": "The Are_you_both_using_any_family_method Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "family_planning_methods_you_are_using": {
          "$id": "#/properties/not_pregnant/properties/family_planning_methods_you_are_using",
          "type": "array",
          "title": "The Family_planning_methods_you_are_using Schema"
        },
        "are_you_willing_to_use_any_family_planning_method": {
          "$id": "#/properties/not_pregnant/properties/are_you_willing_to_use_any_family_planning_method",
          "type": "boolean",
          "title": "The Are_you_willing_to_use_any_family_planning_method Schema",
          "default": False,
          "examples": [
            False
          ]
        }
      }
    },
    "version": {
      "$id": "#/properties/version",
      "type": "object",
      "title": "The Version Schema",
      "required": [
        "number",
        "date"
      ],
      "properties": {
        "number": {
          "$id": "#/properties/version/properties/number",
          "type": "integer",
          "title": "The Number Schema",
          "default": 0,
          "examples": [
            1
          ]
        },
        "date": {
          "$id": "#/properties/version/properties/date",
          "type": "string",
          "title": "The Date Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        }
      }
    }
  }
}