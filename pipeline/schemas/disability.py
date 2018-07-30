import sys

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        
    def extract_disability(self):
        for i in self.arr:
            #id should be here
            self.extracted.append(i["disability"])

        return self.extracted

    def clean_data(self):
        self.extract_disability()
        pass
    
    def mapExtracted(self):
        pass