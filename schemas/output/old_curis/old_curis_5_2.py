old_curis_schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "cb_id",
    "address",
    "birthdate",
    "contact_number",
    "date_visits",
    "email_address",
    "family_members",
    "first_name",
    "gender",
    "health_informations",
    "households",
    "identification",
    "last_name",
    "last_name_suffix",
    "middle_name",
    "nhid",
    "organization",
    "profile_picture",
    "profiles",
    "registered_at",
    "symptoms_collection",
    "child_healths",
    "family_planning_and_maternal_healths",
    "dental_health",
    "disability",
    "type",
    "user-cam"
  ],
  "properties": {
    "cb_id": {
      "$id": "#/properties/cb_id",
      "type": "string",
      "title": "The Cb_id Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "address": {
      "$id": "#/properties/address",
      "type": "object",
      "title": "The Address Schema",
      "required": [
        "barangay",
        "country",
        "lot_or_house_number",
        "postal_code",
        "province"
      ],
      "properties": {
        "barangay": {
          "$id": "#/properties/address/properties/barangay",
          "type": "string",
          "title": "The Barangay Schema",
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
        },
        "lot_or_house_number": {
          "$id": "#/properties/address/properties/lot_or_house_number",
          "type": "string",
          "title": "The Lot_or_house_number Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "postal_code": {
          "$id": "#/properties/address/properties/postal_code",
          "type": "string",
          "title": "The Postal_code Schema",
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
        }
      }
    },
    "birthdate": {
      "$id": "#/properties/birthdate",
      "type": "string",
      "title": "The Birthdate Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "contact_number": {
      "$id": "#/properties/contact_number",
      "type": "object",
      "title": "The Contact_number Schema",
      "required": [
        "country_code",
        "number"
      ],
      "properties": {
        "country_code": {
          "$id": "#/properties/contact_number/properties/country_code",
          "type": "string",
          "title": "The Country_code Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "number": {
          "$id": "#/properties/contact_number/properties/number",
          "type": "string",
          "title": "The Number Schema",
          "default": "",
          "examples": [
            ""
          ]
        }
      }
    },
    "date_visits": {
      "$id": "#/properties/date_visits",
      "type": "array",
      "title": "The Date_visits Schema"
    },
    "email_address": {
      "$id": "#/properties/email_address",
      "type": "string",
      "title": "The Email_address Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "family_members": {
      "$id": "#/properties/family_members",
      "type": "array",
      "title": "The Family_members Schema"
    },
    "first_name": {
      "$id": "#/properties/first_name",
      "type": "string",
      "title": "The First_name Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "gender": {
      "$id": "#/properties/gender",
      "type": "string",
      "title": "The Gender Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "health_informations": {
      "$id": "#/properties/health_informations",
      "type": "array",
      "title": "The Health_informations Schema",
      "items": {
        "$id": "#/properties/health_informations/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "allergies",
          "blood_pressure",
          "blood_sign",
          "blood_sugar",
          "blood_type",
          "diagnosed",
          "exercise_in_a_week",
          "family_history",
          "fruits_in_a_week",
          "height",
          "high_cost_medicine",
          "maintenance_drugs",
          "medical_equipments",
          "smoking_habit",
          "vegetables_in_a_week",
          "waist_circumference",
          "weight",
          "date_updated",
          "alcohol_in_a_week",
          "taking_long_term_medication",
          "why_take_or_not_prescribed_dose",
          "how_travel_for_long_term_meds",
          "times_exposed_to_smoke",
          "do_u_have_disability",
          "do_u_have_health_insurance_plan",
          "traditional_medicine"
        ],
        "properties": {
          "allergies": {
            "$id": "#/properties/health_informations/items/properties/allergies",
            "type": "string",
            "title": "The Allergies Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "blood_pressure": {
            "$id": "#/properties/health_informations/items/properties/blood_pressure",
            "type": "object",
            "title": "The Blood_pressure Schema",
            "required": [
              "first_reading",
              "second_reading",
              "third_reading"
            ],
            "properties": {
              "first_reading": {
                "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/first_reading",
                "type": "object",
                "title": "The First_reading Schema",
                "required": [
                  "diastole",
                  "systole"
                ],
                "properties": {
                  "diastole": {
                    "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/first_reading/properties/diastole",
                    "type": "integer",
                    "title": "The Diastole Schema",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  },
                  "systole": {
                    "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/first_reading/properties/systole",
                    "type": "integer",
                    "title": "The Systole Schema",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  }
                }
              },
              "second_reading": {
                "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/second_reading",
                "type": "object",
                "title": "The Second_reading Schema",
                "required": [
                  "diastole",
                  "systole"
                ],
                "properties": {
                  "diastole": {
                    "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/second_reading/properties/diastole",
                    "type": "integer",
                    "title": "The Diastole Schema",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  },
                  "systole": {
                    "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/second_reading/properties/systole",
                    "type": "integer",
                    "title": "The Systole Schema",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  }
                }
              },
              "third_reading": {
                "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/third_reading",
                "type": "object",
                "title": "The Third_reading Schema",
                "required": [
                  "diastole",
                  "systole"
                ],
                "properties": {
                  "diastole": {
                    "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/third_reading/properties/diastole",
                    "type": "integer",
                    "title": "The Diastole Schema",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  },
                  "systole": {
                    "$id": "#/properties/health_informations/items/properties/blood_pressure/properties/third_reading/properties/systole",
                    "type": "integer",
                    "title": "The Systole Schema",
                    "default": 0,
                    "examples": [
                      0
                    ]
                  }
                }
              }
            }
          },
          "blood_sign": {
            "$id": "#/properties/health_informations/items/properties/blood_sign",
            "type": "string",
            "title": "The Blood_sign Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "blood_sugar": {
            "$id": "#/properties/health_informations/items/properties/blood_sugar",
            "type": "string",
            "title": "The Blood_sugar Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "blood_type": {
            "$id": "#/properties/health_informations/items/properties/blood_type",
            "type": "string",
            "title": "The Blood_type Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "diagnosed": {
            "$id": "#/properties/health_informations/items/properties/diagnosed",
            "type": "array",
            "title": "The Diagnosed Schema"
          },
          "exercise_in_a_week": {
            "$id": "#/properties/health_informations/items/properties/exercise_in_a_week",
            "type": "string",
            "title": "The Exercise_in_a_week Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "family_history": {
            "$id": "#/properties/health_informations/items/properties/family_history",
            "type": "array",
            "title": "The Family_history Schema"
          },
          "fruits_in_a_week": {
            "$id": "#/properties/health_informations/items/properties/fruits_in_a_week",
            "type": "string",
            "title": "The Fruits_in_a_week Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "height": {
            "$id": "#/properties/health_informations/items/properties/height",
            "type": "integer",
            "title": "The Height Schema",
            "default": 0,
            "examples": [
              0
            ]
          },
          "high_cost_medicine": {
            "$id": "#/properties/health_informations/items/properties/high_cost_medicine",
            "type": "string",
            "title": "The High_cost_medicine Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "maintenance_drugs": {
            "$id": "#/properties/health_informations/items/properties/maintenance_drugs",
            "type": "string",
            "title": "The Maintenance_drugs Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "medical_equipments": {
            "$id": "#/properties/health_informations/items/properties/medical_equipments",
            "type": "string",
            "title": "The Medical_equipments Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "smoking_habit": {
            "$id": "#/properties/health_informations/items/properties/smoking_habit",
            "type": "string",
            "title": "The Smoking_habit Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "vegetables_in_a_week": {
            "$id": "#/properties/health_informations/items/properties/vegetables_in_a_week",
            "type": "string",
            "title": "The Vegetables_in_a_week Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "waist_circumference": {
            "$id": "#/properties/health_informations/items/properties/waist_circumference",
            "type": "integer",
            "title": "The Waist_circumference Schema",
            "default": 0,
            "examples": [
              0
            ]
          },
          "weight": {
            "$id": "#/properties/health_informations/items/properties/weight",
            "type": "integer",
            "title": "The Weight Schema",
            "default": 0,
            "examples": [
              0
            ]
          },
          "date_updated": {
            "$id": "#/properties/health_informations/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "alcohol_in_a_week": {
            "$id": "#/properties/health_informations/items/properties/alcohol_in_a_week",
            "type": "string",
            "title": "The Alcohol_in_a_week Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "taking_long_term_medication": {
            "$id": "#/properties/health_informations/items/properties/taking_long_term_medication",
            "type": "string",
            "title": "The Taking_long_term_medication Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "why_take_or_not_prescribed_dose": {
            "$id": "#/properties/health_informations/items/properties/why_take_or_not_prescribed_dose",
            "type": "string",
            "title": "The Why_take_or_not_prescribed_dose Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "how_travel_for_long_term_meds": {
            "$id": "#/properties/health_informations/items/properties/how_travel_for_long_term_meds",
            "type": "string",
            "title": "The How_travel_for_long_term_meds Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "times_exposed_to_smoke": {
            "$id": "#/properties/health_informations/items/properties/times_exposed_to_smoke",
            "type": "string",
            "title": "The Times_exposed_to_smoke Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "do_u_have_disability": {
            "$id": "#/properties/health_informations/items/properties/do_u_have_disability",
            "type": "string",
            "title": "The Do_u_have_disability Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "do_u_have_health_insurance_plan": {
            "$id": "#/properties/health_informations/items/properties/do_u_have_health_insurance_plan",
            "type": "string",
            "title": "The Do_u_have_health_insurance_plan Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "traditional_medicine": {
            "$id": "#/properties/health_informations/items/properties/traditional_medicine",
            "type": "string",
            "title": "The Traditional_medicine Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "households": {
      "$id": "#/properties/households",
      "type": "array",
      "title": "The Households Schema",
      "items": {
        "$id": "#/properties/households/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "amenities_present_in_house",
          "date_updated",
          "house_ownership",
          "neighborhood_description",
          "no_of_families_in_the_household",
          "no_of_people_in_the_household",
          "sanitary_ownership",
          "sanitary_type",
          "type_of_house",
          "what_u_se_to_wash_hands",
          "water_sources",
          "how_ensure_water_safe"
        ],
        "properties": {
          "amenities_present_in_house": {
            "$id": "#/properties/households/items/properties/amenities_present_in_house",
            "type": "array",
            "title": "The Amenities_present_in_house Schema"
          },
          "date_updated": {
            "$id": "#/properties/households/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "house_ownership": {
            "$id": "#/properties/households/items/properties/house_ownership",
            "type": "string",
            "title": "The House_ownership Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "neighborhood_description": {
            "$id": "#/properties/households/items/properties/neighborhood_description",
            "type": "string",
            "title": "The Neighborhood_description Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "no_of_families_in_the_household": {
            "$id": "#/properties/households/items/properties/no_of_families_in_the_household",
            "type": "integer",
            "title": "The No_of_families_in_the_household Schema",
            "default": 0,
            "examples": [
              0
            ]
          },
          "no_of_people_in_the_household": {
            "$id": "#/properties/households/items/properties/no_of_people_in_the_household",
            "type": "integer",
            "title": "The No_of_people_in_the_household Schema",
            "default": 0,
            "examples": [
              0
            ]
          },
          "sanitary_ownership": {
            "$id": "#/properties/households/items/properties/sanitary_ownership",
            "type": "string",
            "title": "The Sanitary_ownership Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "sanitary_type": {
            "$id": "#/properties/households/items/properties/sanitary_type",
            "type": "array",
            "title": "The Sanitary_type Schema"
          },
          "type_of_house": {
            "$id": "#/properties/households/items/properties/type_of_house",
            "type": "string",
            "title": "The Type_of_house Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "what_u_se_to_wash_hands": {
            "$id": "#/properties/households/items/properties/what_u_se_to_wash_hands",
            "type": "string",
            "title": "The What_u_se_to_wash_hands Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "water_sources": {
            "$id": "#/properties/households/items/properties/water_sources",
            "type": "array",
            "title": "The Water_sources Schema"
          },
          "how_ensure_water_safe": {
            "$id": "#/properties/households/items/properties/how_ensure_water_safe",
            "type": "array",
            "title": "The How_ensure_water_safe Schema"
          }
        }
      }
    },
    "identification": {
      "$id": "#/properties/identification",
      "type": "object",
      "title": "The Identification Schema",
      "required": [
        "id1",
        "id2",
        "id3"
      ],
      "properties": {
        "id1": {
          "$id": "#/properties/identification/properties/id1",
          "type": "object",
          "title": "The Id1 Schema",
          "required": [
            "identifier",
            "type"
          ],
          "properties": {
            "identifier": {
              "$id": "#/properties/identification/properties/id1/properties/identifier",
              "type": "string",
              "title": "The Identifier Schema",
              "default": "",
              "examples": [
                ""
              ]
            },
            "type": {
              "$id": "#/properties/identification/properties/id1/properties/type",
              "type": "string",
              "title": "The Type Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "id2": {
          "$id": "#/properties/identification/properties/id2",
          "type": "object",
          "title": "The Id2 Schema",
          "required": [
            "identifier",
            "type"
          ],
          "properties": {
            "identifier": {
              "$id": "#/properties/identification/properties/id2/properties/identifier",
              "type": "string",
              "title": "The Identifier Schema",
              "default": "",
              "examples": [
                ""
              ]
            },
            "type": {
              "$id": "#/properties/identification/properties/id2/properties/type",
              "type": "string",
              "title": "The Type Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            }
          }
        },
        "id3": {
          "$id": "#/properties/identification/properties/id3",
          "type": "object",
          "title": "The Id3 Schema",
          "required": [
            "identifier",
            "type"
          ],
          "properties": {
            "identifier": {
              "$id": "#/properties/identification/properties/id3/properties/identifier",
              "type": "string",
              "title": "The Identifier Schema",
              "default": "",
              "examples": [
                ""
              ]
            },
            "type": {
              "$id": "#/properties/identification/properties/id3/properties/type",
              "type": "string",
              "title": "The Type Schema",
              "default": "",
              "examples": [
                ""
              ],
              "pattern": "^(.*)$"
            }
          }
        }
      }
    },
    "last_name": {
      "$id": "#/properties/last_name",
      "type": "string",
      "title": "The Last_name Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "last_name_suffix": {
      "$id": "#/properties/last_name_suffix",
      "type": "string",
      "title": "The Last_name_suffix Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "middle_name": {
      "$id": "#/properties/middle_name",
      "type": "string",
      "title": "The Middle_name Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "nhid": {
      "$id": "#/properties/nhid",
      "type": "string",
      "title": "The Nhid Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "organization": {
      "$id": "#/properties/organization",
      "type": "string",
      "title": "The Organization Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "profile_picture": {
      "$id": "#/properties/profile_picture",
      "type": "object",
      "title": "The Profile_picture Schema",
      "required": [
        "name",
        "path"
      ],
      "properties": {
        "name": {
          "$id": "#/properties/profile_picture/properties/name",
          "type": "string",
          "title": "The Name Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "path": {
          "$id": "#/properties/profile_picture/properties/path",
          "type": "string",
          "title": "The Path Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        }
      }
    },
    "profiles": {
      "$id": "#/properties/profiles",
      "type": "array",
      "title": "The Profiles Schema",
      "items": {
        "$id": "#/properties/profiles/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "civil_status",
          "date_updated",
          "education",
          "employment",
          "are_you_currently_earning",
          "where_income_from",
          "religion"
        ],
        "properties": {
          "civil_status": {
            "$id": "#/properties/profiles/items/properties/civil_status",
            "type": "string",
            "title": "The Civil_status Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "date_updated": {
            "$id": "#/properties/profiles/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "education": {
            "$id": "#/properties/profiles/items/properties/education",
            "type": "string",
            "title": "The Education Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "employment": {
            "$id": "#/properties/profiles/items/properties/employment",
            "type": "object",
            "title": "The Employment Schema",
            "required": [
              "is_employed",
              "monthly_income",
              "nature",
              "currency"
            ],
            "properties": {
              "is_employed": {
                "$id": "#/properties/profiles/items/properties/employment/properties/is_employed",
                "type": "boolean",
                "title": "The Is_employed Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "monthly_income": {
                "$id": "#/properties/profiles/items/properties/employment/properties/monthly_income",
                "type": "string",
                "title": "The Monthly_income Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "nature": {
                "$id": "#/properties/profiles/items/properties/employment/properties/nature",
                "type": "string",
                "title": "The Nature Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "currency": {
                "$id": "#/properties/profiles/items/properties/employment/properties/currency",
                "type": "string",
                "title": "The Currency Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "are_you_currently_earning": {
            "$id": "#/properties/profiles/items/properties/are_you_currently_earning",
            "type": "string",
            "title": "The Are_you_currently_earning Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "where_income_from": {
            "$id": "#/properties/profiles/items/properties/where_income_from",
            "type": "string",
            "title": "The Where_income_from Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "religion": {
            "$id": "#/properties/profiles/items/properties/religion",
            "type": "string",
            "title": "The Religion Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "registered_at": {
      "$id": "#/properties/registered_at",
      "type": "string",
      "title": "The Registered_at Schema",
      "default": "",
      "examples": [
        ""
      ],
      "pattern": "^(.*)$"
    },
    "symptoms_collection": {
      "$id": "#/properties/symptoms_collection",
      "type": "array",
      "title": "The Symptoms_collection Schema",
      "items": {
        "$id": "#/properties/symptoms_collection/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "abdomen",
          "arms",
          "chest",
          "date_updated",
          "head",
          "legs",
          "neck",
          "pelvis",
          "skin"
        ],
        "properties": {
          "abdomen": {
            "$id": "#/properties/symptoms_collection/items/properties/abdomen",
            "type": "object",
            "title": "The Abdomen Schema",
            "required": [
              "abdomen"
            ],
            "properties": {
              "abdomen": {
                "$id": "#/properties/symptoms_collection/items/properties/abdomen/properties/abdomen",
                "type": "array",
                "title": "The Abdomen Schema"
              }
            }
          },
          "arms": {
            "$id": "#/properties/symptoms_collection/items/properties/arms",
            "type": "object",
            "title": "The Arms Schema",
            "required": [
              "elbow",
              "fingers",
              "hand_and_palm",
              "lower_arm",
              "upper_arm",
              "wrist"
            ],
            "properties": {
              "elbow": {
                "$id": "#/properties/symptoms_collection/items/properties/arms/properties/elbow",
                "type": "array",
                "title": "The Elbow Schema"
              },
              "fingers": {
                "$id": "#/properties/symptoms_collection/items/properties/arms/properties/fingers",
                "type": "array",
                "title": "The Fingers Schema"
              },
              "hand_and_palm": {
                "$id": "#/properties/symptoms_collection/items/properties/arms/properties/hand_and_palm",
                "type": "array",
                "title": "The Hand_and_palm Schema"
              },
              "lower_arm": {
                "$id": "#/properties/symptoms_collection/items/properties/arms/properties/lower_arm",
                "type": "array",
                "title": "The Lower_arm Schema"
              },
              "upper_arm": {
                "$id": "#/properties/symptoms_collection/items/properties/arms/properties/upper_arm",
                "type": "array",
                "title": "The Upper_arm Schema"
              },
              "wrist": {
                "$id": "#/properties/symptoms_collection/items/properties/arms/properties/wrist",
                "type": "array",
                "title": "The Wrist Schema"
              }
            }
          },
          "chest": {
            "$id": "#/properties/symptoms_collection/items/properties/chest",
            "type": "object",
            "title": "The Chest Schema",
            "required": [
              "chest",
              "lungs_and_breathing"
            ],
            "properties": {
              "chest": {
                "$id": "#/properties/symptoms_collection/items/properties/chest/properties/chest",
                "type": "array",
                "title": "The Chest Schema"
              },
              "lungs_and_breathing": {
                "$id": "#/properties/symptoms_collection/items/properties/chest/properties/lungs_and_breathing",
                "type": "array",
                "title": "The Lungs_and_breathing Schema"
              }
            }
          },
          "date_updated": {
            "$id": "#/properties/symptoms_collection/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "head": {
            "$id": "#/properties/symptoms_collection/items/properties/head",
            "type": "object",
            "title": "The Head Schema",
            "required": [
              "chin_and_jaw",
              "ears",
              "eyes",
              "head",
              "mouth",
              "nose"
            ],
            "properties": {
              "chin_and_jaw": {
                "$id": "#/properties/symptoms_collection/items/properties/head/properties/chin_and_jaw",
                "type": "array",
                "title": "The Chin_and_jaw Schema"
              },
              "ears": {
                "$id": "#/properties/symptoms_collection/items/properties/head/properties/ears",
                "type": "array",
                "title": "The Ears Schema"
              },
              "eyes": {
                "$id": "#/properties/symptoms_collection/items/properties/head/properties/eyes",
                "type": "array",
                "title": "The Eyes Schema"
              },
              "head": {
                "$id": "#/properties/symptoms_collection/items/properties/head/properties/head",
                "type": "array",
                "title": "The Head Schema"
              },
              "mouth": {
                "$id": "#/properties/symptoms_collection/items/properties/head/properties/mouth",
                "type": "array",
                "title": "The Mouth Schema"
              },
              "nose": {
                "$id": "#/properties/symptoms_collection/items/properties/head/properties/nose",
                "type": "array",
                "title": "The Nose Schema"
              }
            }
          },
          "legs": {
            "$id": "#/properties/symptoms_collection/items/properties/legs",
            "type": "object",
            "title": "The Legs Schema",
            "required": [
              "foot",
              "knee",
              "shin",
              "thigh",
              "toes"
            ],
            "properties": {
              "foot": {
                "$id": "#/properties/symptoms_collection/items/properties/legs/properties/foot",
                "type": "array",
                "title": "The Foot Schema"
              },
              "knee": {
                "$id": "#/properties/symptoms_collection/items/properties/legs/properties/knee",
                "type": "array",
                "title": "The Knee Schema"
              },
              "shin": {
                "$id": "#/properties/symptoms_collection/items/properties/legs/properties/shin",
                "type": "array",
                "title": "The Shin Schema"
              },
              "thigh": {
                "$id": "#/properties/symptoms_collection/items/properties/legs/properties/thigh",
                "type": "array",
                "title": "The Thigh Schema"
              },
              "toes": {
                "$id": "#/properties/symptoms_collection/items/properties/legs/properties/toes",
                "type": "array",
                "title": "The Toes Schema"
              }
            }
          },
          "neck": {
            "$id": "#/properties/symptoms_collection/items/properties/neck",
            "type": "object",
            "title": "The Neck Schema",
            "required": [
              "lowerback",
              "neck",
              "shoulders",
              "throat",
              "upperback"
            ],
            "properties": {
              "lowerback": {
                "$id": "#/properties/symptoms_collection/items/properties/neck/properties/lowerback",
                "type": "array",
                "title": "The Lowerback Schema"
              },
              "neck": {
                "$id": "#/properties/symptoms_collection/items/properties/neck/properties/neck",
                "type": "array",
                "title": "The Neck Schema"
              },
              "shoulders": {
                "$id": "#/properties/symptoms_collection/items/properties/neck/properties/shoulders",
                "type": "array",
                "title": "The Shoulders Schema"
              },
              "throat": {
                "$id": "#/properties/symptoms_collection/items/properties/neck/properties/throat",
                "type": "array",
                "title": "The Throat Schema"
              },
              "upperback": {
                "$id": "#/properties/symptoms_collection/items/properties/neck/properties/upperback",
                "type": "array",
                "title": "The Upperback Schema"
              }
            }
          },
          "pelvis": {
            "$id": "#/properties/symptoms_collection/items/properties/pelvis",
            "type": "object",
            "title": "The Pelvis Schema",
            "required": [
              "genitals",
              "hip",
              "pelvis"
            ],
            "properties": {
              "genitals": {
                "$id": "#/properties/symptoms_collection/items/properties/pelvis/properties/genitals",
                "type": "array",
                "title": "The Genitals Schema"
              },
              "hip": {
                "$id": "#/properties/symptoms_collection/items/properties/pelvis/properties/hip",
                "type": "array",
                "title": "The Hip Schema"
              },
              "pelvis": {
                "$id": "#/properties/symptoms_collection/items/properties/pelvis/properties/pelvis",
                "type": "array",
                "title": "The Pelvis Schema"
              }
            }
          },
          "skin": {
            "$id": "#/properties/symptoms_collection/items/properties/skin",
            "type": "object",
            "title": "The Skin Schema",
            "required": [
              "skin"
            ],
            "properties": {
              "skin": {
                "$id": "#/properties/symptoms_collection/items/properties/skin/properties/skin",
                "type": "array",
                "title": "The Skin Schema"
              }
            }
          }
        }
      }
    },
    "child_healths": {
      "$id": "#/properties/child_healths",
      "type": "array",
      "title": "The Child_healths Schema",
      "items": {
        "$id": "#/properties/child_healths/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "newborn",
          "infant",
          "child",
          "date_updated"
        ],
        "properties": {
          "newborn": {
            "$id": "#/properties/child_healths/items/properties/newborn",
            "type": "object",
            "title": "The Newborn Schema",
            "required": [
              "provided_with_the_following",
              "exclusive_breast_feeding",
              "experience_any",
              "provide_colostrum_or_breast_milk_after_delivery",
              "how_soon_colostrum_br_milk_after_delivery",
              "ANC_visits",
              "place_receive_ANC",
              "why_not_deliver_in_health_center",
              "where_was_baby_delivered",
              "provided_first_breast_milk"
            ],
            "properties": {
              "provided_with_the_following": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/provided_with_the_following",
                "type": "array",
                "title": "The Provided_with_the_following Schema"
              },
              "exclusive_breast_feeding": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/exclusive_breast_feeding",
                "type": "boolean",
                "title": "The Exclusive_breast_feeding Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "experience_any": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/experience_any",
                "type": "array",
                "title": "The Experience_any Schema"
              },
              "provide_colostrum_or_breast_milk_after_delivery": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/provide_colostrum_or_breast_milk_after_delivery",
                "type": "string",
                "title": "The Provide_colostrum_or_breast_milk_after_delivery Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "how_soon_colostrum_br_milk_after_delivery": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/how_soon_colostrum_br_milk_after_delivery",
                "type": "string",
                "title": "The How_soon_colostrum_br_milk_after_delivery Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ANC_visits": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/ANC_visits",
                "type": "integer",
                "title": "The Anc_visits Schema",
                "default": 0,
                "examples": [
                  1
                ]
              },
              "place_receive_ANC": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/place_receive_ANC",
                "type": "string",
                "title": "The Place_receive_anc Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "why_not_deliver_in_health_center": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/why_not_deliver_in_health_center",
                "type": "string",
                "title": "The Why_not_deliver_in_health_center Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "where_was_baby_delivered": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/where_was_baby_delivered",
                "type": "string",
                "title": "The Where_was_baby_delivered Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "provided_first_breast_milk": {
                "$id": "#/properties/child_healths/items/properties/newborn/properties/provided_first_breast_milk",
                "type": "string",
                "title": "The Provided_first_breast_milk Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "infant": {
            "$id": "#/properties/child_healths/items/properties/infant",
            "type": "object",
            "title": "The Infant Schema",
            "required": [
              "mid_upper_arm_circumference",
              "exclusive_breast_feeding",
              "eating_solid_food",
              "kind_of_solid_food",
              "following_received",
              "following_experience",
              "provided_first_breast_milk",
              "how_soon_colostrum_br_milk_after_delivery",
              "months_of_exclusive_breast_feeding",
              "ANC_visits",
              "place_receive_ANC",
              "why_not_deliver_in_health_center",
              "where_was_baby_delivered"
            ],
            "properties": {
              "mid_upper_arm_circumference": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/mid_upper_arm_circumference",
                "type": "array",
                "title": "The Mid_upper_arm_circumference Schema"
              },
              "exclusive_breast_feeding": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/exclusive_breast_feeding",
                "type": "boolean",
                "title": "The Exclusive_breast_feeding Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "eating_solid_food": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/eating_solid_food",
                "type": "boolean",
                "title": "The Eating_solid_food Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "kind_of_solid_food": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/kind_of_solid_food",
                "type": "string",
                "title": "The Kind_of_solid_food Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "following_received": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/following_received",
                "type": "array",
                "title": "The Following_received Schema"
              },
              "following_experience": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/following_experience",
                "type": "array",
                "title": "The Following_experience Schema"
              },
              "provided_first_breast_milk": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/provided_first_breast_milk",
                "type": "string",
                "title": "The Provided_first_breast_milk Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "how_soon_colostrum_br_milk_after_delivery": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/how_soon_colostrum_br_milk_after_delivery",
                "type": "string",
                "title": "The How_soon_colostrum_br_milk_after_delivery Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "months_of_exclusive_breast_feeding": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/months_of_exclusive_breast_feeding",
                "type": "string",
                "title": "The Months_of_exclusive_breast_feeding Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "ANC_visits": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/ANC_visits",
                "type": "integer",
                "title": "The Anc_visits Schema",
                "default": 0,
                "examples": [
                  1
                ]
              },
              "place_receive_ANC": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/place_receive_ANC",
                "type": "string",
                "title": "The Place_receive_anc Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "why_not_deliver_in_health_center": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/why_not_deliver_in_health_center",
                "type": "string",
                "title": "The Why_not_deliver_in_health_center Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "where_was_baby_delivered": {
                "$id": "#/properties/child_healths/items/properties/infant/properties/where_was_baby_delivered",
                "type": "string",
                "title": "The Where_was_baby_delivered Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "child": {
            "$id": "#/properties/child_healths/items/properties/child",
            "type": "object",
            "title": "The Child Schema",
            "required": [
              "mid_upper_arm_circumference",
              "exclusive_breast_feeding",
              "eating_solid_food",
              "following_received",
              "following_experience",
              "times_struggled_to_provide_food_for_child",
              "treatment_for_malnutrition",
              "if_yes_what_treatment"
            ],
            "properties": {
              "mid_upper_arm_circumference": {
                "$id": "#/properties/child_healths/items/properties/child/properties/mid_upper_arm_circumference",
                "type": "array",
                "title": "The Mid_upper_arm_circumference Schema"
              },
              "exclusive_breast_feeding": {
                "$id": "#/properties/child_healths/items/properties/child/properties/exclusive_breast_feeding",
                "type": "boolean",
                "title": "The Exclusive_breast_feeding Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "eating_solid_food": {
                "$id": "#/properties/child_healths/items/properties/child/properties/eating_solid_food",
                "type": "boolean",
                "title": "The Eating_solid_food Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "following_received": {
                "$id": "#/properties/child_healths/items/properties/child/properties/following_received",
                "type": "array",
                "title": "The Following_received Schema"
              },
              "following_experience": {
                "$id": "#/properties/child_healths/items/properties/child/properties/following_experience",
                "type": "array",
                "title": "The Following_experience Schema"
              },
              "times_struggled_to_provide_food_for_child": {
                "$id": "#/properties/child_healths/items/properties/child/properties/times_struggled_to_provide_food_for_child",
                "type": "string",
                "title": "The Times_struggled_to_provide_food_for_child Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "treatment_for_malnutrition": {
                "$id": "#/properties/child_healths/items/properties/child/properties/treatment_for_malnutrition",
                "type": "string",
                "title": "The Treatment_for_malnutrition Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "if_yes_what_treatment": {
                "$id": "#/properties/child_healths/items/properties/child/properties/if_yes_what_treatment",
                "type": "string",
                "title": "The If_yes_what_treatment Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              }
            }
          },
          "date_updated": {
            "$id": "#/properties/child_healths/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "family_planning_and_maternal_healths": {
      "$id": "#/properties/family_planning_and_maternal_healths",
      "type": "array",
      "title": "The Family_planning_and_maternal_healths Schema",
      "items": {
        "$id": "#/properties/family_planning_and_maternal_healths/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "are_you_pregnant",
          "is_pregnant_or_have_children",
          "ANC_visits",
          "place_receive_ANC",
          "no_ANC_why_not",
          "how_many_children_do_you_have",
          "why_not_deliver_in_health_center",
          "is_pregnant",
          "not_pregnant",
          "date_updated"
        ],
        "properties": {
          "are_you_pregnant": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/are_you_pregnant",
            "type": "boolean",
            "title": "The Are_you_pregnant Schema",
            "default": False,
            "examples": [
              False
            ]
          },
          "is_pregnant_or_have_children": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant_or_have_children",
            "type": "string",
            "title": "The Is_pregnant_or_have_children Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "ANC_visits": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/ANC_visits",
            "type": "integer",
            "title": "The Anc_visits Schema",
            "default": 0,
            "examples": [
              1
            ]
          },
          "place_receive_ANC": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/place_receive_ANC",
            "type": "string",
            "title": "The Place_receive_anc Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "no_ANC_why_not": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/no_ANC_why_not",
            "type": "string",
            "title": "The No_anc_why_not Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "how_many_children_do_you_have": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/how_many_children_do_you_have",
            "type": "integer",
            "title": "The How_many_children_do_you_have Schema",
            "default": 0,
            "examples": [
              1
            ]
          },
          "why_not_deliver_in_health_center": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/why_not_deliver_in_health_center",
            "type": "string",
            "title": "The Why_not_deliver_in_health_center Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "is_pregnant": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant",
            "type": "object",
            "title": "The Is_pregnant Schema",
            "required": [
              "how_many_months_are_you_pregnant",
              "how_many_parental_visit_did_you_have",
              "where_do_you_plan_to_deliver_baby",
              "are_you_taking_ferrous_sulfate_with_folic_acid",
              "were_you_vaccinated_with_tetanus_toxoid",
              "is_this_your_first_pregnancy",
              "did_you_give_birth_less_than_6_weeks_ago",
              "did_you_experience_the_following",
              "do_you_intend_to_practice_family_planning"
            ],
            "properties": {
              "how_many_months_are_you_pregnant": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/how_many_months_are_you_pregnant",
                "type": "string",
                "title": "The How_many_months_are_you_pregnant Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "how_many_parental_visit_did_you_have": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/how_many_parental_visit_did_you_have",
                "type": "string",
                "title": "The How_many_parental_visit_did_you_have Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "where_do_you_plan_to_deliver_baby": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/where_do_you_plan_to_deliver_baby",
                "type": "string",
                "title": "The Where_do_you_plan_to_deliver_baby Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "are_you_taking_ferrous_sulfate_with_folic_acid": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/are_you_taking_ferrous_sulfate_with_folic_acid",
                "type": "boolean",
                "title": "The Are_you_taking_ferrous_sulfate_with_folic_acid Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "were_you_vaccinated_with_tetanus_toxoid": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/were_you_vaccinated_with_tetanus_toxoid",
                "type": "array",
                "title": "The Were_you_vaccinated_with_tetanus_toxoid Schema"
              },
              "is_this_your_first_pregnancy": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/is_this_your_first_pregnancy",
                "type": "boolean",
                "title": "The Is_this_your_first_pregnancy Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "did_you_give_birth_less_than_6_weeks_ago": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/did_you_give_birth_less_than_6_weeks_ago",
                "type": "boolean",
                "title": "The Did_you_give_birth_less_than_6_weeks_ago Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "did_you_experience_the_following": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/did_you_experience_the_following",
                "type": "array",
                "title": "The Did_you_experience_the_following Schema"
              },
              "do_you_intend_to_practice_family_planning": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/is_pregnant/properties/do_you_intend_to_practice_family_planning",
                "type": "boolean",
                "title": "The Do_you_intend_to_practice_family_planning Schema",
                "default": False,
                "examples": [
                  False
                ]
              }
            }
          },
          "not_pregnant": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant",
            "type": "object",
            "title": "The Not_pregnant Schema",
            "required": [
              "have_you_been_pregnant_ever_since",
              "how_long_has_it_been_since_your_last_delivery",
              "when_was_your_last_delivery_date",
              "what_type_is_the_place_of_delivery",
              "what_childbirth_support_did_you_received",
              "did_you_experience_any_of_the_following_after_delivery",
              "do_you_have_spouse_right_now",
              "are_you_both_using_any_family_method",
              "family_planning_methods_you_are_using",
              "are_you_willing_to_use_any_family_planning_method"
            ],
            "properties": {
              "have_you_been_pregnant_ever_since": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/have_you_been_pregnant_ever_since",
                "type": "boolean",
                "title": "The Have_you_been_pregnant_ever_since Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "how_long_has_it_been_since_your_last_delivery": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/how_long_has_it_been_since_your_last_delivery",
                "type": "string",
                "title": "The How_long_has_it_been_since_your_last_delivery Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "when_was_your_last_delivery_date": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/when_was_your_last_delivery_date",
                "type": "string",
                "title": "The When_was_your_last_delivery_date Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "what_type_is_the_place_of_delivery": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/what_type_is_the_place_of_delivery",
                "type": "string",
                "title": "The What_type_is_the_place_of_delivery Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "what_childbirth_support_did_you_received": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/what_childbirth_support_did_you_received",
                "type": "string",
                "title": "The What_childbirth_support_did_you_received Schema",
                "default": "",
                "examples": [
                  ""
                ],
                "pattern": "^(.*)$"
              },
              "did_you_experience_any_of_the_following_after_delivery": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/did_you_experience_any_of_the_following_after_delivery",
                "type": "array",
                "title": "The Did_you_experience_any_of_the_following_after_delivery Schema"
              },
              "do_you_have_spouse_right_now": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/do_you_have_spouse_right_now",
                "type": "boolean",
                "title": "The Do_you_have_spouse_right_now Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "are_you_both_using_any_family_method": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/are_you_both_using_any_family_method",
                "type": "boolean",
                "title": "The Are_you_both_using_any_family_method Schema",
                "default": False,
                "examples": [
                  False
                ]
              },
              "family_planning_methods_you_are_using": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/family_planning_methods_you_are_using",
                "type": "array",
                "title": "The Family_planning_methods_you_are_using Schema"
              },
              "are_you_willing_to_use_any_family_planning_method": {
                "$id": "#/properties/family_planning_and_maternal_healths/items/properties/not_pregnant/properties/are_you_willing_to_use_any_family_planning_method",
                "type": "boolean",
                "title": "The Are_you_willing_to_use_any_family_planning_method Schema",
                "default": False,
                "examples": [
                  False
                ]
              }
            }
          },
          "date_updated": {
            "$id": "#/properties/family_planning_and_maternal_healths/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "dental_health": {
      "$id": "#/properties/dental_health",
      "type": "array",
      "title": "The Dental_health Schema",
      "items": {
        "$id": "#/properties/dental_health/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "do_you_own_toothbrush",
          "times_clean_teeth_daily",
          "what_problems",
          "family_members_d_problems_last_6_months",
          "what_do_u_use_to_clean_teeth",
          "date_updated"
        ],
        "properties": {
          "do_you_own_toothbrush": {
            "$id": "#/properties/dental_health/items/properties/do_you_own_toothbrush",
            "type": "boolean",
            "title": "The Do_you_own_toothbrush Schema",
            "default": False,
            "examples": [
              True
            ]
          },
          "times_clean_teeth_daily": {
            "$id": "#/properties/dental_health/items/properties/times_clean_teeth_daily",
            "type": "string",
            "title": "The Times_clean_teeth_daily Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "what_problems": {
            "$id": "#/properties/dental_health/items/properties/what_problems",
            "type": "array",
            "title": "The What_problems Schema"
          },
          "family_members_d_problems_last_6_months": {
            "$id": "#/properties/dental_health/items/properties/family_members_d_problems_last_6_months",
            "type": "string",
            "title": "The Family_members_d_problems_last_6_months Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "what_do_u_use_to_clean_teeth": {
            "$id": "#/properties/dental_health/items/properties/what_do_u_use_to_clean_teeth",
            "type": "string",
            "title": "The What_do_u_use_to_clean_teeth Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "date_updated": {
            "$id": "#/properties/dental_health/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "disability": {
      "$id": "#/properties/disability",
      "type": "array",
      "title": "The Disability Schema",
      "items": {
        "$id": "#/properties/disability/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "do_you_have_types_disability",
          "date_updated"
        ],
        "properties": {
          "do_you_have_types_disability": {
            "$id": "#/properties/disability/items/properties/do_you_have_types_disability",
            "type": "string",
            "title": "The Do_you_have_types_disability Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          },
          "date_updated": {
            "$id": "#/properties/disability/items/properties/date_updated",
            "type": "string",
            "title": "The Date_updated Schema",
            "default": "",
            "examples": [
              ""
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    },
    "type": {
      "$id": "#/properties/type",
      "type": "string",
      "title": "The Type Schema",
      "default": "",
      "examples": [
        "user-resident"
      ],
      "pattern": "^(.*)$"
    },
    "user-cam": {
      "$id": "#/properties/user-cam",
      "type": "object",
      "title": "The User-cam Schema",
      "required": [
        "id",
        "owner"
      ],
      "properties": {
        "id": {
          "$id": "#/properties/user-cam/properties/id",
          "type": "string",
          "title": "The Id Schema",
          "default": "",
          "examples": [
            ""
          ],
          "pattern": "^(.*)$"
        },
        "owner": {
          "$id": "#/properties/user-cam/properties/owner",
          "type": "string",
          "title": "The Owner Schema",
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