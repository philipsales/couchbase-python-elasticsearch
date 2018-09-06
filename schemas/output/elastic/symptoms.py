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