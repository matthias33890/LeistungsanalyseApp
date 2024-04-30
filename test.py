import json
from my_functions import build_person, build_experiment
from my_classes import Subject, Supervisor, Experiment, Person
import os

# Hauptfunktion
def main():
    # Informationen zum Person und Versuchsperson
    print("Geben Sie die Informationen für die Person ein:")
    person = Person(
        first_name=input("Vorname: "),
        last_name=input("Nachname: "),
    )
    print("Geben Sie die Informationen für die Versuchsperson ein:")
    subject = Subject(
        first_name=input("Vorname: "),
        last_name=input("Nachname: "),
        sex=input("Geschlecht (male/female): "),
        birthdate=input("Geburtsdatum (DD.MM.YYYY): "),
        email=input("E-Mail: ")
    )
    input("Press Enter to continue...")
    Person.put(person)
    Subject.update_email(subject)

if __name__ == "__main__":
    main()