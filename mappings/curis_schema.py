import sys 

profile = {
    "civil_status":"",
    "religion":"",
    "employment":{},
    "education":""
}

household = {
    "no_of_families_in_the_household": 0,
    "no_of_people_in_the_household": 0,
    "type_of_house": "",
    "house_ownership": "",
    "neighborhood_description": "",
    "sanitary_type": [],
    "sanitary_ownership": "",
    "amenities_present_in_house": []
}

health = {
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
    "maintenance_drugs": ""
}

symptoms = {
    "head" : {
        "head": [],
        "eyes": [],
        "nose": [],
        "mouth": [],
        "chin_jaw": [],
        "ears": []
    },
    "neck" : {
        "neck": [],
        "throat": [],
        "upperback": [],
        "lowerback": [],
        "shoulder": []
    },
    "chest" : {
        "chest": [],
        "lungs": []
    },
    "arms" : {
        "upper": [],
        "elbow": [],
        "lower": [],
        "wrist": [],
        "hand": [],
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
    }
}