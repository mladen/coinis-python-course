lista = [1, 2, 3, 2, 4, 2]
print("Stara lista: ", lista)

broj_koji_mijenjamo = 2
novi_broj = -2

for i in range(len(lista)):
    if lista[i] == broj_koji_mijenjamo:
        lista[i] = novi_broj

print("Nova list: ", lista)
