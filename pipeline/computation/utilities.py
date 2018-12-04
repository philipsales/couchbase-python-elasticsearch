FEET_TO_INCH = .3048
HEIGHT_NOT_METRIC = 10.0
INFORMAL_SETTLERS = "Informal settlers"
UNDERWEIGHT = "Underweight"
NORMAL = "Normal"
OVERWEIGHT = "Overweight"
OBESE = "Obese"
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
                
            # Computation of BMI
            bmi = weight / (final_height * final_height)

            # Assigning the BMI result
            bmi_result = self._categorize_bmi(bmi)
        # This happens when height and weight is a string
        except TypeError:
            bmi_result = ""
        
        # This happens when the values are zeros
        except ZeroDivisionError:
            bmi_result = ""
            
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

        if(house_ownership == INFORMAL_SETTLERS or (id_type == "4Ps" and id_identifier != None)):
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

        if bmi <= 18.5:
            bmi_result = UNDERWEIGHT
        elif 18.6 <= bmi <= 24.9:
            bmi_result = NORMAL
        elif 25 <= bmi <= 29.9:
            bmi_result = OVERWEIGHT
        elif bmi >= 30:
            bmi_result = OBESE
        
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
            monthly_income = float(self.params["profiles.employment.monthly_income"])
        except ValueError:
            monthly_income = 0.0
        
        return monthly_income

    def _income_score(self,income):
        if(income < 1000):
            score = 5
        elif(income >= 1000 or income < 2500):
            score = 4
        elif(income >= 2500 or income < 5000):
            score = 3
        elif(income >= 5000 or income < 7500):
            score = 2
        elif(income >= 7500 or income <=10000):
            score = 1
        else:
            score = 0
        
        return score
    
    def _education_score(self,education):
        if(education == ELEMENTARY_LEVEL or education == ELEMENTARY_GRADUATE):
            score = 1
        else:
            score = 0
        
        return score

    def _type_of_house_score(self,type_of_house):
        if(type_of_house == BAHAY_KUBO or type_of_house == WOOD_BASED):
            score = 1
        else:
            score = 0
        
        return score
    
    def _sanitary_ownership_score(self,sanitary_ownership):
        
        if(sanitary_ownership.casefold() == SHARED.casefold()):
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

        return ctr

    def _height_to_metric(self,height):
        if height <= HEIGHT_NOT_METRIC:
            height = height * FEET_TO_INCH

        return height