def generisi_sifru(broj):
    prva_cifra = broj // 1000
    druga_cifra = (broj % 1000) // 100
    treca_cifra = (broj % 100) // 10
    cetvrta_cifra = broj % 10

    zbir_kvadrata_prve_i_poslednje = (prva_cifra**2) + (cetvrta_cifra**2)
    razlika_kvadrata_druge_i_trece = (druga_cifra**2) - (treca_cifra**2)

    sifra = zbir_kvadrata_prve_i_poslednje - razlika_kvadrata_druge_i_trece
    return sifra


# Unos cetvorocifrenog broja
broj = int(input("Unesite cetvorocifreni broj: "))

# Generisanje sifre
sifra = generisi_sifru(broj)

# Ispis rezultata
print("Generisana sifra za otvaranje sefa je:", sifra)
