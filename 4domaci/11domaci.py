import os
from pprint import pprint
from functools import reduce

# from functools import reduce

cwd = os.getcwd()  # Get the current working directory (cwd)

drzava_koju_je_korisnik_izabrao = input(
    "Unesite ime drzave: "
)  # input() uvijek vraca string

try:
    with open(cwd + "/4domaci/population.txt", "r") as file:
        read_content = file.read()
        print(read_content)

        print("\n")

        svi_podaci = [red.split(",") for red in read_content.split("\n")]
        pprint(svi_podaci)

        izabrana_drzava = list(
            filter(
                lambda drzava: drzava[0] == drzava_koju_je_korisnik_izabrao, svi_podaci
            )
        )
        print(f"\n\nIzabrana drzava: {izabrana_drzava}")

        broj_stanovnika = reduce(
            lambda ukupna_populacija_acc, drzava: ukupna_populacija_acc
            + int(drzava[2]),
            izabrana_drzava,
            0,
        )

        print(f"Drzava {izabrana_drzava[0][0]} ima {broj_stanovnika} stanovnika.")
except FileNotFoundError:
    print("Fajl nije pronadjen")
except Exception as e:
    print(f"Doslo je do greske: {e}")
