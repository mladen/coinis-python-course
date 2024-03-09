broj = int(input("Unesite broj: "))

zbir_parnih = 0
brojac_parnih = 0

proizvod_neparnih = 1
brojac_neparnih = 0

while broj > 0:
    cifra = broj % 10  # Ovo znaci da uzimamo poslednju cifru broja
    if cifra % 2 == 0:
        zbir_parnih += cifra
        brojac_parnih += 1
    else:
        proizvod_neparnih *= cifra
        brojac_neparnih += 1
    broj -= 1

print(
    f"Zbir parnih cifara je {zbir_parnih}, a proizvod neparnih cifara je {proizvod_neparnih}. Broj parnih cifara je {brojac_parnih}, a broj neparnih cifara je {brojac_neparnih}."
)
