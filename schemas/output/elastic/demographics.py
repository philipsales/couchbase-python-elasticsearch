profile_mapping = {  
    "demographics":{  
        "_source":{  
            "enabled": True
        },
        "properties":{
            "awh_id": { "type": "keyword" },
            "active": { "type": "boolean" },
            "sex": { "type": "keyword" },
            "birth_date": { 
                "type": "date",
                "format": "MM/dd/yyyy"
            },
            "deceased": {
                "type": "object",
                "properties": {
                    "is_dead": { "type": "boolean" },
                    "year": { "type": "keyword" }
                }
            },
            "address": {
                "type": "object",
                "properties": {
                    "add_date": { "type": "date" },
                    "commnty": { "type": "keyword" },
                    "province": { "type": "keyword" },
                    "zip": { "type": "keyword" },
                    "country": { "type": "keyword" }
                }
            },
            "org": {"type":"keyword"},
            "civil_st": { "type": "keyword" },
            "religion": { "type": "keyword" },
            "educ": { "type": "keyword" },
            "employed": {
                "type": "object",
                "properties": {
                    "is_empl": { "type": "boolean" },
                    "m_income": { "type": "float" },
                    "nature": { "type": "keyword" }
                }
            },
            "version": {
                "type": "object",
                "properties": {
                    "number": { "type": "integer" },
                    "date": { "type": "date" }
                }
            }
        }
    }
}

demographics_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "awh_id",
    "active",
    "sex",
    "birth_date",
    "deceased",
    "address",
    "org",
    "civil_st",
    "religion",
    "educ",
    "employed",
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
    "active": {
      "$id": "#/properties/active",
      "type": "boolean",
      "title": "The Active Schema",
      "default": False,
      "examples": [
        True
      ]
    },
    "sex": {
      "$id": "#/properties/sex",
      "type": "string",
      "title": "The Sex Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "birth_date": {
      "$id": "#/properties/birth_date",
      "type": "string",
      "title": "The Birth_date Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "deceased": {
      "$id": "#/properties/deceased",
      "type": "object",
      "title": "The Deceased Schema",
      "required": [
        "is_dead",
        "year"
      ],
      "properties": {
        "is_dead": {
          "$id": "#/properties/deceased/properties/is_dead",
          "type": "boolean",
          "title": "The Is_dead Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "year": {
          "$id": "#/properties/deceased/properties/year",
          "type": "string",
          "title": "The Year Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "address": {
      "$id": "#/properties/address",
      "type": "object",
      "title": "The Address Schema",
      "required": [
        "add_date",
        "commnty",
        "province",
        "zip",
        "country"
      ],
      "properties": {
        "add_date": {
          "$id": "#/properties/address/properties/add_date",
          "type": "string",
          "title": "The Add_date Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "commnty": {
          "$id": "#/properties/address/properties/commnty",
          "type": "string",
          "title": "The Commnty Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "province": {
          "$id": "#/properties/address/properties/province",
          "type": "string",
          "title": "The Province Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "zip": {
          "$id": "#/properties/address/properties/zip",
          "type": "string",
          "title": "The Zip Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "country": {
          "$id": "#/properties/address/properties/country",
          "type": "string",
          "title": "The Country Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        }
      }
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
    "civil_st": {
      "$id": "#/properties/civil_st",
      "type": "string",
      "title": "The Civil_st Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "religion": {
      "$id": "#/properties/religion",
      "type": "string",
      "title": "The Religion Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "educ": {
      "$id": "#/properties/educ",
      "type": "string",
      "title": "The Educ Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "employed": {
      "$id": "#/properties/employed",
      "type": "object",
      "title": "The Employed Schema",
      "required": [
        "is_empl",
        "m_income",
        "nature"
      ],
      "properties": {
        "is_empl": {
          "$id": "#/properties/employed/properties/is_empl",
          "type": "boolean",
          "title": "The Is_empl Schema",
          "default": False,
          "examples": [
            False
          ]
        },
        "m_income": {
          "$id": "#/properties/employed/properties/m_income",
          "type": "number",
          "title": "The M_income Schema",
          "default": 0.0,
          "examples": [
            0.0
          ]
        },
        "nature": {
          "$id": "#/properties/employed/properties/nature",
          "type": "string",
          "title": "The Nature Schema",
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