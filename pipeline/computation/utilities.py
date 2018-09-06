FEET_TO_INCH = .3048
HEIGHT_NOT_METRIC = 10.0

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
        org = self.params["Organization"]
        return org.replace("_"," ")

    '''
    INTERNAL FUNCTIONS ONLY

    used by the external functions
    '''
    
    def _categorize_bmi(self,bmi):
        bmi_result=""

        if bmi <= 18.5:
            bmi_result = "Underweight"
        elif 18.6 <= bmi <= 24.9:
            bmi_result = "Normal"
        elif 25 <= bmi <= 29.9:
            bmi_result = "Overweight"
        elif bmi >= 30:
            bmi_result = "Obese"
        
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
            height = height * FEET_TO_INCH

        return height