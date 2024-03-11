string = "Prva recenica. Ovo je druga recenica. Na kraju treca"

string_koji_sadrzi_samo_velika_slova = ""

for i in string:
    if i.isupper():
        string_koji_sadrzi_samo_velika_slova += i

print(string_koji_sadrzi_samo_velika_slova)
