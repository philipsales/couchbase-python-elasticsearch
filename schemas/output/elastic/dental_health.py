dental_health_mapping = {
	"dental_health":{  
        "_source":{  
            "enabled": True
		},
		"properties":{
			"awh_id":{"type": "keyword"},
			"org": {"type": "keyword"},
			"dental_health": {
				"type":"object",
				"properties": {
          "do_you_own_toothbrush": {"type": "boolean"},
          "times_clean_teeth_daily": {"type": "keyword"},
					"what_problems": {"type": "keyword"},
					"what_do_u_use_to_clean_teeth": {"type": "keyword"},
          "family_members_d_problems_last_6_months": {"type": "keyword"}
				}
			},
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

dental_health_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "org",
    "cam_account",
    "dental_health",
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
    "dental_health": {
      "$id": "#/properties/dental_health",
      "type": "object",
      "title": "The Dental_health Schema",
      "required": [
        "do_you_own_toothbrush",
        "times_clean_teeth_daily",
        "what_problems",
        "what_do_u_use_to_clean_teeth",
        "family_members_d_problems_last_6_months"
      ],
      "properties": {
        "do_you_own_toothbrush": {
          "$id": "#/properties/dental_health/properties/do_you_own_toothbrush",
          "type": "boolean",
          "title": "The Do_you_own_toothbrush Schema",
          "default": False,
          "examples": [
            True
          ]
        },
        "times_clean_teeth_daily": {
          "$id": "#/properties/dental_health/properties/times_clean_teeth_daily",
          "type": "string",
          "title": "The Times_clean_teeth_daily Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "what_problems": {
          "$id": "#/properties/dental_health/properties/what_problems",
          "type": "array",
          "title": "The What_problems Schema"
        },
        "what_do_u_use_to_clean_teeth": {
          "$id": "#/properties/dental_health/properties/what_do_u_use_to_clean_teeth",
          "type": "string",
          "title": "The What_do_u_use_to_clean_teeth Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "family_members_d_problems_last_6_months": {
          "$id": "#/properties/dental_health/properties/family_members_d_problems_last_6_months",
          "type": "string",
          "title": "The Family_members_d_problems_last_6_months Schema",
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