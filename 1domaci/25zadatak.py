rastojanje_cm = int(
    input("Unesite rastojanje izmedju ulaza u kancelarije u centimetrima: ")
)

# Racunanje broja cijelih metara
broj_metara = rastojanje_cm // 100

# Ispis rezultata
print("U datom rastojanju ima", broj_metara, "cijelih metara.")
