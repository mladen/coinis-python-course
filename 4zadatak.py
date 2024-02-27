def obim_terena(d, s):
    return 2 * (d + s)


def ukupna_distanca(d, s):
    return 4 * obim_terena(d, s)


duzina = float(input("Unesite duzinu terena (d): "))
sirina = float(input("Unesite sirinu terena (s): "))

distanca = ukupna_distanca(duzina, sirina)

print(f"Sportista će pretrcati ukupno {distanca} metara dok obidje teren 4 puta.")
