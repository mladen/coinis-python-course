cijene_akcije_kompanije = [5, 6, 3, 4, 5, 4, 5, 15, 16, 15, 16, 2, 3]

najveci_pad = 0
najveci_rast = 0

for indeks in range(len(cijene_akcije_kompanije) - 1):
    razlika_susjednih_cijena = (
        cijene_akcije_kompanije[indeks + 1] - cijene_akcije_kompanije[indeks]
    )
    if razlika_susjednih_cijena > najveci_rast:
        najveci_rast = razlika_susjednih_cijena
    elif razlika_susjednih_cijena < najveci_pad:
        najveci_pad = razlika_susjednih_cijena

print(f"Najveci rast cijena je {najveci_rast}, a najveci pad je {najveci_pad}.")
