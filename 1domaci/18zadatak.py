def cijena_ps5_konzole(cijena):
    nova_cijena = cijena + (cijena * 10 / 100)

    return nova_cijena - (nova_cijena * 10 / 100)


cijena = float(input("Unesite cijenu knjige: "))

print(
    "Cijena knjige nakon povecanja i nakon popusta iznosi:",
    cijena_ps5_konzole(cijena),
)
