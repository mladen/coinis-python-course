lista_studenata = [
    "Ana",
    "Ivana",
    "Milica",
    "Pero",
    "Mirko",
    "Zivko",
    "Lazar",
    "Jovan",
    "Mara",
    "Mira",
]
lista_prosjecnih_ocjena = [7, 8, 9, 6, 7, 8, 9, 6, 7, 8]

print(list(zip(lista_studenata, lista_prosjecnih_ocjena)))

studenti_sa_vecim_prosjekom = []

for student, ocjena in zip(lista_studenata, lista_prosjecnih_ocjena):
    if ocjena > 8.5:
        studenti_sa_vecim_prosjekom.append((student, ocjena))

print(f"\n\nStudenti sa prosjekom vecim od 8.5: {studenti_sa_vecim_prosjekom}.")
