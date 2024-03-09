posjete_na_utakmicama = {
    "01.03.2022.": [5000, 5500, 6000],
    "02.03.2022.": [6000, 6200],
    "03.03.2022.": [4500, 4800, 4900, 5000],
    "04.03.2022.": [7000, 7200],
    "05.03.2022.": [5500, 5800],
    "06.03.2022.": [8000],
    "07.03.2022.": [7500, 7600],
    "08.03.2022.": [6000],
    "09.03.2022.": [6500, 6700],
    "10.03.2022.": [7000, 7200],
}


# NOTE: ChatGPT predlozio
# broj_posjeta_po_danima = {}
# dan_sa_najvise_posjeta = ""

# for datum, broj_posjeta in posjete_na_utakmicama.items():
#     if isinstance(broj_posjeta, list):
#         broj_posjeta = sum([int(x) for x in broj_posjeta])
#     if datum in broj_posjeta_po_danima:
#         broj_posjeta_po_danima[datum] += int(broj_posjeta)
#     else:
#         broj_posjeta_po_danima[datum] = int(broj_posjeta)

# for datum, broj_posjeta in broj_posjeta_po_danima.items():
#     if broj_posjeta == max(broj_posjeta_po_danima.values()):
#         dan_sa_najvise_posjeta = datum

# print(
#     f"Dan sa najvise posjeta je {dan_sa_najvise_posjeta} sa {max(broj_posjeta_po_danima.values())} posjeta."
# )


# NOTE: Moje rjesenje
broj_posjeta_po_danima = {}
dan_sa_najvise_posjeta = ""

for datum, posjete_u_danu in posjete_na_utakmicama.items():
    broj_posjeta = sum(posjete_u_danu)
    print(f"Na dan {datum} bilo je {broj_posjeta} posjeta.")
    broj_posjeta_po_danima[datum] = broj_posjeta

maksimalne_posjete = 0

for datum, broj_posjeta in broj_posjeta_po_danima.items():
    if broj_posjeta > maksimalne_posjete:
        maksimalne_posjete = broj_posjeta
        dan_sa_najvise_posjeta = datum

print(
    f"Najviše posjeta je bilo dana {dan_sa_najvise_posjeta} i to {maksimalne_posjete} posjeta."
)
