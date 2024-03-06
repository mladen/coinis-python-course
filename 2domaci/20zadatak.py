unijeti_broj = int(input("Unesi broj: "))

if unijeti_broj % 2 == 0:
    print("Broj je paran")

    suma_parnih_cifara = 0

    for cifra in str(unijeti_broj):
        if int(cifra) % 2 == 0:
            suma_parnih_cifara += int(cifra)

    print(f"Suma parnih cifara broja {unijeti_broj} je {suma_parnih_cifara}")
else:
    print("Broj je neparan")

    proizvod_neparnih_cifara = 1

    for cifra in str(unijeti_broj):
        if int(cifra) % 2 != 0:
            proizvod_neparnih_cifara *= int(cifra)

    print(
        f"Proizvod neparnih cifara broja {unijeti_broj} je {proizvod_neparnih_cifara}"
    )
