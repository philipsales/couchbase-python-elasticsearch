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
          "date_updated"
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
          "type_of_house"
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
              "nature"
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
              }
            }
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