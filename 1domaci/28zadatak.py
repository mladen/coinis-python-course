broj = int(input("Unesite trocifreni broj: "))

# Izdvajanje cifara broja
prva_cifra = broj // 100
srednja_cifra = (broj % 100) // 10
zadnja_cifra = broj % 10

novi_broj = zadnja_cifra * 100 + srednja_cifra * 10 + prva_cifra

# NOTE: (drugi nacin) Mozemo samo trocifreni broj prebaciti u string i onda zamijeniti prvu i zadnju cifru

print("Novi broj je:", novi_broj)
