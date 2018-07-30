import sys

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        
    def extract_child_health(self):
        for i in self.arr:
            #id should be here
            self.extracted.append(i["child_health"])

        return self.extracted

    def clean_data(self):
        self.extract_child_health()
        pass
    
    def mapExtracted(self):
        pass