dimenzije_prozora_tuple = (
    int(input("Unesite sirinu prozora: ")),
    int(input("Unesite visinu prozora: ")),
)

dimenzije_zavjese_tuple = (
    int(input("Unesite sirinu zavjese: ")),
    int(input("Unesite visinu zavjese: ")),
)

if dimenzije_prozora_tuple[0] < dimenzije_zavjese_tuple[0]:
    print("Zavjesa je prevelika.")
elif dimenzije_prozora_tuple[1] < dimenzije_zavjese_tuple[1]:
    print("Zavjesa je prevelika.")
else:
    print("Zavjesa je odgovarajuca.")
