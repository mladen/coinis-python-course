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


def get_students_with_greater_grade(year, grade):
    try:
        with open(file_path, "r") as file:
            students = file.read()

            all_data = [row.split(",") for row in students.split("\n")]
            all_data = [
                [data.strip(" ") for data in row] for row in all_data
            ]  # Strip the whitespace from the data
            print(f"All data: {all_data}\n")

            clean_data = (
                all_data[1:-1] if all_data[-1] == [""] else all_data[1:]
            )  # If the last element is an empty string, remove it. Else, just remove the first line (which contains the headers)

            print(f"Clean data: {clean_data}\n")

            if grade not in ["A", "B", "C", "D", "E"]:
                raise ValueError("Grade must be one of the following: A, B, C, D, E")

            if grade == "A":
                grade_max = 10
                grade_min = 9.5
            elif grade == "B":
                grade_max = 9.5
                grade_min = 8.5
            elif grade == "C":
                grade_max = 8.5
                grade_min = 7.5
            elif grade == "D":
                grade_max = 7.5
                grade_min = 6.5
            elif grade == "E":
                grade_max = 6.5
                grade_min = 6

            students_with_all_10s = filter(
                lambda student: int(student[2]) == year and float(student[3]) == 10,
                clean_data,
            )

            # print(f"Students with all 10s: {list(students_with_all_10s)}\n")

            other_students = filter(
                lambda student: (
                    int(student[2]) == year
                    and grade_min <= float(student[3]) < grade_max
                ),
                clean_data,
            )

            # TODO: Do the previous filtering using only one filter function

            all_found_students = list(other_students) + list(students_with_all_10s)
            print(all_found_students)
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Students successfully read from file!")


# get_students_with_greater_grade(3, "A")
get_students_with_greater_grade(2, "B")
