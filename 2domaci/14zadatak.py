prvi_proizvod = int(input("Unesite cijenu prvog proizvoda: "))
drugi_proizvod = int(input("Unesite cijenu drugog proizvoda: "))
treci_proizvod = int(input("Unesite cijenu treceg proizvoda: "))

sortirani_proizvodi = sorted([prvi_proizvod, drugi_proizvod, treci_proizvod])

# NOTE: Prva verzija
# print(f"Najjeftiniji proizvodi su {sortirani_proizvodi[0]} i {sortirani_proizvodi[1]}")

# NOTE: Druga verzija
najjeftiniji_proizvodi = sortirani_proizvodi[:2]
print(
    f"Najjeftiniji proizvodi su {najjeftiniji_proizvodi[0]} i {najjeftiniji_proizvodi[1]}"
)
