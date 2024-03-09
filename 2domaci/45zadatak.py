plate = [500, 450, 700, 800, 1000, 1200, 750]

prosjecna_plata = sum(plate) / len(plate)

broj_plata_vecih_od_prosjecne = 0

for indeks, plata in enumerate(plate):
    if plata > prosjecna_plata:
        broj_plata_vecih_od_prosjecne += 1

print(
    f"Prosjecna plata je {prosjecna_plata}, a broj broj zaposlenih koji imaju platu koja je veca od prosjecne je {broj_plata_vecih_od_prosjecne}."
)
