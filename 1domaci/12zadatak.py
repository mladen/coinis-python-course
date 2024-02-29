import datetime


def godina_mjesec_rodjenja(
    danasnja_godina, danasnji_mjesec, godine_danas, mjeseci_danas
):
    # Izracunavanje godine rodjenja
    godina_rodjenja = danasnja_godina - godine_danas

    # Izracunavanje mjeseca rodjenja
    mjesec_rodjenja = danasnji_mjesec - mjeseci_danas

    # Ako je rezultat manji od 1, godinu treba smanjiti za 1, a mjesec prebaciti u opseg od 1 do 12
    if mjesec_rodjenja < 1:
        godina_rodjenja -= 1
        mjesec_rodjenja += 12

    return godina_rodjenja, mjesec_rodjenja


# Unos trenutnog datuma
danasnji_datum = datetime.datetime.now()
danasnja_godina = danasnji_datum.year
danasnji_mjesec = danasnji_datum.month

# Unos broja godina koje Milos ima danas
godine_danas = int(input("Unesite koliko godina Milos ima danas: "))

# Unos broja mjeseci u trenutnoj godini
mjeseci_danas = int(input("Unesite koliko mjeseci ima trenutno u ovoj godini: "))

# Racunanje godine i mjeseca rodjenja Milosa
godina, mjesec = godina_mjesec_rodjenja(
    danasnja_godina, danasnji_mjesec, godine_danas, mjeseci_danas
)

# Ispis rezultata
print("Milos je rodjen {} godine i {} mjeseca.".format(godina, mjesec))
