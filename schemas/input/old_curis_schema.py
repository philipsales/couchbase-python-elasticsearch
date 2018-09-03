import sys 

profile = {
    "civil_status":"",
    "religion":"",
    "employment":{
        "is_employed": True,
        "monthly_income": 0.0,
        "nature": "",
    },
    "education":""
}

demographics = {
    "cb_id": "",
    "gender": "",
    "birthdate":"",
    "address": {
        "barangay": "",
        "country": "",
        "lot_or_house_number": "",
        "postal_code": "",
        "province": ""
    },
    "organization": "",
    "profiles": {
        "civil_status":"",
        "religion":"",
        "employment":{
            "is_employed": True,
            "monthly_income": 0.0,
            "nature": "",
        },
        "education":""
    }
}

household = {
    "cb_id":"",
    "organization": "",
    "households": {
        "no_of_families_in_the_household": 0,
        "no_of_people_in_the_household": 0,
        "type_of_house": "",
        "house_ownership": "",
        "neighborhood_description": "",
        "sanitary_type": [],
        "sanitary_ownership": "",
        "amenities_present_in_house": []
    }
}

health = {
    "cb_id": "",
    "organization": "",
    "health_informations": {
        "height": "",
        "weight": "",
        "blood_type": "",
        "blood_sign":"",
        "allergies": "",
        "blood_pressure": {
            "first_reading": {
                "systole": 0.0,
                "diastole": 0.0
            },
            "second_reading": {
                "systole": 0.0,
                "diastole": 0.0
            },
            "third_reading": {
                "systole": 0.0,
                "diastole": 0.0
            }
        },
        "waist_circumference": "",
        "blood_sugar": "",
        "smoking_habit": "",
        "fruits_in_a_week": "",
        "vegetables_in_a_week": "",
        "exercise_in_a_week": "",
        "family_history": [],
        "diagnosed": [],
        "medical_equipments": "",
        "high_cost_medicine": "",
        "maintenance_drugs": "",
        "bmi": ""
    }
}

symptoms = {
    "cb_id": "",
    "organization": "",
    "symptoms_collection": {"head" : {
        "head": [],
        "eyes": [],
        "nose": [],
        "mouth": [],
        "chin_and_jaw": [],
        "ears": []
    },
    "neck" : {
        "neck": [],
        "throat": [],
        "upperback": [],
        "lowerback": [],
        "shoulders": []
    },
    "chest" : {
        "chest": [],
        "lungs_and_breathing": []
    },
    "arms" : {
        "upper_arm": [],
        "elbow": [],
        "lower_arm": [],
        "wrist": [],
        "hand_and_palm": [],
        "fingers": []
    },
    "abdomen": {
        "abdomen": []
    },
    "pelvis" : {
        "hip": [],
        "pelvis": [],
        "genitals": []
    },
    
    "legs" : {
        "thigh": [],
        "shin": [],
        "knee": [],
        "foot": [],
        "toes": []
    },
    "skin": {
        "skin":[]
    }}
}