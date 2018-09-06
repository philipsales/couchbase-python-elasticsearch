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