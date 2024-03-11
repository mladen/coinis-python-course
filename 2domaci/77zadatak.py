# lista = [1, 2, 3, 2, 4, 2]
lista = [4, 5, 6, 7, 9]

# provjeri da li je lista sortirana rastuce
sortirana = False

for i in range(len(lista) - 1):
    if lista[i] < lista[i + 1]:
        sortirana = True
    else:
        sortirana = False

print(sortirana)
