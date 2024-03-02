def cijena_voznje(predjeni_km: float) -> float:
    cijena_po_1_km = 0.5  # Cijena je u EUR
    pocetna_cijena = 1  # Cijena je u EUR

    cijena_voznje = pocetna_cijena + (predjeni_km * cijena_po_1_km)
    return cijena_voznje


predjeni_km = float(input("Unesite broj predjenih kilometara: "))

cijena = cijena_voznje(predjeni_km)

print("Cijena voznje je:", cijena, "EUR")
