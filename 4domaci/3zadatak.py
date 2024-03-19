studenti = [
    {
        "ime": "Ana",
        "godine": 20,
        "prosjek": 7,
    },
    {
        "ime": "Ivana",
        "godine": 21,
        "prosjek": 8,
    },
    {
        "ime": "Milica",
        "godine": 22,
        "prosjek": 9,
    },
    {
        "ime": "Pero",
        "godine": 23,
        "prosjek": 6,
    },
    {
        "ime": "Mirko",
        "godine": 18,
        "prosjek": 7,
    },
    {
        "ime": "Zivko",
        "godine": 19,
        "prosjek": 8,
    },
    {
        "ime": "Lazar",
        "godine": 18,
        "prosjek": 9,
    },
    {
        "ime": "Jovan",
        "godine": 22,
        "prosjek": 6,
    },
    {
        "ime": "Mara",
        "godine": 24,
        "prosjek": 7,
    },
    {
        "ime": "Mira",
        "godine": 23,
        "prosjek": 8,
    },
]

print(f"Lista svih studenata: {studenti}\n")

stariji_studenti = list(filter(lambda student: student["godine"] > 21, studenti))
print(f"Studenti koji imaju vise od 21 godinu su: {stariji_studenti}\n")

stariji_studenti.sort(key=lambda student: student["prosjek"], reverse=True)
print(f"Stariji studenti sortirani po prosjeku: {stariji_studenti}")
