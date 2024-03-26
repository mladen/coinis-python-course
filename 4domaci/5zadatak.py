from functools import reduce
from pprint import pprint

studenti = [
    {"ime": "Ana", "ocjena": 5, "predmet": "matematika"},
    {"ime": "Anja", "ocjena": 4, "predmet": "istorija"},
    {"ime": "Olja", "ocjena": 5, "predmet": "fizika"},
    {"ime": "Ivan", "ocjena": 3, "predmet": "matematika"},
    {"ime": "Marko", "ocjena": 4, "predmet": "matematika"},
    {"ime": "Petar", "ocjena": 5, "predmet": "fizika"},
    {"ime": "Jovan", "ocjena": 2, "predmet": "matematika"},
]


def prosjek_ocjena(acc, student):
    # acc_indeks = next(
    #     (
    #         acc_indeks
    #         for acc_indeks, acc_student in enumerate(acc)
    #         if acc_student["predmet"] == student["predmet"]
    #     ),
    #     None,
    # )

    # add student to acc if not exists
    # if acc_indeks is None:

    # print(f"acc: {acc}\n")

    indeks_predmeta = [
        acc_indeks
        for acc_indeks, acc_student in enumerate(acc)
        if acc_student["predmet"] == student["predmet"]
    ]

    if indeks_predmeta:
        acc[indeks_predmeta[0]]["prosjecna_ocjena"].extend([student["ocjena"]])
        return acc
    else:
        return acc + [
            {"predmet": student["predmet"], "prosjecna_ocjena": [student["ocjena"]]}
        ]


ocjene_po_predmetima = reduce(
    prosjek_ocjena,
    # lambda acc, student: acc + [{student["predmet"]: student["ocjena"]}],
    studenti,
    [],
)

prosjecne_ocjene_po_predmetima = [
    {
        "predmet": student["predmet"],
        "prosjecna_ocjena": sum(student["prosjecna_ocjena"])
        / len(student["prosjecna_ocjena"]),
    }
    for student in ocjene_po_predmetima
]

print(f"\nProsjecne ocjene po predmetima: {prosjecne_ocjene_po_predmetima}\n")
