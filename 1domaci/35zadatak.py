petocifreni_broj = int(input("Unesite petocifreni broj: "))

print(
    "Sprat na kome se nalazi stan je:",
    int(str(petocifreni_broj)[2]) + int(str(petocifreni_broj)[4]),
)
