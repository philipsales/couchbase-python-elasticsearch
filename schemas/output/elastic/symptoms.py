symptoms_mapping = {
    "symptoms":{  
        "_source":{  
            "enabled": True
        },
        "properties": {
            "awh_id": {"type": "keyword"},
            "org": {"type":"keyword"},
            "head": {
                "type":"object",
                "properties": {
                    "head": {"type": "keyword"},
                    "eyes": {"type": "keyword"},
                    "nose": {"type": "keyword"},
                    "mouth": {"type": "keyword"},
                    "chin_jaw": {"type": "keyword"},
                    "ears": {"type": "keyword"}
                    }
            },
            "neck": {
                "type":"object",
                "properties": {
                    "neck": {"type": "keyword"},
                    "throat": {"type": "keyword"},
                    "upperback": {"type": "keyword"},
                    "lowerback": {"type": "keyword"},
                    "shoulder": {"type": "keyword"}
                }
            },
            "chest": {
                "type":"object",
                "properties": {
                    "chest": {"type": "keyword"},
                    "lungs": {"type": "keyword"}
                }
            },
            "arms": {
                "type":"object",
                "properties": {
                    "upper": {"type": "keyword"},
                    "elbow": {"type": "keyword"},
                    "lower": {"type": "keyword"},
                    "wrist": {"type": "keyword"},
                    "hand": {"type": "keyword"},
                    "fingers": {"type": "keyword"}
                }
            },
            "abdomen": {"type": "keyword"},
            "pelvis": {
                "type":"object",
                "properties": {
                    "hip": {"type": "keyword"},
                    "pelvis": {"type": "keyword"},
                    "genitals": {"type": "keyword"}
                }		
            },
            "legs": {
                "type":"object",
                "properties": {
                    "thigh": {"type": "keyword"},
                    "shin": {"type": "keyword"},
                    "knee": {"type": "keyword"},
                    "foot": {"type": "keyword"},
                    "toes": {"type": "keyword"}
                }
            },
            "skin": {"type": "keyword"},
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
symptoms_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "org",
    "cam_account",
    "head",
    "neck",
    "chest",
    "arms",
    "abdomen",
    "pelvis",
    "legs",
    "skin",
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
    "head": {
      "$id": "#/properties/head",
      "type": "object",
      "title": "The Head Schema",
      "required": [
        "head",
        "eyes",
        "nose",
        "mouth",
        "chin_jaw",
        "ears"
      ],
      "properties": {
        "head": {
          "$id": "#/properties/head/properties/head",
          "type": "array",
          "title": "The Head Schema"
        },
        "eyes": {
          "$id": "#/properties/head/properties/eyes",
          "type": "array",
          "title": "The Eyes Schema"
        },
        "nose": {
          "$id": "#/properties/head/properties/nose",
          "type": "array",
          "title": "The Nose Schema"
        },
        "mouth": {
          "$id": "#/properties/head/properties/mouth",
          "type": "array",
          "title": "The Mouth Schema"
        },
        "chin_jaw": {
          "$id": "#/properties/head/properties/chin_jaw",
          "type": "array",
          "title": "The Chin_jaw Schema"
        },
        "ears": {
          "$id": "#/properties/head/properties/ears",
          "type": "array",
          "title": "The Ears Schema"
        }
      }
    },
    "neck": {
      "$id": "#/properties/neck",
      "type": "object",
      "title": "The Neck Schema",
      "required": [
        "neck",
        "throat",
        "upperback",
        "lowerback",
        "shoulder"
      ],
      "properties": {
        "neck": {
          "$id": "#/properties/neck/properties/neck",
          "type": "array",
          "title": "The Neck Schema"
        },
        "throat": {
          "$id": "#/properties/neck/properties/throat",
          "type": "array",
          "title": "The Throat Schema"
        },
        "upperback": {
          "$id": "#/properties/neck/properties/upperback",
          "type": "array",
          "title": "The Upperback Schema"
        },
        "lowerback": {
          "$id": "#/properties/neck/properties/lowerback",
          "type": "array",
          "title": "The Lowerback Schema"
        },
        "shoulder": {
          "$id": "#/properties/neck/properties/shoulder",
          "type": "array",
          "title": "The Shoulder Schema"
        }
      }
    },
    "chest": {
      "$id": "#/properties/chest",
      "type": "object",
      "title": "The Chest Schema",
      "required": [
        "chest",
        "lungs"
      ],
      "properties": {
        "chest": {
          "$id": "#/properties/chest/properties/chest",
          "type": "array",
          "title": "The Chest Schema"
        },
        "lungs": {
          "$id": "#/properties/chest/properties/lungs",
          "type": "array",
          "title": "The Lungs Schema"
        }
      }
    },
    "arms": {
      "$id": "#/properties/arms",
      "type": "object",
      "title": "The Arms Schema",
      "required": [
        "upper",
        "elbow",
        "lower",
        "wrist",
        "hand",
        "fingers"
      ],
      "properties": {
        "upper": {
          "$id": "#/properties/arms/properties/upper",
          "type": "array",
          "title": "The Upper Schema"
        },
        "elbow": {
          "$id": "#/properties/arms/properties/elbow",
          "type": "array",
          "title": "The Elbow Schema"
        },
        "lower": {
          "$id": "#/properties/arms/properties/lower",
          "type": "array",
          "title": "The Lower Schema"
        },
        "wrist": {
          "$id": "#/properties/arms/properties/wrist",
          "type": "array",
          "title": "The Wrist Schema"
        },
        "hand": {
          "$id": "#/properties/arms/properties/hand",
          "type": "array",
          "title": "The Hand Schema"
        },
        "fingers": {
          "$id": "#/properties/arms/properties/fingers",
          "type": "array",
          "title": "The Fingers Schema"
        }
      }
    },
    "abdomen": {
      "$id": "#/properties/abdomen",
      "type": "array",
      "title": "The Abdomen Schema"
    },
    "pelvis": {
      "$id": "#/properties/pelvis",
      "type": "object",
      "title": "The Pelvis Schema",
      "required": [
        "hip",
        "pelvis",
        "genitals"
      ],
      "properties": {
        "hip": {
          "$id": "#/properties/pelvis/properties/hip",
          "type": "array",
          "title": "The Hip Schema"
        },
        "pelvis": {
          "$id": "#/properties/pelvis/properties/pelvis",
          "type": "array",
          "title": "The Pelvis Schema"
        },
        "genitals": {
          "$id": "#/properties/pelvis/properties/genitals",
          "type": "array",
          "title": "The Genitals Schema"
        }
      }
    },
    "legs": {
      "$id": "#/properties/legs",
      "type": "object",
      "title": "The Legs Schema",
      "required": [
        "thigh",
        "shin",
        "knee",
        "foot",
        "toes"
      ],
      "properties": {
        "thigh": {
          "$id": "#/properties/legs/properties/thigh",
          "type": "array",
          "title": "The Thigh Schema"
        },
        "shin": {
          "$id": "#/properties/legs/properties/shin",
          "type": "array",
          "title": "The Shin Schema"
        },
        "knee": {
          "$id": "#/properties/legs/properties/knee",
          "type": "array",
          "title": "The Knee Schema"
        },
        "foot": {
          "$id": "#/properties/legs/properties/foot",
          "type": "array",
          "title": "The Foot Schema"
        },
        "toes": {
          "$id": "#/properties/legs/properties/toes",
          "type": "array",
          "title": "The Toes Schema"
        }
      }
    },
    "skin": {
      "$id": "#/properties/skin",
      "type": "array",
      "title": "The Skin Schema"
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