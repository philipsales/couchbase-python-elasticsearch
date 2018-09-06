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