broj = int(input("Unesite broj: "))

suma_cifara = 0

for cifra in str(broj):
    suma_cifara += int(cifra)

print(f"Suma cifara broja {broj} je {suma_cifara}.")
