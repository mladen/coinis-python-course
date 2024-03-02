import math


def euklidsko_rastojanje(tacka1, tacka2):
    # Izracunavanje Euklidskog rastojanja izmedju dvije tacke
    return math.sqrt((tacka2[0] - tacka1[0]) ** 2 + (tacka2[1] - tacka1[1]) ** 2)


def povrsina_trougla(t1, t2, t3):
    # Izracunavanje duzina stranica trougla
    a = euklidsko_rastojanje(t1, t2)
    b = euklidsko_rastojanje(t2, t3)
    c = euklidsko_rastojanje(t3, t1)

    # Poluobim trougla
    s = (a + b + c) / 2

    # Izracunavanje povrsine trougla pomocu Heronove formule
    povrsina = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return povrsina


# Unos koordinata tjemena trougla
x1, y1 = map(
    float, input("Unesite koordinate prvog tjemena trougla (x1, y1): ").split(",")
)
x2, y2 = map(
    float, input("Unesite koordinate drugog tjemena trougla (x2, y2): ").split(",")
)
x3, y3 = map(
    float, input("Unesite koordinate treceg tjemena trougla (x3, y3): ").split(",")
)

# Formiranje tacaka na osnovu unijetih koordinata
t1 = (x1, y1)
t2 = (x2, y2)
t3 = (x3, y3)

# Izracunavanje povrsine trougla
povrsina = povrsina_trougla(t1, t2, t3)

# Ispis rezultata
print("Povrsina trougla je:", povrsina)
