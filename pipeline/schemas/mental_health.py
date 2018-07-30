import sys

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        
    def extract_mental_health(self):
        for i in self.arr:
            #id should be here
            self.extracted.append(i["mental_health"])

        return self.extracted

    def clean_data(self):
        self.extract_mental_health()
        pass
    
    def mapExtracted(self):
        pass