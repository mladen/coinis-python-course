from functools import reduce

lista = ["Hello, World!", "Python is cool", "Functional programming rocks"]

broj_rijeci_po_elementu_liste = list(map(lambda element: len(element.split()), lista))

print("Broj rijeci po elementu liste je ", broj_rijeci_po_elementu_liste)

ukupan_broj_rijeci = reduce(lambda x, y: x + y, broj_rijeci_po_elementu_liste)

print("Broj rijeci ", ukupan_broj_rijeci)
