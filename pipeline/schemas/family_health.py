import sys

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        
    def extract_family_health(self):
        for i in self.arr:
            #id should be here
            #add family_planning_male
            self.extracted.append(i["family_planning_and_maternal_health"])

        return self.extracted

    def clean_data(self):
        self.extract_family_health()
        pass
    
    def mapExtracted(self):
        pass