def povrsina_i_obim_zida(x1, y1, x2, y2):
    # Izracunavanje sirine i visine pravougaonika
    sirina = abs(x2 - x1)
    visina = abs(y2 - y1)

    # Izracunavanje povrsine
    povrsina = sirina * visina

    # Izracunavanje obima
    obim = 2 * (sirina + visina)

    return povrsina, obim


# Unos koordinata donje desne i gornje leve ivice zida
x1 = float(input("Unesite x koordinatu donje desnog coska zida: "))
y1 = float(input("Unesite y koordinatu donje desnog coska zida: "))
x2 = float(input("Unesite x koordinatu gornjeg lijevog coska zida: "))
y2 = float(input("Unesite y koordinatu gornjeg lijevog coska zida: "))

# Racunanje povrsine i obima zida
povrsina, obim = povrsina_i_obim_zida(x1, y1, x2, y2)

# Ispis rezultata
print("Povrsina zida je:", povrsina)
print("Obim zida je:", obim)
