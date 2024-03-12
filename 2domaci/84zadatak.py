# NOTE: Rjesenje ChatGPT-a (nije dobro)
# def dodatni_stolovi(gosti, stolovi):
#     slobodna_mjesta = sum(stol * 4 for stol in stolovi)
#     potrebno_mjesta = gosti - slobodna_mjesta
#     dodatni_stolovi = (potrebno_mjesta + 3) // 4  # Zaokruživanje na viši ceo broj
#     return dodatni_stolovi


# stolovi = [4, 6, 2, 8, 5]  # Kapaciteti stolova (broj mjesta po stolu)
# broj_gostiju = int(input("Unesite broj gostiju: "))

# dodatni = dodatni_stolovi(broj_gostiju, stolovi)
# print(f"Potrebno je dodatno nabaviti {dodatni} stolova.")

import math

kapacitet_stolova = [4, 6, 2, 8, 5]

broj_gostiju = 27

visak_gostiju = broj_gostiju - sum(kapacitet_stolova)
print(
    f"Imamo stolove za {sum(kapacitet_stolova)}. Visak gostiju je {visak_gostiju}, pa ce nam ukupno trebati {math.floor(broj_gostiju/4) + 1}"
)
