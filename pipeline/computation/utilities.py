FEET_TO_METER = .3048
HEIGHT_NOT_METRIC = 10.00

INFORMAL_SETTLERS = "Informal settlers"

MINIMUM_BMI = 5.00
UNDERWEIGHT_CEILING = 18.59
NORMAL_FLOOR = 18.60
NORMAL_CEILING = 24.99
OVERWEIGHT_FLOOR = 25.00
OVERWEIGHT_CEILING = 29.99
OBESE_FLOOR = 30.00

ELEMENTARY_LEVEL = "Elementary Level"
ELEMENTARY_GRADUATE = "Elementary Graduate"
BAHAY_KUBO = "Bahay-kubo"
WOOD_BASED = "Wood-based"
SHARED = "Shared"

class Computations:
    def __init__(self, params):
        self.params = params

    '''
    EXTERNAL FUNCTIONS

    the function names should be included in the variable "computations"
    in hash_maps/hash_map.py

    #TODO: Add logic here if there are new computations. Make sure to keep it
    in a function
    '''
    def bmi(self):
        try:

            variable = self._typecast_bmi_params()

            (height, weight) = (variable["height"], variable["weight"])

            final_height = self._height_to_metric(height)
            final_height = final_height / 100
                
            # Computation of BMI
            bmi = round(weight / (final_height ** 2), 2)

            # Assigning the BMI result
            bmi_result = self._categorize_bmi(bmi)
        # This happens when height and weight is a string
        except TypeError:
            bmi_result = "Undefined"
        
        # This happens when the values are zeros
        except ZeroDivisionError:
            bmi_result = "Undefined"
            
        return bmi_result

    def organization(self):
        org = next(iter(self.params.values()))
        return org.replace("_"," ")

    def poor_risk_score(self):
        score = 0

        house_ownership = self.params["households.house_ownership"]
        id_type = self.params["identification.id1.type"]
        id_identifier = self.params["identification.id1.identifier"]
        
        occupation = self._occupation_filter()

        if(house_ownership.casefold() == INFORMAL_SETTLERS.casefold() or (id_type == "4Ps" and id_identifier != None)):
            score = 12
        elif(occupation != ""):
            income = self._typecase_monthly_income()
            education = self.params["profiles.education"]
            type_of_house = self.params["households.type_of_house"]
            sanitary_ownership = self.params["households.sanitary_ownership"]
            amenities_points = self._amenities_counter()

            score = (self._income_score(income) + self._education_score(education)
                    + amenities_points + self._type_of_house_score(type_of_house)
                    + self._sanitary_ownership_score(sanitary_ownership))

        return score

    '''
    INTERNAL FUNCTIONS ONLY

    used by the external functions
    '''
    
    def _categorize_bmi(self,bmi):
        bmi_result=""

        if bmi <= MINIMUM_BMI:
            bmi_result = "Underweight"
        elif bmi >= NORMAL_FLOOR and bmi < NORMAL_CEILING:
            bmi_result = "Normal"
        elif bmi >= OVERWEIGHT_FLOOR and bmi < OVERWEIGHT_CEILING:
            bmi_result = "Overweight"
        elif bmi >= OBESE_FLOOR: 
            bmi_result = "Obese"
        else:
            bmi_result = "Undefined"
            
        return bmi_result

    def _typecast_bmi_params(self):
        try:
            # Convert height and weight to integer
            height = int(self.params["health_informations.height"])
            weight = int(self.params["health_informations.weight"])

        # If values are empty strings...
        except ValueError:
            height = 0.0
            weight = 0.0

        return {"height": height, "weight": weight}
    
    def _typecase_monthly_income(self):
        try:
            monthly_income = int(self.params["profiles.employment.monthly_income"])
        except ValueError:
            monthly_income = 0
        
        return monthly_income

    def _income_score(self,income):
        if(income < 1000):
            score = 5
        elif(income < 2500 and (income >= 1000 or income < 2500)):
            score = 4
        elif(income < 5000 and (income >= 2500 or income < 5000)):
            score = 3
        elif(income < 7500 and (income >= 5000 or income < 7500)):
            score = 2
        elif(income <= 10000 and (income >= 7500 or income <=10000)):
            score = 1
        else:
            score = 0
        
        return score
    
    def _education_score(self,education):
        if(education.casefold() == ELEMENTARY_LEVEL.casefold() 
            or education.casefold() == ELEMENTARY_GRADUATE.casefold()):
            score = 1
        else:
            score = 0
        
        return score

    def _type_of_house_score(self,type_of_house):
        if(type_of_house.casefold() == BAHAY_KUBO.casefold() 
            or type_of_house.casefold() == WOOD_BASED.casefold()):
            score = 1
        else:
            score = 0
        
        return score
    
    def _sanitary_ownership_score(self,sanitary_ownership):
        print(sanitary_ownership)
        if(sanitary_ownership.casefold() == SHARED.casefold()):
            print("Im in!!")
            score = 2
        else:
            score = 0
        
        return 0

    def _occupation_filter(self):
        occupation = self.params["profiles.employment.nature"]

        if(occupation.casefold() == "empty".casefold()):
            return ""
        else:
            return occupation

    def _amenities_counter(self):
        amenities = self.params["households.amenities_present_in_house"]
        ctr = 0

        for i in amenities:
            ctr += 1

        final_ctr = 3 - ctr

        return final_ctr

    def _height_to_metric(self,height):
        if height <= HEIGHT_NOT_METRIC:
            height = (height * FEET_TO_METER) / 100

        return height

    def risk_score_ncd_general(self):
        score = 0

        house_ownership = self.params["households.house_ownership"]
        id_type = self.params["identification.id1.type"]
        id_identifier = self.params["identification.id1.identifier"]
        
        occupation = self._occupation_filter()

        if(house_ownership.casefold() == INFORMAL_SETTLERS.casefold() or (id_type == "4Ps" and id_identifier != None)):
            score = 12
        elif(occupation != ""):
            income = self._typecase_monthly_income()
            education = self.params["profiles.education"]
            type_of_house = self.params["households.type_of_house"]
            sanitary_ownership = self.params["households.sanitary_ownership"]
            amenities_points = self._amenities_counter()

            score = (self._income_score(income) + self._education_score(education)
                    + amenities_points + self._type_of_house_score(type_of_house)
                    + self._sanitary_ownership_score(sanitary_ownership))

        return score