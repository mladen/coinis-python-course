import math

lista_brojeva = [39, 542, 123, 9, 49, 64, 65]

cijeli_brojevi = []

for broj in lista_brojeva:
    kvadratni_korijen = math.sqrt(broj)
    if kvadratni_korijen.is_integer():
        cijeli_brojevi.append(kvadratni_korijen)
        # print(
        #     f"Broj {broj} ima kvadratni korijen {kvadratni_korijen} koji je cijeli broj."
        # )

print(
    f"Ukupan broj brojeva ciji kvadratni korijen je cijeli broj je {len(cijeli_brojevi)}"
)
