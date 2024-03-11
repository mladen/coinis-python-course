lista_cijelih_brojeva = [55, 2, 321, 167, 23, 44, 216, 832, 3, 111]
dvocifreni_brojevi = []
trocifreni_brojevi = []

for broj in lista_cijelih_brojeva:
    if len(str(broj)) == 2:
        dvocifreni_brojevi.append(broj)
    elif len(str(broj)) == 3:
        trocifreni_brojevi.append(broj)

print(f"Dvocifrenih brojeva ima {len(dvocifreni_brojevi)}")
print(f"Trocifrenih brojeva ima {len(trocifreni_brojevi)}")
