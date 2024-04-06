import os
from pprint import pprint
from functools import reduce


cwd = os.getcwd()  # Get the current working directory (cwd)

# Open csv file
try:
    with open(cwd + "/salaries.csv", "r") as file:
        read_content = file.read()
        # print(read_content)

        # print("\n")

        svi_podaci = [red.split(",") for red in read_content.split("\n")]
        # print(svi_podaci[2])

        salary = []

        for index in range(len(svi_podaci) - 1):
            # print(svi_podaci[index])
            # broj = int(float((svi_podaci[index][4].strip())))
            broj = svi_podaci[index][4].strip()
            salary.append(broj)

        # print(type(salary[0]))

        cleaned_values = []

        for value in salary:
            # Clean the string (e.g., remove commas)
            cleaned_value = value.replace(",", "")  # Remove commas
            try:
                new_value = int(float(cleaned_value))
                cleaned_values.append(new_value)
            except ValueError:
                print(f"Could not convert {value} to float")

        print(f"Maksimalna vrijednost: {max(cleaned_values)}")
        print(f"Minimalna vrijednost: {min(cleaned_values)}")

        # Prosjecna vrijednost
        suma = 0
        for value in cleaned_values:
            suma += value

        prosjek = suma / len(cleaned_values)

        print(f"Prosjecna vrijednost: {prosjek}")

        # Procentualna razlika izmedju maksimalne i prosjecne vrijednosti
        razlika = max(cleaned_values) - prosjek
        procenat = (razlika / prosjek) * 100

        print(
            f"Procentualna razlika izmedju maksimalne i prosjecne vrijednosti: {procenat}%"
        )

        # salaries = [
        #     int(red[4]) for red in svi_podaci[1:] # TODO: Provjeriti ovo
        # ]  # Gets all salaries from 4th column
        # print(len(salaries))

except FileNotFoundError:
    print("Fajl nije pronadjen")
except Exception as e:
    print(f"Doslo je do greske: {e}")
