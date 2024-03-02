a = int(input("Unesite neki broj: "))
b = int(input("Unesite jos jedan broj: "))

srednja_vrijednost = lambda a, b: (a + b) / 2

print("Srednja vrijednost brojeva", a, "i", b, "iznosi:", srednja_vrijednost(a, b))
