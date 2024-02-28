duzina_ograde = lambda d, s, r: 2 * (d + 2 * r) + 2 * (s + 2 * r)

# Unos dimenzija terena i rastojanja ograde
d = int(input("Unesite duzinu terena u metrima: "))
s = int(input("Unesite sirinu terena u metrima: "))
r = int(input("Unesite rastojanje ograde od terena u metrima: "))

# Racunanje duzine ograde
duzina = duzina_ograde(d, s, r)

# Ispis rezultata
print("Duzina ograde je:", duzina, "metara.")
