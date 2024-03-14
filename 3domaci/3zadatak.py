def najduzi_testerasti_podniz(lista):
    max_duzina = 0
    trenutna_duzina = 0

    trenutni_niz = []
    privremeni_niz = []

    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            privremeni_niz.append(lista[i])
            trenutna_duzina += 1

            print("Privremeni niz je: ", privremeni_niz)
        else:
            trenutna_duzina = 0
            privremeni_niz = []

        if trenutna_duzina > max_duzina:
            max_duzina = trenutna_duzina
            trenutni_niz = privremeni_niz
    # return max(max_duzina, trenutna_duzina)
    return trenutni_niz


# Testiranje funkcije
lista = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]
print("Najduzi testerasti podniz:", najduzi_testerasti_podniz(lista))
