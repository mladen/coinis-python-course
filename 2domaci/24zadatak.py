# tekst = str(input("Unesite tekst: "))
tekst = "Ovo je neki tekst i ima vise od 30 slova! Treba ga skratiti i, na kraju, dodati tri tacke."

if len(tekst) > 30:
    skraceni_tekst = tekst[:30]
    skraceni_tekst += "..."
    print(skraceni_tekst)
