import json
from datetime import datetime
import my_functions
import requests
import json

#global attributes:
url = "http://127.0.0.1:5000/"

class Person:
    def __init__(self, first_name, last_name): #Hier brauchen wir nun nur noch Vor- und Nachnamen
        self.first_name = first_name
        self.last_name = last_name
    
    def save(self, filename):
        # Save the experiment details as a JSON file
        with open(filename, "w") as outfile:
            json.dump(self.__dict__, outfile)
    
    def put(self):
        data = {
            "name": self.first_name
        }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate, email): # Beim Subjekt brauchen wir zusätzlich noch Geschlecht und Geburtsdatum
        super().__init__(first_name, last_name) # hier ist ein zusätzliches Attribut unnötig.
        self.sex = sex
        self.__birthdate__ = birthdate  # Hidden attribute for birthdate
        self.age = self.calculate_age()
        self.max_hr = self.estimate_max_hr()
        self.email = email

    def calculate_age(self):
        today = datetime.now()
        birthdate = datetime.strptime(self.__birthdate__, '%d.%m.%Y')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return int(age)

    def estimate_max_hr(self):
        return my_functions.estimate_max_hr(self.age, self.sex)
    
    def update_email(self):
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)

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


