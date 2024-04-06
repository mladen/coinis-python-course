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
            broj = int(svi_podaci[index][4].strip())
            salary.append(broj)

        print(type(salary[0]))

        # salaries = []

        # print(len(salaries))

        # salaries = [
        #     int(red[4]) for red in svi_podaci[1:] # TODO: Provjeriti ovo
        # ]  # Gets all salaries from 4th column
        # print(len(salaries))

except FileNotFoundError:
    print("Fajl nije pronadjen")
except Exception as e:
    print(f"Doslo je do greske: {e}")
