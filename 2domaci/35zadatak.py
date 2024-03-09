recenica_sa_ciframa = str(
    input("Unesite recenicu sa ciframa: ")
)  # Npr. "Hi Mr. Rober53. How are you today? Today is 08.10.2019”, stampa 5308102019

broj = ""

for karakter in recenica_sa_ciframa:
    if karakter.isdigit():
        broj += karakter

print(f"Broj iz recenice {recenica_sa_ciframa} je {int(broj)}.")
