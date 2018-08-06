
profile_mapping = {  
    "patients":{  
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