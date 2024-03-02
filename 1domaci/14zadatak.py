def procjena_cijene_stana(velicina, lokacija, parking):
    cijena_kvadrata = 1200
    fiksna_cijena_ucesca = 1000

    # Preracunavanje lokacije na osnovu zone
    if lokacija == 1:
        faktor_lokacije = 3
    elif lokacija == 2:
        faktor_lokacije = 2
    else:
        faktor_lokacije = 1

    # Preracunavanje dostupnosti parkinga
    faktor_parkinga = 1 if parking else 0

    # Racunanje cene stana
    cijena = (
        # TODO: Ovo jos nije zavrseno
        # velicina * faktor velicine + lokacija * faktor lokacije + ukupna lokacija * faktor parkinga
        velicina
        + faktor_lokacije * 5
        + faktor_parkinga * 10
    ) * cijena_kvadrata + fiksna_cijena_ucesca

    return cijena


# Unos parametara stana
velicina = float(input("Unesite velicinu stana (u kvadratnim metrima): "))
lokacija = int(
    input(
        "Unesite lokaciju stana (1 - uzi centar, 2 - siri centar ili 3 - periferija): "
    )
)
parking = int(input("Da li stan ima parking? (1 - ima, 0 - nema): "))

# Izracunavanje cene stana
cijena_stana = procjena_cijene_stana(velicina, lokacija, parking)

# Ispis rezultata
print("Procenjena cijena stana iznosi:", cijena_stana, "eura")
