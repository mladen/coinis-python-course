# Da malo vjezbam stvari unaprijed, koristicu lambda funkcije

izracunaj_povrsinu = lambda a, b: a * b
izracunaj_obim = lambda a, b: 2 * (a + b)

a = float(input("Unesite duzinu pravougaonika: "))
b = float(input("Unesite sirinu pravougaonika: "))

povrsina = izracunaj_povrsinu(a, b)
obim = izracunaj_obim(a, b)

print("Povrsina pravougaonika je:", povrsina)
print("Obim pravougaonika je:", obim)
