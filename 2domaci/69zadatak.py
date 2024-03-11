zarade = [450, 680, 800, 800, 550]
nove_zarade = []

print("Trenutne zarade su: ", zarade)

prosjecna_zarada = sum(zarade) / len(zarade)
print("Prosjecna zarada iznosi: ", prosjecna_zarada)

for zarada in zarade:
    if zarada > prosjecna_zarada:
        nove_zarade.append(
            zarada - (zarada / 100) * 10
        )  # Zarade iznad prosjeka umanjuje za 10%
    else:
        nove_zarade.append(
            zarada + (zarada / 100) * 10
        )  #  Zarade ispod prosjeka uvecava za 10%

print("Lista novih zarada je: ", nove_zarade)
