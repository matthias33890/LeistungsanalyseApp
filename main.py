from calculation import calc_mean
from my_functions import build_experiment, build_person, estimate_max_hr

if __name__ == "__main__":
    
    # Verwendung der Funktionen aus calculation.py
    numbers = [10, 20, 30, 40, 50]
    mean_of_numbers = calc_mean(numbers)
    print(f"Mean of numbers: {mean_of_numbers}")

    # Verwendung der Funktionen aus my_functions.py
    age = 30
    sex = 'male'
    person = build_person("Matthias", "Hansen", sex, age)
    print(f"Person: {person}")

    experiment = build_experiment("Heart Rate Study", "2024-03-20", person, person)
    print(f"Experiment: {experiment}")

