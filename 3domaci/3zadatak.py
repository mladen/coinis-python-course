def najduzi_testerasti_podniz(lista):
    max_duzina = 0
    # trenutna_duzina = 0

    maksimalni_niz = []
    trenutni_niz = []

    trenutni_niz.append(lista[0])
    trenutna_duzina = 1

    print("Trenutni niz:", trenutni_niz)

    for i in range(
        1, len(lista)
    ):  # -1 jer gledamo i i i+1 (poslednji element nema i+1 sa kim bi se uporedio)
        print("Trenutno gledamo element:", lista[i])

        if lista[i - 1] >= lista[i]:
            trenutna_duzina = 0
            trenutni_niz = []
            trenutni_niz.append(lista[i])
            # resetujemo trenutnu duzinu i niz
            # ali maksimalna duzina ostaje ista
            # takodje, posto krecemo iz pocetka, dodajemo ovaj element kao prvi u niz
        else:
            trenutni_niz.append(lista[i])
            trenutna_duzina += 1

        if trenutna_duzina > max_duzina:
            max_duzina = trenutna_duzina
            maksimalni_niz = trenutni_niz

        print("Trenutni niz:", trenutni_niz)
        print("Maksimalni niz:", maksimalni_niz)
        print("-------------------")
    return maksimalni_niz


# Testiranje funkcije
# lista = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]
lista = [1, 2, 3, 2, 1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7]
print("Najduzi testerasti podniz:", najduzi_testerasti_podniz(lista))
