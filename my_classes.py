import json

class Person:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.__dict__ = self.__to_dict__()
        
    def estimate_max_hr(self):
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

        
    def __to_dict__(self):
        # Konvertiert die Attribute der Person in ein Dictionary
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age,
            "estimated_max_hr": self.estimate_max_hr()
        }
    
    def save(self, filename):
        # Speichert die Experimentdetails als JSON-Datei
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)
    
class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject
        self.__dict__ = self.__to_dict__()
        
    def save(self, filename):
        # Speichert die Experimentdetails als JSON-Datei
        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile)
    
    def __to_dict__(self):
        # Konvertiert die Attribute des Experiments in ein Dictionary
        return {
            "name": self.name,
            "date": self.date,
            "supervisor": self.supervisor.to_dict(),
            "subject": self.subject.to_dict()
        }