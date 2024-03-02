x = int(input("Unesite vrijednost za Milicu: "))
y = int(input("Unesite vrijednost za Anu: "))

print("Prije zamjene:")
print("Milica =", x)
print("Ana =", y)

# Zamjena vrijednosti promjenljivih x i y
x, y = y, x

print("Posle zamjene:")
print("Milica =", x)
print("Ana =", y)
