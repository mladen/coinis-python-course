lista_brojeva = [21, 4, 5, 21, 64, 21, 4]

uneseni_broj = int(
    input("Unesi broj kako bismo provjerili koliko puta se isti ponavlja: ")
)
broj_ponavljanja = 0

for broj in lista_brojeva:
    if broj == uneseni_broj:
        broj_ponavljanja += 1

if broj_ponavljanja == 0:
    print(f"Broj koji ste unijeli ne postoji u listi brojeva.")
else:
    print(f"Broj koji ste unijeli se ponavlja {broj_ponavljanja} puta.")
