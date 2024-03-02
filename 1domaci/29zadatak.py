duza_stranica_pravougaonika = 543
kraca_stranica_pravougaonika = 130

stranica_kvadrata = 65

broj_kvadrata_po_duzoj_stranici_pravougaonika = (
    duza_stranica_pravougaonika // stranica_kvadrata
)

broj_kvadrata_po_kracoj_stranici_pravougaonika = (
    kraca_stranica_pravougaonika // stranica_kvadrata
)

# Ukupan broj kvadrata koji mozemo izrezati
ukupan_broj_kvadrata = (
    broj_kvadrata_po_duzoj_stranici_pravougaonika
    * broj_kvadrata_po_kracoj_stranici_pravougaonika
)

print(
    "Iz pravougaonika dimenzija 543 x 130 je moguce izrezati",
    ukupan_broj_kvadrata,
    "kvadrata stranice 65.",
)
