FEET_TO_METER = .3048
HEIGHT_NOT_METRIC = 10.00

MINIMUM_BMI = 5.00
UNDERWEIGHT_CEILING = 18.59
NORMAL_FLOOR = 18.60
NORMAL_CEILING = 24.99
OVERWEIGHT_FLOOR = 25.00
OVERWEIGHT_CEILING = 29.99
OBESE_FLOOR = 30.00

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

            variable = self._typecast()

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

    def _typecast(self):
        try:
            # Convert height and weight to integer
            height = int(self.params["health_informations.height"])
            weight = int(self.params["health_informations.weight"])

        # If values are empty strings...
        except ValueError:
            height = 0.0
            weight = 0.0

        return {"height": height, "weight": weight}

    def _height_to_metric(self,height):
        if height <= HEIGHT_NOT_METRIC:
            height = (height * FEET_TO_METER) / 100

        return height