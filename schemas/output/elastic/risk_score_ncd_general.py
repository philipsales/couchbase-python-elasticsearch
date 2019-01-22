risk_score_ncd_general_mapping = {
    "risk_score_ncd_general":{  
        "_source":{  
            "enabled": True
        },
        "properties":{
            "awh_id": {"type":"keyword"},
            "org": {"type":"keyword"},
            "cam_account": {"type":"keyword"},
            "risk_score_ncd_general": {"type":"integer"},
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

risk_score_ncd_general_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "org",
    "cam_account",
    "risk_score_ncd_general",
    "version"
  ],
  "properties": {
    "awh_id": {
      "$id": "#/properties/awh_id",
      "type": "string",
      "title": "The Awh_id Schema",
      "default": "",
      "examples": [
        "1231231"
      ],
      "pattern": "^(.*)$"
    },
    "org": {
      "$id": "#/properties/org",
      "type": "string",
      "title": "The Org Schema",
      "default": "",
      "examples": [
        "Cuartero RHU"
      ],
      "pattern": "^(.*)$"
    },
    "cam_account": {
      "$id": "#/properties/cam_account",
      "type": "string",
      "title": "The Cam_account Schema",
      "default": "",
      "examples": [
        "rostee@gmail.com"
      ],
      "pattern": "^(.*)$"
    },
    "risk_score_ncd_general": {
      "$id": "#/properties/risk_score_ncd_general",
      "type": "integer",
      "title": "The NCD General Schema",
      "default": 0,
      "examples": [
        8
      ]
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
            "2018-21-05T00:00:00"
          ],
          "pattern": "^(.*)$"
        }
      }
    }
  }
}