# NOTE: Rjesenje ChatGPT-a (nije dobro)
# def broj_golova(zbir):
#     # Razdvajamo zbir na pojedinačne cifre i sumiramo ih
#     cifre_zbira = sum(map(int, str(zbir)))
#     # Broj golova je zbir cifara podeljen sa 2, jer svaki gol ima dve cifre
#     broj_golova = cifre_zbira // 2
#     return broj_golova


# # Testiranje funkcije
# petrov_zbir = int(input("Unesite Petrov zbir: "))
# print("Broj golova na utakmici je:", broj_golova(petrov_zbir))

# NOTE: Moje rjesenje:
# NOTE: Svaki gol se prijavljuje sa dvije cifre (ili je gol postigao jedan tim ili drugi tim, ne moze i jedan i drugi)
# Dakle, kada jedan tim postigne gol, imamo 1:0. Kada neko opet postigne gol, imamo npr. 2:0...
# 1:0 - +1 gol
# 2:0 - +1 gol
# 2:1 - +1 gol
zbir_rezultata = int(input("Unesite zbir rezultata: "))
niz = []

brojac = 0

while sum(niz) < zbir_rezultata:
    # for i in range(zbir_rezultata):
    brojac += 1
    niz.append(brojac)


print(f"Broj golova je {niz[-1]}")

# TODO: Moje rjesenje je dobro, ali hocu da napravim neko ljepse...
