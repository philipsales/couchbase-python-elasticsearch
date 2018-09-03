class BMI:
    def __init__(self, _json):
        self.bmi_result = ""
        self.height = _json["health_informations.height"]
        self.weight = _json["health_informations.weight"]

    def _do_computation(self):
        try:

            variable = self._typecast()

            (height, weight) = (variable["height"], variable["weight"])

            # If height is less than 10, the height is probably not in metric
            if height <= 10.0:
                # So.. we convert it to metric (inch)
                height = height * .3048
                
            # Computation of BMI happens here
            bmi = weight / (height * height)

            # Assigning the BMI result here
            self.bmi_result = self._categorize_bmi(bmi)
        # This happens when height and weight is a string
        except TypeError:
            self.bmi_result = ""
        
        # This happens when the values are zeros
        except ZeroDivisionError:
            self.bmi_result = ""
        
        return self.bmi_result
    
    def _categorize_bmi(self,bmi):
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
            height = int(self.height)
            weight = int(self.weight)

        # If values are empty strings...
        except ValueError:
            height = 0.0
            weight = 0.0

        return {"height": height, "weight": weight}