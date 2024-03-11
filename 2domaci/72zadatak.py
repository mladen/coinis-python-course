lista_ocjena = [6, 5, 7, 8, 6, 7, 5, 9, 5, 10]
lista_ocjena_bez_ocjene_pet = []

# NOTE: Jedan nacin da se uklone sve ocjene 5
# lista_ocjena_bez_ocjene_pet = [i for i in lista_ocjena if i != 5]
# print(lista_ocjena_bez_ocjene_pet)

# NOTE: Drugaciji nacin da se uklone sve ocjene 5, posto jos nismo radili "list comprehentions"
for ocjena in lista_ocjena:
    if ocjena != 5:
        lista_ocjena_bez_ocjene_pet.append(ocjena)

prosjecna_ocjena = sum(lista_ocjena_bez_ocjene_pet) / len(lista_ocjena_bez_ocjene_pet)
print(f"Prosjecna ocjena je {prosjecna_ocjena}.")

brojac = 0

for ocjena in lista_ocjena_bez_ocjene_pet:
    if ocjena > prosjecna_ocjena:
        brojac += 1

print(f"Ocjenu vecu od prosjecne je dobilo {brojac} ucenika.")
