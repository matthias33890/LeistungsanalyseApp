import json
from datetime import datetime
import my_functions

class Person:
    def __init__(self, first_name, last_name): #Hier brauchen wir nun nur noch Vor- und Nachnamen
        self.first_name = first_name
        self.last_name = last_name
    
    def save(self, filename):
        # Save the experiment details as a JSON file
        with open(filename, "w") as outfile:
            json.dump(self.__dict__, outfile)

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate): # Beim Subjekt brauchen wir zusätzlich noch Geschlecht und Geburtsdatum
        super().__init__(first_name, last_name) # hier ist ein zusätzliches Attribut unnötig.
        self.sex = sex
        self.__birthdate__ = birthdate  # Hidden attribute for birthdate
        self.age = self.calculate_age()
        self.max_hr = self.estimate_max_hr()

    def calculate_age(self):
        today = datetime.now()
        birthdate = datetime.strptime(self.__birthdate__, '%d.%m.%Y')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return int(age)

    def estimate_max_hr(self):
        return my_functions.estimate_max_hr(self.age, self.sex)

class Supervisor(Person):
    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name)
        self.department = department  # Zusätzliches Attribut für Supervisor

class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
            # Save the experiment details as a JSON file
        with open(filename, "w") as outfile:
            json.dump(self.__dict__, outfile)
