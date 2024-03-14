lista = [1, 2, 2, 2, 4, 4]
# lista = [1, 2, 3, 4, 5, 6]

proizvod_sekvence = 1
sekvenca_koja_daje_najveci_proizvod = []

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] * lista[j] > proizvod_sekvence:
            proizvod_sekvence = lista[i] * lista[j]
            sekvenca_koja_daje_najveci_proizvod = [lista[i], lista[j]]

print(
    f"Sekvenca koja daje najveci proizvod je: {sekvenca_koja_daje_najveci_proizvod}, a proizvod te sekvence je {proizvod_sekvence}"
)
