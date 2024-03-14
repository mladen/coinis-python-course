def najduzi_testerasti_podniz(lista):
    max_duzina = 0
    trenutna_duzina = 0

    maksimalni_niz = []
    trenutni_niz = []

    for i in range(
        len(lista) - 1
    ):  # -1 jer gledamo i i i+1 (poslednji element nema i+1 sa kim bi se uporedio)
        trenutni_niz.append(lista[i])
        trenutna_duzina += 1

        if lista[i] >= lista[i + 1]:
            trenutna_duzina = 0
            trenutni_niz = []
            # resetujemo trenutnu duzinu i niz
            # ali maksimalna duzina ostaje ista

        if trenutna_duzina > max_duzina:
            max_duzina = trenutna_duzina
            maksimalni_niz = trenutni_niz
    return maksimalni_niz


# Testiranje funkcije
# lista = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]
lista = [1, 2, 3, 2, 1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1]
print("Najduzi testerasti podniz:", najduzi_testerasti_podniz(lista))
