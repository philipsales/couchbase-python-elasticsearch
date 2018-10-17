child_health_mapping = {
	"child_health":{  
        "_source":{  
            "enabled": True
		},
		"properties":{
			"awh_id": {
        "type": "keyword",
        "index": "not_analyzed"
      },
			"org": {"type": "keyword"},
      "newborn": {
        "type": "object",
        "properties": {
            "provided_with_the_following": {"type": "keyword"},
            "exclusive_breast_feeding": {"type": "boolean"},
            "experience_any": {"type": "keyword"},
            "provide_colostrum_or_breast_milk_after_delivery": {"type": "keyword"},
            "how_soon_colostrum_br_milk_after_delivery": {"type": "keyword"},
            "ANC_visits": {"type": "integer"},
            "place_receive_ANC": {"type": "keyword"},
            "why_not_deliver_in_health_center": {"type": "keyword"},
            "where_was_baby_delivered": {"type": "keyword"},
            "provided_first_breast_milk": {"type": "keyword"}
        }
      },
      "infant": {
        "type": "object",
        "properties": {
            "mid_upper_arm_circumference": {"type": "keyword"},
            "exclusive_breast_feeding": {"type": "boolean"},
            "eating_solid_food": {"type": "boolean"},
            "kind_of_solid_food": {"type": "keyword"},
            "following_received": {"type": "keyword"},
            "following_experience": {"type": "keyword"},
            "provided_first_breast_milk": {"type": "keyword"},
            "how_soon_colostrum_br_milk_after_delivery": {"type": "keyword"},
            "months_of_exclusive_breast_feeding": {"type": "keyword"},
            "ANC_visits": {"type": "integer"},
            "place_receive_ANC": {"type": "keyword"},
            "why_not_deliver_in_health_center": {"type": "keyword"},
            "where_was_baby_delivered": {"type": "keyword"}
        }
      },
      "child": {
        "type": "object",
        "properties": {
            "mid_upper_arm_circumference": {"type": "keyword"},
            "exclusive_breast_feeding": {"type": "boolean"},
            "eating_solid_food": {"type": "boolean"},
            "following_received": {"type": "keyword"},
            "following_experience": {"type": "keyword"},
            "times_struggled_to_provide_food_for_child": {"type": "keyword"},
            "treatment_for_malnutrition": {"type": "keyword"},
            "if_yes_what_treatment": {"type": "keyword"}
        }
      },
			"version": {
        "type": "object",
        "properties": {
          "number": {"type": "integer"},
          "date":{"type": "date"}
        }
			}
		}
	}
}

