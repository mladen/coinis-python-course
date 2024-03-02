broj = int(input("Unesite sestocifreni broj: "))

# Izdvajanje cifara broja
c1 = broj // 100000
c2 = (broj // 10000) % 10
c3 = (broj // 1000) % 10
c4 = (broj // 100) % 10
c5 = (broj // 10) % 10
c6 = broj % 10

# TODO: Uraditi kasnije uz pomoc ovog trika!
# Izdvajanje cifara broja koristeci string, koliki god da je broj (uz pomoc for petlje)
# for cifra in str(broj):
#     print(f"c{cifra}")
#     globals()[f"c{cifra}"] = int(cifra)

suma_cifara = c1 + c2 + c3 + c4 + c5 + c6

kvadrat_sume_cifara = suma_cifara**2

proizvod_trece_i_cetvrte_cifre = c3 * c4

# Izracunavanje specijalnog identifikacionog broja
identifikacioni_broj = kvadrat_sume_cifara - proizvod_trece_i_cetvrte_cifre

print("Specijalni identifikacioni broj je:", identifikacioni_broj)
