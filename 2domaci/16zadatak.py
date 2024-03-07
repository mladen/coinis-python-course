# Ovo je verzija kada su stranice paralelne sa koordinatnim osama.
# TODO: BONUS: Implementirati i verziju kada stranice nisu paralelne sa koordinatnim osama.

Tacka = (3, 2)

donja_desna_tacka_pravougaonika = (5, 3)
gornja_leva_tacka_pravougaonika = (1, 7)

if (
    Tacka[0] > donja_desna_tacka_pravougaonika[0]
    or Tacka[0] < gornja_leva_tacka_pravougaonika[0]
):
    print("Tacka se ne nalazi unutar pravougaonika")
elif (
    Tacka[1] > donja_desna_tacka_pravougaonika[1]
    or Tacka[1] < gornja_leva_tacka_pravougaonika[1]
):
    print("Tacka se ne nalazi unutar pravougaonika")
else:
    print("Tacka se nalazi unutar pravougaonika")
