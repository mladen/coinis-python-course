ocjene_na_predmetu_likovno = {
    "Ivan": "5",
    "Marko": "3",
    "Ana": "4",
    "Petar": "3",
    "Jelena": "5",
    "Iva": "5",
    "Maja": "4",
    "Ivana": "5",
    "Matej": "3",
    "Luka": "4",
}

broj_petica = 0
broj_cetvorki = 0
broj_trojki = 0

for ocjena in ocjene_na_predmetu_likovno.values():
    if ocjena == "5":
        broj_petica += 1
    elif ocjena == "4":
        broj_cetvorki += 1
    else:
        broj_trojki += 1

print(f"Broj petica: {broj_petica}")
print(f"Broj cetvorki: {broj_cetvorki}")
print(f"Broj trojki: {broj_trojki}")
