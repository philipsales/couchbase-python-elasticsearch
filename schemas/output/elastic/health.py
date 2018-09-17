health_mapping = {
    "health":{  
        "_source":{  
            "enabled": True
        },
        "properties":{
            "awh_id": {"type":"keyword"},
            "bmi": {"type":"keyword"},
            "blood_group": {"type":"keyword"},
            "blood_rhesus": {"type":"keyword"},
            "allergies": { "type": "keyword"},
            "bp": {
                "type":"object",
                "properties": {
                    "first": {
                        "type":"object",
                        "properties":{
                            "systole": {"type":"keyword"},
                            "diastole": {"type":"keyword"}
                        }
                    },
                    "second": {
                        "type":"object",
                        "properties":{
                            "systole": {"type":"keyword"},
                            "diastole": {"type":"keyword"}
                        }
                    },
                    "third": {
                        "type":"object",
                        "properties":{
                            "systole": {"type":"keyword"},
                            "diastole": {"type":"keyword"}
                        }
                    }
                }
            },
            "blood_sugar": {"type":"keyword"},
            "smoking_habit": {"type":"keyword"},
            "fruits_in_a_week": {"type":"keyword"},
            "vegetables_in_a_week": {"type":"keyword"},
            "exercise_in_a_week": {"type":"keyword"},
            "family_history": {"type":"keyword"},
            "diagnosed": {"type":"keyword"},
            "medical_equipments": {"type":"keyword"},
            "maintenance_drugs": {"type":"keyword"},
            "high_cost_medicine": {"type": "keyword"},
            "org": {"type":"keyword"},
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

health_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "bmi",
    "blood_group",
    "blood_rhesus",
    "allergies",
    "bp",
    "blood_sugar",
    "smoking_habit",
    "fruits_in_a_week",
    "vegetables_in_a_week",
    "exercise_in_a_week",
    "family_history",
    "diagnosed",
    "medical_equipments",
    "maintenance_drugs",
    "high_cost_medicine",
    "org",
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
    "bmi": {
      "$id": "#/properties/bmi",
      "type": "string",
      "title": "The Bmi Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "blood_group": {
      "$id": "#/properties/blood_group",
      "type": "string",
      "title": "The Blood_group Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "blood_rhesus": {
      "$id": "#/properties/blood_rhesus",
      "type": "string",
      "title": "The Blood_rhesus Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "allergies": {
      "$id": "#/properties/allergies",
      "type": "array",
      "title": "The Allergies Schema"
    },
    "bp": {
      "$id": "#/properties/bp",
      "type": "object",
      "title": "The Bp Schema",
      "required": [
        "first",
        "second",
        "third"
      ],
      "properties": {
        "first": {
          "$id": "#/properties/bp/properties/first",
          "type": "object",
          "title": "The First Schema",
          "required": [
            "systole",
            "diastole"
          ],
          "properties": {
            "systole": {
              "$id": "#/properties/bp/properties/first/properties/systole",
              "type": "number",
              "title": "The Systole Schema",
              "default": 0.0,
              "examples": [
                0.0
              ],
              "pattern": "^(.*)$"
            },
            "diastole": {
              "$id": "#/properties/bp/properties/first/properties/diastole",
              "type": "number",
              "title": "The Diastole Schema",
              "default": 0.0,
              "examples": [
                0.0
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "second": {
          "$id": "#/properties/bp/properties/second",
          "type": "object",
          "title": "The Second Schema",
          "required": [
            "systole",
            "diastole"
          ],
          "properties": {
            "systole": {
              "$id": "#/properties/bp/properties/second/properties/systole",
              "type": "number",
              "title": "The Systole Schema",
              "default": 0.0,
              "examples": [
                0.0
              ],
              "pattern": "^(.*)$"
            },
            "diastole": {
              "$id": "#/properties/bp/properties/second/properties/diastole",
              "type": "number",
              "title": "The Diastole Schema",
              "default": 0.0,
              "examples": [
                0.0
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "third": {
          "$id": "#/properties/bp/properties/third",
          "type": "object",
          "title": "The Third Schema",
          "required": [
            "systole",
            "diastole"
          ],
          "properties": {
            "systole": {
              "$id": "#/properties/bp/properties/third/properties/systole",
              "type": "number",
              "title": "The Systole Schema",
              "default": 0.0,
              "examples": [
                0.0
              ],
              "pattern": "^(.*)$"
            },
            "diastole": {
              "$id": "#/properties/bp/properties/third/properties/diastole",
              "type": "number",
              "title": "The Diastole Schema",
              "default": 0.0,
              "examples": [
                0.0
              ],
              "pattern": "^(.*)$"
            }
          }
        }
      }
    },
    "blood_sugar": {
      "$id": "#/properties/blood_sugar",
      "type": "string",
      "title": "The Blood_sugar Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "smoking_habit": {
      "$id": "#/properties/smoking_habit",
      "type": "string",
      "title": "The Smoking_habit Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "fruits_in_a_week": {
      "$id": "#/properties/fruits_in_a_week",
      "type": "string",
      "title": "The Fruits_in_a_week Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "vegetables_in_a_week": {
      "$id": "#/properties/vegetables_in_a_week",
      "type": "string",
      "title": "The Vegetables_in_a_week Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "exercise_in_a_week": {
      "$id": "#/properties/exercise_in_a_week",
      "type": "string",
      "title": "The Exercise_in_a_week Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "family_history": {
      "$id": "#/properties/family_history",
      "type": "array",
      "title": "The Family_history Schema"
    },
    "diagnosed": {
      "$id": "#/properties/diagnosed",
      "type": "array",
      "title": "The Diagnosed Schema"
    },
    "medical_equipments": {
      "$id": "#/properties/medical_equipments",
      "type": "string",
      "title": "The Medical_equipments Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "maintenance_drugs": {
      "$id": "#/properties/maintenance_drugs",
      "type": "string",
      "title": "The Maintenance_drugs Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "high_cost_medicine": {
      "$id": "#/properties/high_cost_medicine",
      "type": "string",
      "title": "The High_cost_medicine Schema",
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