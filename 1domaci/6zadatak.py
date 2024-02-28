kvadrat_trinoma = lambda a, b, c: a**2 + b**2 + c**2 + 2 * a * b + 2 * a * c + 2 * b * c

a = float(input("Unesite vrijednost parametra a: "))
b = float(input("Unesite vrijednost parametra b: "))
c = float(input("Unesite vrijednost parametra c: "))

rezultat = kvadrat_trinoma(a, b, c)

print(f"Kvadrat trinoma za parametre a={a}, b={b} i c={c} je: {rezultat}")
