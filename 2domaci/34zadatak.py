tekst_sa_ciframa = str(
    input("Unesite tekst sa ciframa: ")
)  # Npr. "1a2b3c4d5e6f7g8h9ij"

proizvod_cifara = 1

for karakter in tekst_sa_ciframa:
    if karakter.isdigit():
        proizvod_cifara *= int(karakter)

print(f"Proizvod cifara teksta {tekst_sa_ciframa} je {proizvod_cifara}.")
