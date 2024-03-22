import os

cwd = os.getcwd()  # Get the current working directory (cwd)
file_path = os.path.join(cwd, "4domaci", "students.txt")


list_of_students = [
    {"ime": "Marko", "prezime": "Markovic", "godina": 2, "prosjek": 8.6},
    {"ime": "Boris", "prezime": "Boricic", "godina": 3, "prosjek": 7.9},
    {"ime": "Novak", "prezime": "Novovic", "godina": 3, "prosjek": 6.9},
]


def append_to_file(list_of_students):
    try:
        with open(file_path, "a") as file:
            file.write("Ime, Prezime, Godina, Prosjek\n")
            for student in list_of_students:
                if 1 <= student["godina"] <= 8 and 6 <= student["prosjek"] <= 10:
                    file.write(
                        f"{student['ime']}, {student['prezime']}, {student['godina']}, {student['prosjek']}\n"
                    )
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Students successfully appended to file!")


append_to_file(list_of_students)
