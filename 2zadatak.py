import math


def izracunaj_korijen(a, b, c):
    diskriminanta = b**2 - 4 * a * c
    if diskriminanta < 0:
        return None, None
    else:
        x1 = (-b + math.sqrt(diskriminanta)) / (2 * a)
        x2 = (-b - math.sqrt(diskriminanta)) / (2 * a)
        return x1, x2


a = float(input("Unesite koeficijent a: "))
b = float(input("Unesite koeficijent b: "))
c = float(input("Unesite koeficijent c: "))

x1, x2 = izracunaj_korijen(a, b, c)

if x1 is None:
    print("Nema realnih rjesenja.")
else:
    print("x1 =", x1)
    print("x2 =", x2)
