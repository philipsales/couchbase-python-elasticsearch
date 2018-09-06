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