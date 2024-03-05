prisustvo = int(input("Unesite procenat prisustva: "))
svi_seminarski_uradjeni = int(
    input(
        "Unesite 1 za 'student je uradio sve seminarske ili 2 - student nije uradio barem jedan seminarski: "
    )
)

if prisustvo > 75 and svi_seminarski_uradjeni == 1:
    print("Student moze da pristupi ispitu.")
else:
    print("Student ne moze da pristupi ispitu.")
