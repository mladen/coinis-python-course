import math


def duzina_trake_za_ivicu_stolnjaka(povrsina):
    # Izracunavanje poluprecnika kruga, preko poznate povrsine
    poluprecnik = math.sqrt(povrsina / math.pi)

    # Izracunavanje obima kruga
    obim = 2 * math.pi * poluprecnik

    return obim


povrsina = float(input("Unesite povrsinu stolnjaka u kvadratnim centimetrima: "))

duzina_trake = duzina_trake_za_ivicu_stolnjaka(povrsina)

print(
    "Potrebna duzina trake za ivicu stolnjaka je: {:.2f} centimetara.".format(
        duzina_trake
    )
)
