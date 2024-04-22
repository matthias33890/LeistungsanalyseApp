import json
from my_functions import build_person, build_experiment
from my_classes import Subject, Supervisor, Experiment
import os

# Hauptfunktion
def main():
    # Experiment-Informationen
    experiment_name = input("Name des Experiments: ")
    date = input("Datum (dd.mm.yyyy): ")

    # Informationen zum Supervisor und Versuchsperson
    print("Geben Sie die Informationen für den Supervisor ein:")
    supervisor = Supervisor(
        first_name=input("Vorname: "),
        last_name=input("Nachname: "),
        department=input("Abteilung: "),
    )

    print("Geben Sie die Informationen für die Versuchsperson ein:")
    subject = Subject(
        first_name=input("Vorname: "),
        last_name=input("Nachname: "),
        sex=input("Geschlecht (male/female): "),
        birthdate=input("Geburtsdatum (DD.MM.YYYY): ")
    )

    # Erstellen des Experiment-Objekts
    experiment = Experiment(experiment_name, date, f"{supervisor.first_name} {supervisor.last_name}" ,f"{subject.first_name} {subject.last_name}")

    # Drucken der Experimentdetails
    print("\nExperiment-Details:")
    print(experiment.__dict__)
    print(supervisor.__dict__)
    print(subject.__dict__)

    # Ordner "jsons" erstellen, falls er noch nicht existiert
    if not os.path.exists("jsons"):
        os.makedirs("jsons")
    
    # Speichern der Daten in einer JSON-Datei
    experiment.save("jsons/experiment_details.json")
    supervisor.save("jsons/supervisor_details.json")
    subject.save("jsons/subject_details.json")


if __name__ == "__main__":
    main()