child_health_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "org",
    "newborn",
    "infant",
    "child",
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
    "newborn": {
      "$id": "#/properties/newborn",
      "type": "object",
      "title": "The Newborn Schema",
      "required": [
        "provided_with_the_following",
        "exclusive_breast_feeding",
        "experience_any",
        "provide_colostrum_or_breast_milk_after_delivery",
        "how_soon_colostrum_br_milk_after_delivery",
        "ANC_visits",
        "place_receive_ANC",
        "why_not_deliver_in_health_center",
        "where_was_baby_delivered",
        "provided_first_breast_milk"
      ],
      "properties": {
        "provided_with_the_following": {
          "$id": "#/properties/newborn/properties/provided_with_the_following",
          "type": "array",
          "title": "The Provided_with_the_following Schema"
        },
        "exclusive_breast_feeding": {
          "$id": "#/properties/newborn/properties/exclusive_breast_feeding",
          "type": "boolean",
          "title": "The Exclusive_breast_feeding Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "experience_any": {
          "$id": "#/properties/newborn/properties/experience_any",
          "type": "array",
          "title": "The Experience_any Schema"
        },
        "provide_colostrum_or_breast_milk_after_delivery": {
          "$id": "#/properties/newborn/properties/provide_colostrum_or_breast_milk_after_delivery",
          "type": "string",
          "title": "The Provide_colostrum_or_breast_milk_after_delivery Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "how_soon_colostrum_br_milk_after_delivery": {
          "$id": "#/properties/newborn/properties/how_soon_colostrum_br_milk_after_delivery",
          "type": "string",
          "title": "The How_soon_colostrum_br_milk_after_delivery Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "ANC_visits": {
          "$id": "#/properties/newborn/properties/ANC_visits",
          "type": "integer",
          "title": "The Anc_visits Schema",
          "default": 0,
          "examples": [
            1
          ]
        },
        "place_receive_ANC": {
          "$id": "#/properties/newborn/properties/place_receive_ANC",
          "type": "string",
          "title": "The Place_receive_anc Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "why_not_deliver_in_health_center": {
          "$id": "#/properties/newborn/properties/why_not_deliver_in_health_center",
          "type": "string",
          "title": "The Why_not_deliver_in_health_center Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "where_was_baby_delivered": {
          "$id": "#/properties/newborn/properties/where_was_baby_delivered",
          "type": "string",
          "title": "The Where_was_baby_delivered Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "provided_first_breast_milk": {
          "$id": "#/properties/newborn/properties/provided_first_breast_milk",
          "type": "string",
          "title": "The Provided_first_breast_milk Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "infant": {
      "$id": "#/properties/infant",
      "type": "object",
      "title": "The Infant Schema",
      "required": [
        "mid_upper_arm_circumference",
        "exclusive_breast_feeding",
        "eating_solid_food",
        "kind_of_solid_food",
        "following_received",
        "following_experience",
        "provided_first_breast_milk",
        "how_soon_colostrum_br_milk_after_delivery",
        "months_of_exclusive_breast_feeding",
        "ANC_visits",
        "place_receive_ANC",
        "why_not_deliver_in_health_center",
        "where_was_baby_delivered"
      ],
      "properties": {
        "mid_upper_arm_circumference": {
          "$id": "#/properties/infant/properties/mid_upper_arm_circumference",
          "type": "array",
          "title": "The Mid_upper_arm_circumference Schema"
        },
        "exclusive_breast_feeding": {
          "$id": "#/properties/infant/properties/exclusive_breast_feeding",
          "type": "boolean",
          "title": "The Exclusive_breast_feeding Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "eating_solid_food": {
          "$id": "#/properties/infant/properties/eating_solid_food",
          "type": "boolean",
          "title": "The Eating_solid_food Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "kind_of_solid_food": {
          "$id": "#/properties/infant/properties/kind_of_solid_food",
          "type": "string",
          "title": "The Kind_of_solid_food Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "following_received": {
          "$id": "#/properties/infant/properties/following_received",
          "type": "array",
          "title": "The Following_received Schema"
        },
        "following_experience": {
          "$id": "#/properties/infant/properties/following_experience",
          "type": "array",
          "title": "The Following_experience Schema"
        },
        "provided_first_breast_milk": {
          "$id": "#/properties/infant/properties/provided_first_breast_milk",
          "type": "string",
          "title": "The Provided_first_breast_milk Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "how_soon_colostrum_br_milk_after_delivery": {
          "$id": "#/properties/infant/properties/how_soon_colostrum_br_milk_after_delivery",
          "type": "string",
          "title": "The How_soon_colostrum_br_milk_after_delivery Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "months_of_exclusive_breast_feeding": {
          "$id": "#/properties/infant/properties/months_of_exclusive_breast_feeding",
          "type": "string",
          "title": "The Months_of_exclusive_breast_feeding Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "ANC_visits": {
          "$id": "#/properties/infant/properties/ANC_visits",
          "type": "integer",
          "title": "The Anc_visits Schema",
          "default": 0,
          "examples": [
            1
          ]
        },
        "place_receive_ANC": {
          "$id": "#/properties/infant/properties/place_receive_ANC",
          "type": "string",
          "title": "The Place_receive_anc Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "why_not_deliver_in_health_center": {
          "$id": "#/properties/infant/properties/why_not_deliver_in_health_center",
          "type": "string",
          "title": "The Why_not_deliver_in_health_center Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "where_was_baby_delivered": {
          "$id": "#/properties/infant/properties/where_was_baby_delivered",
          "type": "string",
          "title": "The Where_was_baby_delivered Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "child": {
      "$id": "#/properties/child",
      "type": "object",
      "title": "The Child Schema",
      "required": [
        "mid_upper_arm_circumference",
        "exclusive_breast_feeding",
        "eating_solid_food",
        "following_received",
        "following_experience",
        "times_struggled_to_provide_food_for_child",
        "treatment_for_malnutrition",
        "if_yes_what_treatment"
      ],
      "properties": {
        "mid_upper_arm_circumference": {
          "$id": "#/properties/child/properties/mid_upper_arm_circumference",
          "type": "array",
          "title": "The Mid_upper_arm_circumference Schema"
        },
        "exclusive_breast_feeding": {
          "$id": "#/properties/child/properties/exclusive_breast_feeding",
          "type": "boolean",
          "title": "The Exclusive_breast_feeding Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "eating_solid_food": {
          "$id": "#/properties/child/properties/eating_solid_food",
          "type": "boolean",
          "title": "The Eating_solid_food Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "following_received": {
          "$id": "#/properties/child/properties/following_received",
          "type": "array",
          "title": "The Following_received Schema"
        },
        "following_experience": {
          "$id": "#/properties/child/properties/following_experience",
          "type": "array",
          "title": "The Following_experience Schema"
        },
        "times_struggled_to_provide_food_for_child": {
          "$id": "#/properties/child/properties/times_struggled_to_provide_food_for_child",
          "type": "string",
          "title": "The Times_struggled_to_provide_food_for_child Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "treatment_for_malnutrition": {
          "$id": "#/properties/child/properties/treatment_for_malnutrition",
          "type": "string",
          "title": "The Treatment_for_malnutrition Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "if_yes_what_treatment": {
          "$id": "#/properties/child/properties/if_yes_what_treatment",
          "type": "string",
          "title": "The If_yes_what_treatment Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
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
            0
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