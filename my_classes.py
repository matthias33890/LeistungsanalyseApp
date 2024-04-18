import json
import my_functions

class Person:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = self.estimate_max_hr()
        
    def estimate_max_hr(self):
        return my_functions.estimate_max_hr(self.age, self.sex)
    
    def save(self, filename):
        # Speichert die Experimentdetails als JSON-Datei
        with open(filename, "w") as outfile:
            json.dump(self.__dict__, outfile)
    
class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        
    
    def save(self, filename):
        # Speichert die Experimentdetails als JSON-Datei
        with open(filename, "w") as outfile:
            json.dump(self.__dict__, outfile)