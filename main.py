import json
from my_functions import build_person, build_experiment
from my_classes import Person, Experiment


# Hauptfunktion
def main():
    # Experiment-Informationen
    experiment_name = input("Name des Experiments: ")
    date = input("Datum (dd.mm.yyyy): ")

    # Informationen zum Supervisor und Versuchsperson
    print("Geben Sie die Informationen für den Supervisor ein:")
    supervisor = Person(
        first_name=input("Vorname: "),
        last_name=input("Nachname: "),
        sex=input("Geschlecht (male/female): "),
        age=int(input("Alter: "))
    )

    print("Geben Sie die Informationen für die Versuchsperson ein:")
    subject = Person(
        first_name=input("Vorname: "),
        last_name=input("Nachname: "),
        sex=input("Geschlecht (male/female): "),
        age=int(input("Alter: "))
    )

    # Erstellen des Experiment-Objekts
    experiment = Experiment(experiment_name, date, supervisor, subject)

    # Drucken der Experimentdetails
    print("\nExperiment-Details:")
    print(experiment.to_dict())

    # Speichern der Daten in einer JSON-Datei
    experiment.save("experiment_details.json")

if __name__ == "__main__":
    main()