niz_cijelih_brojeva = [-2, 3, 6, 1, 0, -5, -6, 3]

suma = 0

for broj in niz_cijelih_brojeva:
    if broj < 0 and broj % 2 == 0:
        suma += abs(broj)

print(suma)
