import os
from pprint import pprint

# from functools import reduce

cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

drzava_koju_je_korisnik_izabrao = str(input("Unesite ime grada: "))

with open(cwd + "/4domaci/population.txt", "r") as file:
    read_content = file.read()
    print(read_content)

    print("\n")

    svi_podaci = [red.split(",") for red in read_content.split("\n")]
    pprint(svi_podaci)

    izabrana_drzava = list(
        filter(lambda grad: grad[0] == drzava_koju_je_korisnik_izabrao, svi_podaci)
    )
    print(f"\n\nIzabrana drzava: {izabrana_drzava}")

    # sorting data by the item with index 1 (which is the name of the city; ['Njemacka', 'Berlin', '3769000']) in a sublist
    sortirani_gradovi = sorted(izabrana_drzava, key=lambda x: int(x[2]))
    print(
        f"\n\nDio grada sa najvecim brojem stanovnika je {sortirani_gradovi[0][1]}"
    )  # Input: Njemacka; Output: Dortmund
