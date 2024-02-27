def razlika_kvadrata(a, b):
    return (a**2) - (b**2)
    # return (a - b) * (a + b)


a = float(input("Unesite prvi broj (a): "))
b = float(input("Unesite drugi broj (b): "))

razlika = razlika_kvadrata(a, b)

print(f"Razlika kvadrata brojeva {a} i {b} je: {razlika}")
