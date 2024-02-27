def povrsina_lista(sirina_mm, visina_mm):
    # povrsina_mm2 = sirina_mm * visina_mm
    # povrsina_cm2 = povrsina_mm2 / 100
    sirina_cm = sirina_mm / 10
    visina_cm = visina_mm / 10
    povrsina_cm2 = sirina_cm * visina_cm
    return povrsina_cm2


sirina = float(input("Unesite sirinu lista papira u milimetrima: "))
visina = float(input("Unesite visinu lista papira u milimetrima: "))

povrsina = povrsina_lista(sirina, visina)

print(f"Povrsina lista papira je: {povrsina} kvadratnih centimetara.")
