household_mapping = {
    "household":{  
        "_source":{  
            "enabled": True
        },
        "properties":{
            "awh_id": {"type":"keyword"},
            "families_in_household": {"type":"integer"},
            "people_in_household": {"type":"integer"},
            "type_of_accommodation": {"type":"keyword"},
            "construction": {"type":"keyword"},
            "type_of_neighbourhood": {"type":"keyword"},
            "utilities": {"type":"keyword"}, 
            "type_of_sanitation": {"type":"keyword"}, 
            "sanitation_ownerships": {"type":"keyword"},
            "org": {"type":"keyword"},
            "water_sources": {"type":"keyword"},
            "how_u_ensure_water_safe": {"type":"keyword"},
            "what_do_u_use_to_wash_hands": {"type":"keyword"},
            "cam_account": {"type": "keyword"},
            "version":{
                "type":"object",
                "properties": {
                    "number": {"type":"integer"},
                    "date": {"type":"date"}
                }               
            }
        }
    }
}

household_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "families_in_household",
    "people_in_household",
    "type_of_accommodation",
    "construction",
    "type_of_neighbourhood",
    "utilities",
    "type_of_sanitation",
    "sanitation_ownerships",
    "org",
    "cam_account",
    "water_sources",
    "how_u_ensure_water_safe",
    "what_do_u_use_to_wash_hands",
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
    "families_in_household": {
      "$id": "#/properties/families_in_household",
      "type": "integer",
      "title": "The Families_in_household Schema",
      "default": 0,
      "examples": [
        0
      ]
    },
    "people_in_household": {
      "$id": "#/properties/people_in_household",
      "type": "integer",
      "title": "The People_in_household Schema",
      "default": 0,
      "examples": [
        0
      ]
    },
    "type_of_accommodation": {
      "$id": "#/properties/type_of_accommodation",
      "type": "string",
      "title": "The Type_of_accommodation Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "construction": {
      "$id": "#/properties/construction",
      "type": "string",
      "title": "The Construction Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "type_of_neighbourhood": {
      "$id": "#/properties/type_of_neighbourhood",
      "type": "string",
      "title": "The Type_of_neighbourhood Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "utilities": {
      "$id": "#/properties/utilities",
      "type": "array",
      "title": "The Utilities Schema"
    },
    "type_of_sanitation": {
      "$id": "#/properties/type_of_sanitation",
      "type": "array",
      "title": "The Type_of_sanitation Schema"
    },
    "sanitation_ownerships": {
      "$id": "#/properties/sanitation_ownerships",
      "type": "string",
      "title": "The Sanitation_ownerships Schema",
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
    "water_sources": {
      "$id": "#/properties/water_sources",
      "type": "array",
      "title": "The Water_sources Schema"
    },
    "how_u_ensure_water_safe": {
      "$id": "#/properties/how_u_ensure_water_safe",
      "type": "array",
      "title": "The How_u_ensure_water_safe Schema"
    },
    "what_do_u_use_to_wash_hands": {
      "$id": "#/properties/what_do_u_use_to_wash_hands",
      "type": "string",
      "title": "The What_do_u_use_to_wash_hands Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
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