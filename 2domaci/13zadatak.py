precnik_1_stola = int(input("Unesite precnik prvog stola: "))
precnik_2_stola = int(input("Unesite precnik drugog stola: "))


if (
    precnik_1_stola > precnik_2_stola
):  # Nije ni potrebno racunati povrsine, dovoljno je uporediti precnike
    print("Prvi sto je veci od drugog stola.")
else:
    print("Drugi sto je veci od prvog stola.")
