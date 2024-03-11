zarade = [450, 680, 800, 800, 550]
povecanje = int(
    input("Unesi iznos za koji treba uvecati zarade koje su vece od prosjeka: ")
)
nove_zarade = []

print("Trenutne zarade su: ", zarade)

prosjecna_zarada = sum(zarade) / len(zarade)
print("Prosjecna zarada iznosi: ", prosjecna_zarada)

for zarada in zarade:
    if zarada > prosjecna_zarada:
        nove_zarade.append(zarada + povecanje)
    else:
        nove_zarade.append(zarada)

print("Lista novih zarada je: ", nove_zarade)
